(()=>{
'use strict';
document.documentElement.classList.add('js-enabled');
for(const button of document.querySelectorAll('[data-toggle]')){
 button.addEventListener('click',()=>{
  const frame=document.getElementById(button.dataset.toggle);
  const show=frame.classList.toggle('show-fit');
  button.setAttribute('aria-pressed',String(show));
  button.textContent=(show?'Nascondi la ':'Mostra la ')+button.dataset.kind;
 });
}
})();
(()=>{
 const frame=document.querySelector('.plane-frame');
 if(!frame)return;
 const overview=frame.querySelector('.overview'),details=frame.querySelector('details'),scroll=frame.querySelector('.zoom-scroll'),plane=overview.querySelector('#plane');
 scroll.replaceChildren();
 details.addEventListener('toggle',()=>{(details.open?scroll:overview).append(plane);});
})();
