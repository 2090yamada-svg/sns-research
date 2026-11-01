#!/usr/bin/env python3
"""読みやすさチェック: python3 scripts/check.py [BASE_URL]  (要 pip install playwright && playwright install chromium)"""
import sys,re
from playwright.sync_api import sync_playwright
B=(sys.argv[1] if len(sys.argv)>1 else "https://2090yamada-svg.github.io/sns-research/").rstrip("/")+"/"
fails=[];rows=[]
def ok(name,cond,detail=""):
    rows.append((name,"OK" if cond else "NG",detail))
    if not cond: fails.append(name)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page();pg.goto(B)
    posts=sorted(set(pg.eval_on_selector_all(".card a","e=>e.map(a=>a.href)")))
    for w in (360,390,1280):
        pg=b.new_page(viewport={"width":w,"height":800});errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        for u in [B,B+"jewelbox/"]+posts:
            pg.goto(u);pg.wait_for_timeout(400)
            sw,cw=pg.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]")
            ok(f"{w}px 横はみ出しなし {u[len(B)-1:]}",sw<=cw,f"{sw}/{cw}")
            if u in posts and w==390:
                ok(f"画像あり {u[len(B)-1:]}",pg.locator("meta[property='og:image'], .post-hero img, article img").count()>0)
                ok(f"ポイント枠 {u[len(B)-1:]}",pg.locator(".keypoints").count()>0)
                ok(f"図あり {u[len(B)-1:]}",pg.locator(".prose figure").count()>0)
                fs=pg.evaluate("parseFloat(getComputedStyle(document.querySelector('.prose p')).fontSize)")
                ok(f"本文16px以上 {u[len(B)-1:]}",fs>=16,f"{fs}px")
            if u in posts and w==1280:
                mw=pg.evaluate("document.querySelector('.prose p').getBoundingClientRect().width/parseFloat(getComputedStyle(document.querySelector('.prose p')).fontSize)")
                ok(f"1行の文字数(≤45字) {u[len(B)-1:]}",mw<=45,f"{mw:.0f}字")
        for start,sel in ((B,".card a"),(B+"jewelbox/",".jb-item a")):
            pg.goto(start);n=pg.locator(sel).count()
            for i in range(n):
                pg.goto(start);pg.wait_for_timeout(300)
                try:
                    pg.locator(sel).nth(i).click(timeout=3000);pg.wait_for_load_state();good=pg.url!=start
                except Exception: good=False
                ok(f"{w}px クリックで記事へ {start[len(B)-1:]} #{i+1}",good)
        ok(f"{w}px JSエラーなし",not errs,"; ".join(errs)[:100])
    b.close()
for r in rows:
    if r[1]=="NG" or "--all" in sys.argv: print(" | ".join(r))
print(f"合計 {len(rows)} 項目 / NG {len(fails)}")
sys.exit(1 if fails else 0)
