const L=C.L,$=s=>document.querySelector(s);
function build(){
  const k=document.querySelector('input[name=kind]:checked').value,d=$('#d').value,g=$('#g').value.trim(),n=$('#n').value.trim(),x=$('#x').value.trim();
  let date='';if(d){date=new Date(d+'T12:00').toLocaleDateString(L.lang==='af'?'af-ZA':'en-ZA',{weekday:'long',day:'numeric',month:'long',year:'numeric'});}
  const lines=[L.msg_hi.replace('{n}',n?L.dis+n:'').replace('{k}',k.toLowerCase())];
  if(date)lines.push(L.msg_date+': '+date);
  if(g)lines.push(L.msg_g+': '+g);
  if(x)lines.push(L.msg_x+': '+x);
  return lines.join('\n');
}
const upd=()=>$('#msg').textContent=build();
$('#q').addEventListener('input',upd);
$('#q').addEventListener('submit',e=>{e.preventDefault();window.open('https://wa.me/'+C.WA+'?text='+encodeURIComponent(build()),'_blank','noopener');});
document.querySelectorAll('[data-kind]').forEach(a=>a.addEventListener('click',()=>{const r=document.querySelector(`input[name=kind][value="${a.dataset.kind}"]`);if(r){r.checked=true;upd();}}));
upd();
const log=$('#log'),chat=$('#chat');let step=null,o={};
function say(t,w='z'){const m=document.createElement('div');m.className='msg '+w;m.textContent=t;log.appendChild(m);log.scrollTop=log.scrollHeight;}
function open(){chat.classList.add('open');$('#zo').setAttribute('aria-expanded','true');if(!log.children.length)say(L.zara_hi);$('#ai').focus();}
function close(){chat.classList.remove('open');$('#zo').setAttribute('aria-expanded','false');}
$('#zo').onclick=()=>chat.classList.contains('open')?close():open();$('#zc').onclick=close;
function startQ(){step='kind';o={};say(L.f1);}
function flow(t){
  if(step==='kind'){o.kind=t;step='date';return say(L.f2);}
  if(step==='date'){o.date=t;step='guests';return say(L.f3);}
  if(step==='guests'){o.guests=t;step='name';return say(L.f4);}
  if(step==='name'){step=null;say(L.f5.replace('{n}',t.replace(/^./,c=>c.toUpperCase())).replace('{k}',o.kind).replace('{d}',o.date).replace('{g}',o.guests));return say(L.f6);}
}
function answer(t){const q=t.toLowerCase();
  if(step)return flow(t);
  if(new RegExp(L.rx_date).test(q))return startQ();
  if(new RegExp(L.rx_price).test(q))return say(C.A.price);
  if(new RegExp(L.rx_where).test(q))return say(C.A.where);
  if(new RegExp(L.rx_what).test(q))return say(C.A.what);
  say(L.unk.replace('{phone}',C.phone));}
$('#quick').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;say(b.textContent,'u');step=null;b.dataset.q==='date'?startQ():say(C.A[b.dataset.q]);});
$('#ask').addEventListener('submit',e=>{e.preventDefault();const v=$('#ai').value.trim();if(!v)return;say(v,'u');$('#ai').value='';setTimeout(()=>answer(v),350);});
