const fs = require('fs');
const path = require('path');
const katex = require('./katex.min.js');
const esc = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const greek = {'Σ':'\\sum ','Δ':'\\Delta ','θ':'\\theta ','ω':'\\omega ','π':'\\pi ','φ':'\\varphi ','ε':'\\varepsilon ','τ':'\\tau ','α':'\\alpha ','Φ':'\\Phi ','Λ':'\\Lambda ','γ':'\\gamma ','λ':'\\lambda ','ρ':'\\rho ','μ':'\\mu ','σ':'\\sigma ','η':'\\eta ','±':'\\pm ','×':'\\times ','…':'\\cdots '};
function latex(s){
  s=s.replace(/[ΣΔθωπφεταΦΛγλρμση±×…]/g,c=>greek[c]);
  s=s.replace(/(?<![A-Za-z\\])(sin|cos|ln)(?=[^A-Za-z]|$)/g,'\\$1 ');
  s=s.replace(/_\{([A-Za-z,]+)\}/g,(all,sub)=>sub.length>1?'_{\\mathrm{'+sub+'}}':all);
  s=s.replace(/\b(MeV|eV)\b/g,'\\,\\mathrm{$1}').replace(/\bJ\b/g,'\\mathrm{J}');
  return s;
}
function prose(s){
  s=s.replaceAll('本册','本页').replace('在 Word 导航窗格中可直接跳转','可使用左侧目录直接跳转');
  return esc(s).replace(/([A-Za-zα-ωΑ-Ω])_([A-Za-z]+)/g,'$1<sub>$2</sub>').replace(/https:\/\/www\.cambridgeinternational\.org\/Images\/664565-2025-2027-syllabus\.pdf/g,'<a href="https://www.cambridgeinternational.org/Images/664565-2025-2027-syllabus.pdf" target="_blank" rel="noopener">Cambridge 9702 官方考纲 2025–2027</a>');
}
const lines=fs.readFileSync(path.join(__dirname,'p4_core.md'),'utf8').split('\n');
let chapters=[],active=null,eq=0,expr=0,md=[];
for(let line of lines){
  line=line.trim();if(!line)continue;
  if(line.startsWith('# ')){
    active={title:line.slice(2),id:'chapter-'+chapters.length,parts:[]};chapters.push(active);md.push('\n'+line+'\n');
  }else if(line.startsWith('## ')){
    active.parts.push('<h3>'+esc(line.slice(3))+'</h3>');md.push('\n'+line+'\n');
  }else if(line.startsWith('@')){
    const a=line.indexOf('|'),b=line.lastIndexOf('|'),kind=line.slice(1,a),formula=line.slice(a+1,b),note=line.slice(b+1);
    const tex=formula.split(';').map(s=>latex(s.trim()));
    const math=tex.map(t=>{expr++;return '<div class="math-line">'+katex.renderToString(t,{output:'mathml',displayMode:true,throwOnError:true,strict:'error'})+'</div>';}).join('');
    eq++;
    const guide=kind==='推导'?'基础关系 → 代入定义 → 化简并检查条件':'先识别现象 → 选择基础关系 → 检查方向、单位与适用条件';
    active.parts.push('<div class="equation" id="eq-'+eq+'"><div class="eq-meta"><span>'+kind+'</span><span class="eq-number">'+String(eq).padStart(2,'0')+'</span></div><div class="math-group">'+math+'</div><p class="equation-guide">'+guide+'</p><p class="condition">'+prose(note)+'</p><details class="latex"><summary>LaTeX 源码</summary><pre><code>'+esc(tex.join(' \\qquad ; \\qquad '))+'</code></pre></details></div>');
    md.push('\n**'+kind+'**\n',...tex.map(t=>'$$\n'+t+'\n$$\n'),note+'\n');
  }else{
    active.parts.push('<p'+(line.startsWith('对应考纲')?' class="syllabus"':'')+'>'+prose(line)+'</p>');md.push(line.replaceAll('本册','本文').replace('在 Word 导航窗格中可直接跳转','可通过 Markdown 标题导航')+'\n');
  }
}
const nav='<a href="handbook.html">← P4 学习与题型全册</a>'+chapters.map((c,i)=>'<a href="#'+c.id+'">'+esc(i===0?'使用说明':c.title)+'</a>').join('');
const main=chapters.map((c,i)=>'<section id="'+c.id+'" aria-labelledby="heading-'+i+'"><'+(i===0?'h1':'h2')+' id="heading-'+i+'">'+esc(c.title)+'</'+(i===0?'h1':'h2')+'>'+c.parts.join('\n')+'</section>').join('\n');
const html=`<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>P4 核心概念与公式 · 9702 Physics</title>
<style>
:root{--paper:#fcfdfd;--ink:#19313a;--muted:#546972;--line:#d6e2e4;--accent:#17687a;--wash:#edf5f6;--nav:#f4f8f8;--code:#e8eff0;color-scheme:light}.equation-guide{margin:4px 0 10px;padding:8px 12px;border-left:3px solid var(--accent);background:var(--wash);color:var(--accent);font-size:13px;font-weight:650}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:32px}body{margin:0;background:var(--paper);color:var(--ink);font-family:'Avenir Next','PingFang SC','Microsoft YaHei',sans-serif;font-size:17px;line-height:1.9}a{color:var(--accent);text-underline-offset:4px}a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:4px}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:8px;background:var(--paper);z-index:9}
.layout{max-width:1440px;margin:auto;display:grid;grid-template-columns:254px minmax(0,1fr)}aside{height:100vh;position:sticky;top:0;overflow:auto;padding:40px 25px;border-right:1px solid var(--line);background:var(--nav)}.brand{font-size:12px;letter-spacing:2px;color:var(--accent);font-weight:650}.nav-title{font-size:22px;font-weight:650;margin:4px 0 22px}nav a{display:block;text-decoration:none;color:var(--muted);font-size:14px;line-height:1.55;padding:8px 10px;border-left:2px solid transparent}nav a:hover,nav a[aria-current]{color:var(--accent);background:var(--wash);border-color:var(--accent)}.nav-note{font-size:12px;line-height:1.8;margin-top:24px;color:var(--muted)}main{min-width:0;max-width:960px;padding:45px 56px 100px}.edition{font-size:12px;letter-spacing:1.5px;color:var(--accent);margin-bottom:26px}h1{font-family:'Songti SC','STSong',serif;font-size:38px;line-height:1.4;letter-spacing:-.6px;margin:0 0 24px}h2{font-size:27px;line-height:1.5;margin:0 0 16px}h3{font-size:18px;font-weight:650;color:var(--accent);margin:32px 0 13px}section{padding:0 0 46px;margin:0 0 40px;border-bottom:1px solid var(--line)}p{margin:14px 0;overflow-wrap:anywhere}.syllabus{color:var(--muted);font-size:13px}.equation{margin:24px 0 30px;padding:18px 0 17px;border-top:1px solid var(--line)}.eq-meta{display:flex;justify-content:space-between;font-size:12px;color:var(--accent);letter-spacing:.8px}.eq-number{font-variant-numeric:tabular-nums;color:var(--muted)}.math-group{display:flex;flex-wrap:wrap;gap:8px 34px;align-items:center;padding:20px 0 8px;min-width:0}.math-line{max-width:100%;overflow-x:auto;padding:8px 2px}.math-line math{font-size:1.34em;white-space:nowrap;margin:0;text-align:left}.condition{font-size:15px;line-height:1.9;color:var(--muted)}details.latex{font-size:12px;color:var(--muted);margin-top:12px}summary{cursor:pointer;min-height:28px;width:max-content}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--code);color:var(--ink);padding:16px;font:13px/1.7 'SFMono-Regular',Consolas,monospace}sub{font-size:.75em}footer{font-size:12px;color:var(--muted)}.mobile-nav{display:none}
@media(prefers-color-scheme:dark){:root{--paper:#152328;--ink:#dfebec;--muted:#adbec3;--line:#34484f;--accent:#82c7d4;--wash:#23383e;--nav:#192a30;--code:#263a40;color-scheme:dark}}
@media(max-width:850px){.layout{grid-template-columns:205px minmax(0,1fr)}aside{padding:28px 15px}main{padding:34px 30px}body{font-size:16px}h1{font-size:31px}}
@media(max-width:620px){.layout{display:block}aside{position:static;height:auto;padding:22px;border-right:0;border-bottom:1px solid var(--line)}.nav-title{margin:3px 0 8px;font-size:19px}aside nav{display:none}aside .nav-note{display:none}.mobile-nav{display:block}.mobile-nav nav{display:grid;grid-template-columns:1fr 1fr;margin-top:12px}.mobile-nav summary{font-size:14px;min-height:44px;padding-top:6px}main{padding:28px 21px 60px}h1{font-size:29px}h2{font-size:24px}.math-line math{font-size:1.2em}.math-group{gap:8px 20px}section{padding-bottom:28px;margin-bottom:32px}nav a{min-height:44px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{aside,.edition,details.latex,.skip{display:none}.layout{display:block}main{max-width:none;padding:0}body{font-size:11pt;background:white;color:black}.equation{break-inside:avoid}h2,h3{break-after:avoid}section{margin-bottom:15px}.condition{font-size:10pt}a{color:inherit}}
</style></head><body><a class="skip" href="#content">跳到正文</a><div class="layout"><aside><div class="brand">CAMBRIDGE · 9702</div><div class="nav-title">P4 概念与公式</div><nav aria-label="章节目录">${nav}</nav><details class="mobile-nav"><summary>展开章节目录</summary><nav aria-label="移动端章节目录">${nav}</nav></details><p class="nav-note">2025–2027 考纲<br>仅 Paper 4 · 不含 Paper 5<br>公式已嵌入，离线可读。</p></aside><main id="content"><div class="edition">A2 PHYSICS / 核心关系 · 条件 · 易错点</div>${main}<footer>公式使用 LaTeX 排版，每组公式下可展开源码。<a href="https://katex.org/docs/options.html" target="_blank" rel="noopener">渲染说明</a> · 本地参考页面，不上传学习资料。</footer></main></div>
<script>
const chapterLinks=[...document.querySelectorAll('aside nav a')];
const obs=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){chapterLinks.forEach(a=>{if(a.hash==='#'+e.target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}}},{rootMargin:'-5% 0px -75% 0px'});document.querySelectorAll('main section').forEach(s=>obs.observe(s));
</script></body></html>`;
const out=path.resolve(__dirname,'../../output/physics/p4-web');fs.mkdirSync(out,{recursive:true});
fs.writeFileSync(path.join(out,'index.html'),html);
fs.writeFileSync(path.join(out,'P4核心概念与公式.md'),md.join('\n'));
console.log(JSON.stringify({file:path.join(out,'index.html'),chapters:chapters.length,formulaGroups:eq,expressions:expr,bytes:Buffer.byteLength(html)}));
