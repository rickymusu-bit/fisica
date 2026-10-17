
(()=>{
 const index=document.getElementById('indice'),toggle=index.querySelector('summary');
 const links=[...index.querySelectorAll('.sidebar-nav a')];
 const outside=[document.querySelector('main'),document.querySelector('.footer'),...document.querySelectorAll('.topbar>.brand,.top-links>a')];
 function sync(){document.body.classList.toggle('index-open',index.open);outside.forEach(e=>{if(e)e.inert=index.open;});}
 function closeIndex(restore=true){index.open=false;sync();if(restore)toggle.focus({preventScroll:true});}
 index.addEventListener('toggle',sync);
 index.querySelector('.sidebar-backdrop').addEventListener('click',()=>closeIndex());
 document.addEventListener('keydown',e=>{if(!index.open)return;if(e.key==='Escape'){e.preventDefault();closeIndex();}if(e.key==='Tab'){const items=[toggle,...links],first=items[0],last=items[items.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}});
 function mark(id){links.forEach(a=>{if(a.hash==='#'+id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}
 links.forEach(a=>a.addEventListener('click',()=>{mark(a.hash.slice(1));closeIndex(false);const heading=document.getElementById(a.hash.slice(1));if(heading)setTimeout(()=>heading.focus({preventScroll:true}),0);}));
 const headings=[...document.querySelectorAll('[data-toc]')];let scheduled=false;
 function current(){scheduled=false;let active=headings[0];for(const h of headings){if(h.getBoundingClientRect().top<=150)active=h;else break;}if(active)mark(active.id);}
 window.addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(current);}},{passive:true});current();
})();
