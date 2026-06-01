#!/usr/bin/env python3
"""Assemble the per-chapter solution fragments into one self-contained study guide."""
import re, html, pathlib

base = pathlib.Path("/home/kerry/Projects/kaya")

CHAPTERS = [
    ("10", "Public-Key Tools", "Discrete log, CDH & DDH assumptions"),
    ("11", "Public-Key Encryption", "ElGamal, PRFs from DDH/CDH, Paillier"),
    ("12", "CCA-Secure Encryption", "Chosen-ciphertext security, FO, OAEP"),
    ("13", "Digital Signatures", "Definitions, RSA-FDH, blind signatures"),
    ("14", "Signatures from OWFs", "Lamport, Winternitz, strong security"),
    ("15", "Elliptic Curves & Pairings", "EC group law, Montgomery, BLS, BB"),
]
# problems covered in the recitation (shown as a note, NOT solved here)
RECITATION = {"10": ["10.21"], "11": ["11.8"], "12": ["12.20"],
              "13": ["13.6"], "15": ["15.3"]}

HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IAM504 — Public Key Cryptography · Final Study Guide</title>
<script>
window.MathJax = {
  tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']] },
  svg: { fontCache: 'global' }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
<style>
:root{
  --bg:#0f1419; --panel:#161b22; --panel2:#1c2530; --ink:#e6edf3; --mut:#9aa7b2;
  --accent:#4 db8b1; --accent:#3fb6ad; --accent2:#7c93ff; --line:#2a3340; --ok:#3fb950;
  --chip:#222b36; --shadow:0 6px 24px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--ink);}
a{color:var(--accent2);text-decoration:none}
.wrap{display:grid;grid-template-columns:300px 1fr;min-height:100vh}
/* sidebar */
aside{position:sticky;top:0;height:100vh;overflow:auto;background:var(--panel);border-right:1px solid var(--line);padding:20px 16px}
aside h1{font-size:18px;margin:.2em 0 .1em;letter-spacing:.2px}
aside .sub{color:var(--mut);font-size:12.5px;margin-bottom:16px}
.searchbox{width:100%;padding:9px 11px;border-radius:9px;border:1px solid var(--line);background:var(--panel2);color:var(--ink);font-size:14px;margin-bottom:6px}
.searchbox::placeholder{color:var(--mut)}
.tools{display:flex;gap:6px;margin:8px 0 14px}
.tools button{flex:1;padding:7px 6px;border-radius:8px;border:1px solid var(--line);background:var(--panel2);color:var(--mut);font-size:12px;cursor:pointer}
.tools button:hover{color:var(--ink);border-color:var(--accent)}
.progress-wrap{margin:6px 0 18px}
.bar{height:8px;border-radius:99px;background:var(--panel2);overflow:hidden;border:1px solid var(--line)}
.bar>span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .3s}
.progress-label{font-size:12px;color:var(--mut);margin-top:6px}
nav ul{list-style:none;margin:0;padding:0}
nav .chap{display:flex;justify-content:space-between;align-items:center;padding:9px 10px;border-radius:8px;color:var(--ink);font-weight:600;font-size:14px;margin-top:4px}
nav .chap:hover{background:var(--panel2)}
nav .chap .cnt{font-size:11px;color:var(--mut);font-weight:500}
nav .plist{margin:2px 0 8px 8px;padding-left:8px;border-left:1px solid var(--line)}
nav .plist a{display:block;padding:3px 8px;border-radius:6px;font-size:12.5px;color:var(--mut)}
nav .plist a:hover{background:var(--panel2);color:var(--ink)}
nav .plist a.done::before{content:"✓ ";color:var(--ok)}
/* main */
main{padding:34px 44px 120px;max-width:1000px}
.hero{border:1px solid var(--line);background:linear-gradient(180deg,var(--panel2),var(--panel));border-radius:16px;padding:22px 26px;margin-bottom:30px;box-shadow:var(--shadow)}
.hero h2{margin:.1em 0 .3em;font-size:23px}
.hero p{margin:.2em 0;color:var(--mut);font-size:14.5px}
.legend{display:flex;gap:18px;flex-wrap:wrap;margin-top:14px;font-size:12.5px;color:var(--mut)}
.legend b{color:var(--ink)}
.chapter{margin:40px 0 10px;scroll-margin-top:18px}
.chapter>h2.chead{font-size:20px;border-bottom:2px solid var(--accent);padding-bottom:8px;display:flex;align-items:baseline;gap:12px}
.chapter>h2.chead small{color:var(--mut);font-weight:400;font-size:13px}
.recnote{background:var(--chip);border:1px dashed var(--line);border-radius:10px;padding:8px 14px;color:var(--mut);font-size:13px;margin:12px 0}
.recnote b{color:var(--accent)}
/* problem cards */
.problem{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:16px 0;scroll-margin-top:14px;box-shadow:var(--shadow)}
.problem.hidden{display:none}
.phead{display:flex;align-items:center;gap:12px}
.ptitle{margin:0;font-size:17px;flex:1}
.pnum{display:inline-block;background:var(--accent);color:#06231f;font-weight:700;border-radius:7px;padding:2px 9px;font-size:14px;margin-right:6px}
.pname{color:var(--mut);font-weight:500;font-size:15px}
.chk{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--mut);cursor:pointer;user-select:none;white-space:nowrap}
.chk input{width:16px;height:16px;accent-color:var(--ok);cursor:pointer}
.statement{margin:12px 0 6px;color:#cdd9e5;font-size:14.5px;background:var(--panel2);border-left:3px solid var(--accent2);border-radius:0 8px 8px 0;padding:10px 14px}
.statement p{margin:.3em 0}
.toggle{margin-top:10px;background:var(--accent2);color:#0a1030;border:none;border-radius:8px;padding:8px 16px;font-size:13px;font-weight:600;cursor:pointer}
.toggle:hover{filter:brightness(1.08)}
.solution{margin-top:14px;border-top:1px dashed var(--line);padding-top:6px;display:none;animation:fade .25s}
.solution.open{display:block}
@keyframes fade{from{opacity:0;transform:translateY(-4px)}to{opacity:1}}
.solution h4{color:var(--accent);margin:16px 0 4px;font-size:14px;text-transform:uppercase;letter-spacing:.6px}
.solution p{margin:.5em 0}
.solution .idea, .solution>h4:first-of-type + p{}
mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}
.toTop{position:fixed;right:22px;bottom:22px;background:var(--accent);color:#06231f;border:none;border-radius:50%;width:46px;height:46px;font-size:20px;cursor:pointer;box-shadow:var(--shadow);display:none}
.toTop.show{display:block}
@media(max-width:880px){.wrap{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:22px}}
.noresult{color:var(--mut);font-style:italic;padding:20px}
</style>
</head>
<body>
<div class="wrap">
<aside>
  <h1>IAM504 · PKC</h1>
  <div class="sub">Boneh–Shoup final · exercise solutions</div>
  <input id="search" class="searchbox" placeholder="Search problems… (e.g. ElGamal, 12.3, DDH)">
  <div class="tools">
    <button onclick="allSol(true)">Expand all</button>
    <button onclick="allSol(false)">Collapse all</button>
  </div>
  <div class="progress-wrap">
    <div class="bar"><span id="pbar"></span></div>
    <div class="progress-label"><span id="pcount">0</span> / 32 marked mastered · <a href="#" onclick="resetProg();return false">reset</a></div>
  </div>
  <nav id="nav"></nav>
</aside>
<main>
  <div class="hero">
    <h2>Public Key Cryptography — Final Exam Study Guide</h2>
    <p>Full worked solutions to the 32 Boneh–Shoup exercises flagged as exam-similar, in the recitation's proof style.</p>
    <p>Each card: faithful problem statement → <b>Idea</b> (intuition) → <b>Solution</b> (rigorous reduction).</p>
    <div class="legend">
      <span><b>Click</b> a problem's button to reveal its solution.</span>
      <span><b>☐ mastered</b> checkbox saves to this browser.</span>
      <span><b>Search</b> filters live.</span>
    </div>
  </div>
"""

FOOT = r"""
</main>
</div>
<button class="toTop" id="toTop" onclick="scrollTo({top:0,behavior:'smooth'})">↑</button>
<script>
const KEY='iam504_progress_v1';
let prog=JSON.parse(localStorage.getItem(KEY)||'{}');
const problems=[...document.querySelectorAll('.problem')];
const TOTAL=problems.length;

// wire each problem: toggle + checkbox + nav anchor data
problems.forEach(p=>{
  const id=p.id;
  const btn=p.querySelector('.toggle');
  const sol=p.querySelector('.solution');
  btn.addEventListener('click',()=>{ sol.classList.toggle('open');
    btn.textContent=sol.classList.contains('open')?'Hide solution':'Show solution'; });
  // checkbox
  const head=p.querySelector('.phead')||p.querySelector('.ptitle').parentNode;
  const lbl=document.createElement('label'); lbl.className='chk';
  const cb=document.createElement('input'); cb.type='checkbox'; cb.checked=!!prog[id];
  lbl.appendChild(cb); lbl.appendChild(document.createTextNode('mastered'));
  cb.addEventListener('change',()=>{ prog[id]=cb.checked; save(); });
  head.appendChild(lbl);
});

function save(){ localStorage.setItem(KEY,JSON.stringify(prog)); paint(); }
function paint(){
  const done=problems.filter(p=>prog[p.id]).length;
  document.getElementById('pbar').style.width=(100*done/TOTAL)+'%';
  document.getElementById('pcount').textContent=done;
  document.querySelectorAll('nav .plist a').forEach(a=>{
    a.classList.toggle('done', !!prog[a.dataset.id]);
  });
}
function resetProg(){ if(confirm('Clear all mastered marks?')){prog={};save();
  document.querySelectorAll('.chk input').forEach(c=>c.checked=false);} }
function allSol(open){ document.querySelectorAll('.problem').forEach(p=>{
  if(p.classList.contains('hidden'))return;
  const s=p.querySelector('.solution'),b=p.querySelector('.toggle');
  s.classList.toggle('open',open); b.textContent=open?'Hide solution':'Show solution'; }); }

// build nav
const nav=document.getElementById('nav'); let navHTML='<ul>';
document.querySelectorAll('.chapter').forEach(ch=>{
  const h=ch.querySelector('h2.chead'); const num=ch.id.replace('ch-','');
  const ps=[...ch.querySelectorAll('.problem')];
  navHTML+=`<li><a class="chap" href="#${ch.id}">Ch ${num} <span class="cnt">${ps.length} probs</span></a><div class="plist">`;
  ps.forEach(p=>{ const t=p.querySelector('.pnum').textContent.trim();
    navHTML+=`<a href="#${p.id}" data-id="${p.id}">${t}</a>`; });
  navHTML+='</div></li>';
});
navHTML+='</ul>'; nav.innerHTML=navHTML;

// search filter
const search=document.getElementById('search');
search.addEventListener('input',()=>{
  const q=search.value.trim().toLowerCase();
  let anyChap=false;
  document.querySelectorAll('.chapter').forEach(ch=>{
    let vis=0;
    ch.querySelectorAll('.problem').forEach(p=>{
      const txt=p.textContent.toLowerCase();
      const show=!q||txt.includes(q);
      p.classList.toggle('hidden',!show); if(show)vis++;
    });
    ch.style.display=vis?'':'none'; if(vis)anyChap=true;
  });
});

// back to top
const toTop=document.getElementById('toTop');
addEventListener('scroll',()=>toTop.classList.toggle('show',scrollY>500));
paint();
</script>
</body>
</html>
"""

out = [HEAD]
for num, title, desc in CHAPTERS:
    frag = (base / f"sol_ch{num}.html").read_text(encoding="utf-8")
    out.append(f'<section class="chapter" id="ch-{num}">')
    out.append(f'<h2 class="chead">Chapter {num} · {title} <small>{desc}</small></h2>')
    if num in RECITATION:
        skipped = ", ".join(RECITATION[num])
        out.append(f'<div class="recnote">Solved in the <b>recitation</b> (not repeated here): '
                   f'{skipped}.</div>')
    out.append(frag)
    out.append('</section>')
out.append(FOOT)

final = "\n".join(out)
dest = base / "IAM504_study_guide.html"
dest.write_text(final, encoding="utf-8")
print(f"wrote {dest}  ({len(final)} bytes)")
print(f"sections: {final.count('<section class=\"problem\"')}")
print(f"chapters: {final.count('<section class=\"chapter\"')}")
