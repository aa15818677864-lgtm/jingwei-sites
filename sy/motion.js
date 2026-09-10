(()=>{'use strict';
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
const items=document.querySelectorAll('.reveal');
if(!reduced.matches&&'IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target);}})},{threshold:.08,rootMargin:'0px 0px -15px 0px'});items.forEach((el,i)=>{el.style.setProperty('--delay',`${Math.min(i%2*80,80)}ms`);observer.observe(el)});document.body.classList.add('motion-ready');}
const menu=document.getElementById('siteMenu'),toggle=document.getElementById('menuButton');
function closeMenu(){menu.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','打開菜單');}
toggle.addEventListener('click',()=>{const open=menu.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'關閉菜單':'打開菜單');});
menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeMenu();document.getElementById('successModal').style.display='none';}});
document.addEventListener('click',e=>{if(!e.target.closest('.header'))closeMenu()});
const progress=document.querySelector('.reading-progress'),floating=document.querySelector('.floating-contact'),contact=document.getElementById('contact');let queued=false;
function update(){const max=document.documentElement.scrollHeight-innerHeight;progress.style.transform=`scaleX(${max>0?scrollY/max:0})`;const r=contact.getBoundingClientRect();floating.classList.toggle('show',scrollY>450&&!(r.top<innerHeight&&r.bottom>0));queued=false}
addEventListener('scroll',()=>{if(!queued){requestAnimationFrame(update);queued=true}},{passive:true});addEventListener('resize',update);update();
// Keep keyboard focus inside the homepage-compatible success dialog.
const modal=document.getElementById('successModal'),close=document.getElementById('modalCloseBtn');let previousFocus=null;
new MutationObserver(()=>{if(modal.style.display==='flex'){previousFocus=document.activeElement;close.focus();}else if(previousFocus){previousFocus.focus();previousFocus=null;}}).observe(modal,{attributes:true,attributeFilter:['style']});
modal.addEventListener('keydown',e=>{if(e.key==='Tab'){e.preventDefault();close.focus();}});
})();
