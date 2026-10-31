(function(){var m=document.getElementById('menu'),o=document.getElementById('menuOpen'),c=document.getElementById('menuClose');
function set(v){if(v){m.hidden=false;requestAnimationFrame(function(){m.classList.add('open')});}else{m.classList.remove('open');setTimeout(function(){m.hidden=true},300);}
m.setAttribute('aria-hidden',!v);o.setAttribute('aria-expanded',v);document.body.style.overflow=v?'hidden':'';}
o.onclick=function(){set(true)};c.onclick=function(){set(false)};
m.addEventListener('click',function(e){if(e.target.tagName==='A')set(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});
if(location.hash==='#menu')set(true);})();
