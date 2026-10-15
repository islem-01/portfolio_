(() => {
 const toggle=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav');
 if(toggle&&nav){toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');toggle.textContent=open?'×':'☰'});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='☰'}));}

 const themeButtons=document.querySelectorAll('.theme-toggle');
 const applyTheme=(mode)=>{document.body.classList.toggle('light-mode',mode==='light');themeButtons.forEach(btn=>{btn.textContent=mode==='light'?'☾':'☼';btn.setAttribute('aria-label',mode==='light'?'Activer le thème sombre':'Activer le thème clair');btn.title=mode==='light'?'Passer au thème sombre':'Passer au thème clair';});};
 let savedTheme='dark';try{savedTheme=localStorage.getItem('portfolio-theme')||'dark';}catch(e){} applyTheme(savedTheme);
 themeButtons.forEach(btn=>btn.addEventListener('click',()=>{const next=document.body.classList.contains('light-mode')?'dark':'light';applyTheme(next);try{localStorage.setItem('portfolio-theme',next);}catch(e){}}));


 // Timeline cards can be opened by mouse or keyboard while preserving real links.
 document.querySelectorAll('[data-card-href]').forEach(card=>{
   const go=()=>{window.location.href=card.dataset.cardHref;};
   card.addEventListener('click',e=>{if(e.target.closest('a,button,input,video,label'))return;go();});
   card.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target===card){e.preventDefault();go();}});
 });
 // Optional local video previews: files are never uploaded or sent anywhere.
 document.querySelectorAll('[data-video-preview]').forEach(input=>input.addEventListener('change',()=>{
   const role=input.dataset.videoPreview,player=document.querySelector(`[data-video-player="${role}"]`),hint=document.querySelector(`[data-video-hint="${role}"]`);
   if(!player||!input.files||!input.files[0])return;
   if(player.dataset.objectUrl)URL.revokeObjectURL(player.dataset.objectUrl);
   const url=URL.createObjectURL(input.files[0]);player.dataset.objectUrl=url;player.src=url;player.hidden=false;
   if(hint)hint.textContent=`Prévisualisation locale : ${input.files[0].name}. Cette vidéo n’est pas téléversée sur le site.`;
   player.load();
 }));

 const year=document.getElementById('year');if(year)year.textContent=new Date().getFullYear();
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches,canvas=document.getElementById('particles');
 if(canvas&&!reduced){const ctx=canvas.getContext&&canvas.getContext('2d');if(ctx){let w=0,h=0,pts=[],raf=0,mouse={x:-9999,y:-9999};const resize=()=>{w=canvas.width=Math.min(window.innerWidth,1800);h=canvas.height=window.innerHeight;const count=Math.min(70,Math.max(22,Math.floor(w/22)));pts=Array.from({length:count},()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,r:Math.random()*1.6+.5,c:Math.random()<.6?'56,189,248':Math.random()<.5?'167,139,250':'251,191,36'}));};resize();window.addEventListener('resize',resize,{passive:true});window.addEventListener('pointermove',e=>{mouse.x=e.clientX;mouse.y=e.clientY},{passive:true});let running=true;document.addEventListener('visibilitychange',()=>{running=!document.hidden;if(running&&!raf)draw()});function draw(){raf=0;if(!running)return;ctx.clearRect(0,0,w,h);for(let i=0;i<pts.length;i++){const p=pts[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;const dx=p.x-mouse.x,dy=p.y-mouse.y,d=Math.sqrt(dx*dx+dy*dy);if(d<100){p.x+=dx/d*.12;p.y+=dy/d*.12;}ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(${p.c},.72)`;ctx.fill();for(let j=i+1;j<pts.length;j++){const q=pts[j],xx=p.x-q.x,yy=p.y-q.y,dd=Math.sqrt(xx*xx+yy*yy);if(dd<105){ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.strokeStyle=`rgba(63,123,245,${(1-dd/105)*.16})`;ctx.lineWidth=.6;ctx.stroke();}}}raf=requestAnimationFrame(draw)}draw();window.addEventListener('pagehide',()=>{if(raf)cancelAnimationFrame(raf);window.removeEventListener('resize',resize)});}}
 const projectCards=[...document.querySelectorAll('.project-card[data-category]')];
 let activeType='all',activeDomain='all';
 const filterProjects=()=>{let visible=0;projectCards.forEach(card=>{const categories=(card.dataset.category||'').split(/\s+/),domains=(card.dataset.domains||'').split(/\s+/);const typeMatch=activeType==='all'||categories.includes(activeType);const domainMatch=activeDomain==='all'||domains.includes(activeDomain);const show=typeMatch&&domainMatch;card.hidden=!show;if(show)visible++;});const empty=document.querySelector('.empty-state');if(empty)empty.style.display=visible?'none':'block';};
 document.querySelectorAll('.type-filter').forEach(btn=>btn.addEventListener('click',()=>{activeType=btn.dataset.filter;document.querySelectorAll('.type-filter').forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));filterProjects();}));
 document.querySelectorAll('.domain-filter').forEach(btn=>btn.addEventListener('click',()=>{activeDomain=btn.dataset.domainFilter;document.querySelectorAll('.domain-filter').forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));filterProjects();}));
})();
