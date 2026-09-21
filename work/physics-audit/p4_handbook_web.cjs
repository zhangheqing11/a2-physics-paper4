const fs=require('fs'),path=require('path'),katex=require('./katex.min.js');
const base=path.resolve(__dirname,'../../output/physics/p4-web');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'p4_reader_content.json'),'utf8'));
const core=fs.readFileSync(path.join(base,'index.html'),'utf8');
const qpblocks=JSON.parse(fs.readFileSync(path.join(__dirname,'p4_qpblocks.json'),'utf8'));
const mapped=JSON.parse(fs.readFileSync(path.join(__dirname,'p4_mapped.json'),'utf8'));
const rowLookup=new Map(mapped.map(r=>[r.paper+'|'+r.q,r]));
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const superMap={'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-','⁺':'+'};
const subMap={'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9'};
const symbols={'Σ':'\\sum ','Δ':'\\Delta ','θ':'\\theta ','ω':'\\omega ','π':'\\pi ','φ':'\\varphi ','ε':'\\varepsilon ','τ':'\\tau ','α':'\\alpha ','Φ':'\\Phi ','λ':'\\lambda ','ρ':'\\rho ','μ':'\\mu ','σ':'\\sigma ','η':'\\eta ','±':'\\pm ','×':'\\times ','≈':'\\approx ','∝':'\\propto ','≥':'\\ge ','≤':'\\le ','→':'\\to ','∞':'\\infty ','−':'-','½':'\\tfrac{1}{2}','⅓':'\\tfrac{1}{3}','⅔':'\\tfrac{2}{3}','ℏ':'\\hbar '};
function tex(s){
 s=s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+/g,x=>'^{'+[...x].map(c=>superMap[c]).join('')+'}').replace(/[₀₁₂₃₄₅₆₇₈₉]+/g,x=>'_{'+[...x].map(c=>subMap[c]).join('')+'}');
 s=s.replace(/_(rms|max|min|escape|orbit|th|liquid|container|loss|in|on|by|eq|osc|rad|high|low|act|half|acc|star|obs|[A-Za-z])/g,(_,x)=>'_{'+(x.length>1?'\\mathrm{'+x+'}':x)+'}');
 // Preserve scope of radicals and parenthesised powers, not just the next glyph.
 s=s.replace(/\^\(([^()]+)\)/g,'^{$1}');
 while(/√\(([^()]+)\)/.test(s))s=s.replace(/√\(([^()]+)\)/g,'\\sqrt{$1}');
 s=s.replace(/√([A-Za-z0-9]+)/g,'\\sqrt{$1}');
 s=s.replace(/[ΣΔθωπφεταΦλρμση±×≈∝≥≤→∞−½⅓⅔ℏ]/g,c=>symbols[c]);
 s=s.replace(/(?<![A-Za-z\\])(sin|cos|tan|ln|exp)(?=[^a-z]|$)/g,'\\$1 ');
 s=s.replace(/√[〈⟨]([^〉⟩]+)[〉⟩]/g,'\\sqrt{\\langle $1\\rangle}');
 return s;
}
const conversions=[],failures=[];
function sourceParts(text){
 const m=text.match(/^([smw]\d{2})\/(\d{2}) Q([^\s]+)/); if(!m)return null;
 return {short:m[1]+'/'+m[2],paper:'9702_'+m[1]+'_'+m[2],q:m[3]};
}
function cleanQuestion(raw){
 const lines=raw.replace(/\r/g,'').split('\n');
 const cleaned=[];
 for(let line of lines){
  const trimmed=line.trim();
  if(!trimmed) { cleaned.push(''); continue; }
  if(/^=== MERGED PAGE \d+/.test(trimmed))continue;
  if(/^© UCLES/.test(trimmed)||/^9702\/\d{2}\/[A-Z]\/[^\s]+/.test(trimmed))continue;
  if(/DO NOT WRITE IN THIS MARGIN|TURN OVER|For Examiner's Use/i.test(trimmed))continue;
  if(/^\*[^*]+\*.*$/.test(trimmed)||/^\s*\d{1,3}\s*$/.test(trimmed))continue;
  if(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(line))continue;
  const nonAscii=[...trimmed].filter(c=>c.charCodeAt(0)>127).length;
  const asciiWords=(trimmed.match(/[A-Za-z]{2,}/g)||[]).join('');
  if(nonAscii>=3&&nonAscii/Math.max(trimmed.length,1)>.22&&asciiWords.length<4)continue;
  if(/^[.·_\-=–—\s]{8,}$/.test(trimmed))continue;
  if(/\.{8,}|_{8,}/.test(line))continue;
  line=line.replace(/\s*\[Total:\s*\d+\]\s*$/i,'').replace(/\s+\[\d+\]\s*$/,'').replace(/[ \t]+$/,'');
  if(!line.trim())continue;
  cleaned.push(line);
 }
 while(cleaned.length&&cleaned[0]==='')cleaned.shift();
 while(cleaned.length&&cleaned[cleaned.length-1]==='')cleaned.pop();
 const out=[];let blanks=0;
 for(const line of cleaned){if(!line.trim()){blanks++;if(blanks>1)continue;}else blanks=0;out.push(line);}
 return out.join('\n').replace(/^\s+|\s+$/g,'').trim();
}
function targetQuestion(raw,q){
 const parts=q.match(/\([^)]+\)/g)||[];
 if(!parts.length)return cleanQuestion(raw);
 const lines=raw.replace(/\r/g,'').split('\n');
 const topLetter=parts[0].slice(1,-1);
 const topRe=new RegExp('^\\s*(?:\\d+\\s+)?\\('+topLetter+'\\)(?:\\s|$)');
 const start=lines.findIndex(line=>topRe.test(line));
 if(start<0)return cleanQuestion(raw);
 const nextTop=/^\s*(?:\d+\s+)?\([a-h]\)(?:\s|$)/;
 let end=lines.findIndex((line,i)=>i>start&&nextTop.test(line));
 if(end<0)end=lines.length;
 let selected=lines.slice(start,end);
 if(parts.length>1){
  const roman=parts[1].slice(1,-1);
  const segment=selected.join('\n');
  const nestedRe=/\((i{1,3}|iv|v|vi{0,3}|ix|x)\)(?=\s|$)/gi;
  const nested=[...segment.matchAll(nestedRe)];
  const target=nested.findIndex(m=>m[1].toLowerCase()===roman.toLowerCase());
  if(target>=0){
   const parentEnd=nested[0].index;
   const targetStart=nested[target].index;
   const targetEnd=target+1<nested.length?nested[target+1].index:segment.length;
   selected=(segment.slice(0,parentEnd)+'\n'+segment.slice(targetStart,targetEnd)).split('\n');
  }
 }
 return cleanQuestion(selected.join('\n'));
}
function questionPanel(text){
 const p=sourceParts(text); if(!p||!qpblocks[p.paper])return '';
 const block=qpblocks[p.paper][p.q.split('(')[0]]; if(!block)return '';
 const row=rowLookup.get(p.paper+'|'+p.q);
 const answer=row?.answer||'';
 return '<div class="question"><div class="qmeta">代表真题 · '+esc(p.short)+' · Q'+esc(p.q)+' · '+(row?.marks||'?')+' 分</div><p class="question-context">原题题目（保留该小问所属前置条件）</p><pre class="question-text">'+esc(targetQuestion(block.text,p.q))+'</pre><p class="source">QP 合并第'+esc(String(row?.qp_page||block.page))+'页起 · MS 合并第'+esc(String(row?.page||''))+'页</p>'+(answer?'<details class="mark-scheme"><summary>展开对应评分标准摘录</summary><pre>'+esc(answer)+'</pre></details>':'')+'</div>';
}
function prose(s,math=true){
 if(!math)return esc(s);
 const re=/[A-Za-z0-9(ΣΔθωπφεταΦλρμσηℏ½⅓⅔][A-Za-z0-9ΣΔθωπφεταΦλρμσηℏ½⅓⅔⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉_{}()\[\].+\-−×*/^=≈∝≥≤<>√→∞±|〈〉⟨⟩]*/g;
 let html='',pos=0;
 for(const m of s.matchAll(re)){
  let token=m[0];
  if(!/[=≈∝≥≤√]|[⁰¹²³⁴⁵⁶⁷⁸⁹]/.test(token)||token.length<3)continue;
  // Unmatched parentheses belong to the surrounding prose, not the formula.
  while(token.endsWith(')')&&[...token].filter(c=>c===')').length>[...token].filter(c=>c==='(').length)token=token.slice(0,-1);
  token=token.replace(/[.,]+$/,'');
  if(/[=≈∝≥≤_√]$/.test(token)||[...token].filter(c=>c==='(').length!==[...token].filter(c=>c===')').length)continue;
  const latex=tex(token);
  try{
   const rendered=katex.renderToString(latex,{output:'mathml',displayMode:false,throwOnError:true,strict:'error'});
   html+=esc(s.slice(pos,m.index))+'<span class="inline-math" data-original="'+esc(token)+'" title="'+esc(token)+'">'+rendered+'</span>';
   pos=m.index+token.length;conversions.push({original:token,latex});
  }catch(e){failures.push({original:token,error:e.message});}
 }
 return html+esc(s.slice(pos));
}
const sections=[];let section={title:'P4 学习与题型全册',id:'start',blocks:[]};sections.push(section);
data.blocks.forEach((b,i)=>{if(b.kind==='p'&&b.style==='Heading1'){section={title:b.text,id:'section-'+sections.length,blocks:[]};sections.push(section);}else section.blocks.push({...b,index:i});});
let types=0,representatives=0,practice=0,sources=0,papers=0,indexRows=0,figure=0;
const typeRecords=[];
const mapping={入门:1,C:2,G:3,T:4,K:5,H:6,S:7,E:8,D:9,B:10,I:10,A:11,Q:12,N:13,M:14,Z:15};
function formulaPanel(title){
 const key=title.startsWith('入门')?'入门':title.split(' ')[0];const n=mapping[key];if(n===undefined)return '';
 const match=core.match(new RegExp('<section id="chapter-'+n+'"[^>]*>([\\s\\S]*?)</section>'));
 if(!match)throw Error('Missing formula chapter '+n);
 let body=match[1].replace(/<h2[^>]*>[\s\S]*?<\/h2>/,'').replace(/id="([^"]+)"/g,'id="'+key+'-$1"');
 return '<details class="formula-panel"><summary>本章核心概念与公式速查</summary><p class="source-note">补充阅读：来自配套《核心概念与公式》。'+(key==='B'||key==='I'?'磁场与电磁感应共用这一组速查。':'')+'<a href="index.html#chapter-'+n+'">在公式册中阅读 ↗</a></p>'+body+'</details>';
}
 function renderSection(s){
 let out='',articleOpen=false,paperOpen=false,tree=false,currentType=null;
 const isIndex=s.title==='全部试卷与小问索引';
 function closeArticle(){if(articleOpen){out+='</article>';articleOpen=false;}}
 function closePaper(){if(paperOpen){out+='</details>';paperOpen=false;}}
 for(const b of s.blocks){
  if(b.kind==='image'){figure++;out+='<figure><img loading="lazy" src="'+b.data+'" alt="图像速查 '+figure+'：原册四幅物理关系示意图"><figcaption>原册图像速查 '+figure+'；无量纲示意，具体作图以题给坐标与条件为准。</figcaption></figure>';continue;}
  if(b.kind==='table'){out+='<div class="table-scroll"><table>'+b.rows.map((r,i)=>'<tr>'+r.map(c=>'<'+(i?'td':'th scope="col"')+'>'+prose(c)+'</'+(i?'td':'th')+'>').join('')+'</tr>').join('')+'</table></div>';continue;}
  let text=b.text;
  if(b.style==='Title')continue;
  if(text.startsWith('在Word中可使用导航窗格'))text='使用左侧章节目录跳转；每章题型树可直达条目。浏览器搜索可以定位正文；折叠索引可先用“展开全部索引”打开后搜索。所有原题出处仍在同一页中。';
  if(b.style==='Heading2'){
   const m=text.match(/^([A-Z]\d{2}) /);
   if(m){closeArticle();types++;typeRecords.push({code:m[1],title:text,section:s.title});currentType=m[1];articleOpen=true;tree=false;out+='<article class="type-entry" id="'+m[1]+'"><div class="card-head"><span class="type-code">'+m[1]+'</span><h3>'+esc(text.slice(4))+'</h3></div>';continue;}
   if(isIndex){closePaper();papers++;paperOpen=true;out+='<details class="paper-index" id="paper-'+text.split(' ')[0].replaceAll('/','-')+'"><summary>'+esc(text)+'</summary>';continue;}
   tree=text==='本章题型树';out+='<h3>'+esc(text)+'</h3>';continue;
  }
  if(b.style==='Heading3'){out+='<h4>'+esc(text)+'</h4>';continue;}
  if(tree&&/^[A-Z]\d{2}\s/.test(text)){out+='<p class="type-link"><a href="#'+text.slice(0,3)+'">'+prose(text)+'</a></p>';continue;}
  if(text.startsWith('本类型完整题源')){sources++;out+='<details class="type-sources"><summary>本类型完整题源</summary><p>'+prose(text.replace(/^本类型完整题源\s*/,''),false)+'</p></details>';continue;}
  if(isIndex&&b.style==='Indextext'){
   const entries=text.split('； ');indexRows+=entries.length;
   out+='<ul class="question-list">'+entries.map(t=>'<li>'+esc(t).replace(/\b([A-Z]\d{2})\b/g,'<a href="#$1">$1</a>')+'</li>').join('')+'</ul>';continue;
  }
  const label=text.match(/^(细分考法|识别与模型|代表题讲解|英文表达|常见失分|下一道变式)\s+/);
  if(label){if(label[1]==='代表题讲解')representatives++;if(label[1]==='下一道变式')practice++;const shown={'细分考法':'识别信号','识别与模型':'核心公式与条件','代表题讲解':'解题思路与评分点','常见失分':'常见失分','下一道变式':'迁移练习','英文表达':'英文表达'}[label[1]];out+='<div class="field '+({'代表题讲解':'worked','常见失分':'trap','下一道变式':'practice','英文表达':'english','识别与模型':'model'}[label[1]]||'')+'"><h4>'+shown+'</h4><p>'+prose(text.slice(label[0].length))+'</p></div>';}
  else if(/^[smw]\d{2}\/\d{2} Q/.test(text))out+=questionPanel(text);
  else out+='<p class="'+(b.style==='Sourcenote'?'source-note':'')+'">'+prose(text,!isIndex)+'</p>';
 }
 closeArticle();closePaper();
 return '<section id="'+s.id+'"><'+(s.id==='start'?'h1':'h2')+'>'+esc(s.title)+'</'+(s.id==='start'?'h1':'h2')+'>'+formulaPanel(s.title)+out+'</section>';
}
const rendered=sections.map(renderSection).join('\n');
if(types!==85||representatives!==85||practice!==85||sources!==85||papers!==25||indexRows!==1250||figure!==2)throw Error(JSON.stringify({types,representatives,practice,sources,papers,indexRows,figure}));
const nav=sections.map(s=>'<a href="#'+s.id+'">'+esc(s.title.replace('P4 学习与题型全册','全册说明'))+'</a>').join('');
const typeNav=typeRecords.map(t=>'<a href="#'+t.code+'"><span>'+t.code+'</span>'+esc(t.title.slice(4))+'</a>').join('');
const stats='<div class="stats"><div><strong>85</strong><span>题型卡片</span></div><div><strong>1250</strong><span>条小问索引</span></div><div><strong>25</strong><span>份 P4 试卷</span></div><div><strong>2500</strong><span>总分记录</span></div></div>';
const css=core.match(/<style>([\s\S]*?)<\/style>/)[1];
const extra=`
:root{color-scheme:light;--paper:#fffdf8;--ink:#172b35;--muted:#49616b;--line:#d7e0df;--accent:#145f73;--wash:#edf4f3;--nav:#f3f8f7;--code:#f1eee6}html{background:var(--paper)}body{font-family:'PingFang SC','Hiragino Sans GB','Microsoft YaHei',Arial,sans-serif;font-size:18px;line-height:1.88;letter-spacing:.01em;-webkit-font-smoothing:antialiased}main{max-width:1040px}section{border-bottom:0}.type-entry .card-head{border-bottom:0}.type-entry .card-head h3{font-size:25px;line-height:1.42}.field h4{font-size:15px;letter-spacing:.04em}.field p{font-size:17px;line-height:1.9;color:var(--ink)}.worked{font-size:18px;line-height:1.95}.question-context{font-size:14px;color:var(--muted);font-weight:650;margin:4px 0 10px}.question-text,.mark-scheme pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f1e9;color:#1b2b33;border:1px solid #e2ddd0;border-radius:7px;padding:16px 18px;font:15px/1.75 'SFMono-Regular','Menlo','Consolas','PingFang SC',monospace;letter-spacing:0}.question-text{margin:0 0 10px}.mark-scheme{margin-top:12px}.mark-scheme summary{font-size:14px;font-weight:700;color:var(--accent)}.source{font-size:14px}.qmeta{font-size:14px}.type-sources{border-top:0}.type-sources summary{font-size:14px;font-weight:700}.practice{font-size:17px;line-height:1.9}.type-nav a{font-size:13px}.question-list{font-size:15px;line-height:1.9}
.book-links{font-size:14px;margin:18px 0 26px}.book-links a{display:inline-block;margin-right:18px}.hero{background:linear-gradient(130deg,#173b5c,#2c6594);color:#fff;border-radius:18px;padding:30px 34px;margin:0 0 24px;box-shadow:0 12px 28px #193a5422}.hero h1{color:#fff;margin:0 0 12px;font-size:clamp(28px,4vw,44px)}.hero p{color:#e5f0f8;margin:7px 0;font-size:15px}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:24px}.stats div{border-left:1px solid #ffffff66;padding-left:12px}.stats strong{display:block;font-size:25px;line-height:1.2}.stats span{font-size:12px;color:#d7e8f3}.quick-nav{margin:16px 0 24px;border:1px solid var(--line);border-radius:12px;background:var(--wash);padding:6px 12px}.quick-nav summary{color:var(--accent);font-weight:700}.type-nav{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px 16px;padding:8px 0 12px}.type-nav a{display:block;text-decoration:none;color:var(--muted);font-size:12px;line-height:1.45;padding:5px 7px;border-radius:6px}.type-nav a:hover{background:var(--paper);color:var(--accent)}.type-nav span{display:inline-block;min-width:32px;color:var(--accent);font-weight:800}.type-entry{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:24px 28px 28px;margin:22px 0;box-shadow:0 5px 18px #193a540d;scroll-margin-top:20px}.card-head{display:flex;gap:12px;align-items:baseline;border-bottom:2px solid var(--wash);padding-bottom:11px;margin-bottom:14px}.type-entry .card-head h3{font-size:23px;color:var(--accent);margin:0}.type-code{font-weight:800;color:#86401f;font-size:20px;letter-spacing:.5px}.field{margin:20px 0}.field h4{font-size:13px;letter-spacing:1px;color:var(--accent);margin:0 0 7px}.field p{margin:0}.field:first-of-type{display:inline-block;margin-right:28px;vertical-align:top}.field:first-of-type p{color:var(--muted)}.worked{font-size:17px;line-height:2.05;background:#f3f7fa;border-left:5px solid #2c6594;border-radius:10px;padding:14px 17px}.practice{background:#fff9f4;border-left:5px solid #c87542;border-radius:10px;padding:14px 17px}.english{font-family:Georgia,'Songti SC',serif}.trap h4{color:var(--ink)}.question{background:#fff9f4;border:1px solid #f1d4c4;border-left:5px solid #c87542;border-radius:10px;padding:13px 17px;margin:18px 0}.qmeta{font-size:12px;font-weight:800;color:#86401f;margin-bottom:6px}.source{color:#8c3d1e;font-weight:700;font-size:13px}.source-note,figcaption{font-size:13px;color:var(--muted)}.type-link{font-size:14px;line-height:1.8;margin:10px 0}.type-link a{text-decoration:none}.type-sources{font-size:13px;color:var(--muted);border-top:1px dashed var(--line);margin-top:24px}.inline-math{display:inline-block;max-width:100%;overflow-x:auto;vertical-align:middle;padding:2px 1px}.inline-math math{font-size:1.12em}.question-list{padding-left:22px;font-size:14px;line-height:2}figure{margin:22px 0}img{display:block;width:100%;height:auto;background:white}.table-scroll{overflow:auto;margin:20px 0}table{border-collapse:collapse;min-width:100%;font-size:14px;line-height:1.7}th,td{border:1px solid var(--line);padding:10px 12px;min-width:85px;text-align:left}th{background:var(--wash)}.tools{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0}button{font:inherit;font-size:13px;color:var(--accent);background:var(--paper);border:1px solid var(--line);border-radius:4px;padding:10px 14px;cursor:pointer}button:focus-visible{outline:3px solid var(--accent)}.formula-panel h3{font-size:17px}.paper-index>summary{font-weight:600}main{max-width:1000px}@media(max-width:850px){.stats{grid-template-columns:repeat(2,1fr)}.type-nav{grid-template-columns:1fr}.hero{padding:26px 24px}}@media(max-width:620px){.type-entry{padding:20px 16px 22px}.type-entry .card-head h3{font-size:21px}.worked{font-size:16px}details.formula-panel,details.paper-index{padding:5px 12px}.tools button{min-height:44px}}@media print{.tools,.book-links{display:none}details>summary{font-weight:bold}.type-entry{break-before:auto}details:not([open])>*:not(summary){display:block!important}}
`;
const html=`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>P4 学习与题型全册 · 9702 Physics</title><style>${css}${extra}</style></head><body><a class="skip" href="#content">跳到正文</a><div class="layout"><aside><div class="brand">CAMBRIDGE · 9702</div><div class="nav-title">P4 学习全册</div><a href="index.html">核心概念与公式 ↗</a><nav aria-label="章节目录">${nav}</nav><details class="quick-nav"><summary>展开 85 个题型索引</summary><div class="type-nav">${typeNav}</div></details><details class="mobile-nav"><summary>展开章节目录</summary><nav aria-label="移动端章节目录">${nav}</nav></details><p class="nav-note">85 个题型 · 25 份试卷<br>1250 条小问索引<br>仅 Paper 4 · 离线可读</p></aside><main id="content"><div class="edition">A2 PHYSICS / 概念 · 模型 · 代表题 · 变式</div><div class="hero"><h1>P4 学习与题型全册</h1><p>从概念、识别信号到代表题和迁移练习，按题型建立可复习的物理模型。</p><p>2022–2025 语料 · Cambridge 9702 · 仅 Paper 4</p>${stats}</div><div class="book-links"><a href="index.html">核心概念与公式 ↗</a><a href="#${sections.find(s=>s.title==='全部试卷与小问索引').id}">逐卷完整索引 ↓</a></div><p class="source-note">阅读版保留原全册内容；各章另附可展开的公式速查。数学表达直接嵌入，无需联网加载。掌握状态仍为原册的“未学”，本页不自动记录进度。</p><div class="tools"><button id="expand">展开全部题源与试卷索引</button><button id="collapse">收起全部题源与试卷索引</button></div>${rendered}<footer>从最终版全册转换，原 Word 与同步题库未修改。公式速查来自配套概念册。未新增试卷，覆盖范围仍为原声明语料。</footer></main></div><script>
const indexDetails=[...document.querySelectorAll('.type-sources,.paper-index')];document.getElementById('expand').addEventListener('click',()=>indexDetails.forEach(d=>d.open=true));document.getElementById('collapse').addEventListener('click',()=>indexDetails.forEach(d=>d.open=false));
function revealHash(){const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!target)return;let p=target.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}}
window.addEventListener('hashchange',revealHash);revealHash();
const links=[...document.querySelectorAll('aside nav a')];const observer=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting)links.forEach(a=>a.hash==='#'+e.target.id?a.setAttribute('aria-current','location'):a.removeAttribute('aria-current'));},{rootMargin:'-5% 0px -75% 0px'});document.querySelectorAll('main>section').forEach(s=>observer.observe(s));
</script></body></html>`;
fs.writeFileSync(path.join(base,'handbook.html'),html);
fs.writeFileSync(path.join(__dirname,'p4_reader_math_audit.json'),JSON.stringify({conversions,failures},null,2));
const audit={sourceSha256:data.sha256,sourceBlocks:data.blocks.length,types,representatives,practice,sources,papers,indexRows,figure,inlineMath:conversions.length,failedMath:failures.length,bytes:Buffer.byteLength(html)};
fs.writeFileSync(path.join(base,'阅读版核验.json'),JSON.stringify(audit,null,2));console.log(audit);
