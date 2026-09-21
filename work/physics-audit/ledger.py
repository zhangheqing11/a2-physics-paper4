from pathlib import Path
import re,json,csv,collections
root=Path.cwd();p=root/'work/physics-audit';o=root/'output/physics'
inventory=json.loads((p/'inventory.json').read_text()); inv={r['id']:r for r in inventory}
types={
'C01':'弧度与弧长','C02':'角速度 周期与转角','C03':'线速度与实际半径','C04':'向心加速度计算','C05':'速度 加速度与合力方向','C06':'同一刚体不同半径比较','C07':'链轮传动与约束改变','C08':'分解真实作用力','C09':'近似与数量级判断','C10':'卫星周期 轨道半径与图像','C11':'同步轨道与地面自转','C12':'库仑力提供向心力','C13':'磁力提供向心力','C14':'磁场中的周期与半径变化','C15':'圆周运动投影与简谐运动','C16':'转动与电磁感应综合',
'P01':'变量与控制','P02':'可执行装置与测量','P03':'直线化与参数提取','P04':'实验细节与情境安全','P05':'数据变换与不确定度','P06':'描点与误差棒','P07':'最佳线与最差可接受线','P08':'斜率与不确定度','P09':'截距与不确定度','P10':'常量还原与单位缩放','P11':'参数不确定度','P12':'预测与反解'}
# Each entry was selected against the actual question and its matching MS.
maps={
('s22','41'):'2(a)(i):C05 2(a)(ii):C05 2(c):C13',
('s22','42'):'2(b)(i):C05 2(b)(ii):C12 2(b)(iii):C12',
('w22','41'):'1(b):C10 1(c)(i):C10 1(c)(ii):C11',
('w22','42'):'1(b)(ii):C05 1(c)(i):C04 1(c)(ii):C08',
('s23','41'):'2(a):C08 2(b)(i):C03 2(b)(ii):C08 2(b)(iii):C08 2(c)(i):C08 2(c)(ii):C02',
('s23','42'):'1(b):C10 1(c):C10 1(d)(i):C02 1(d)(ii):C11 6(b):C16',
('w23','41'):'6(b)(i):C05 6(b)(ii):C13 6(b)(iii):C05 6(b)(iv):C13 6(c):C13',
('w23','42'):'1(a):C01 1(b):C02 1(c)(i):C02 1(c)(ii):C01 1(c)(iii):C04 1(d):C09',
('m24','42'):'5(a):C05 5(b)(i):C14 5(b)(ii):C14 5(b)(iii):C14',
('s24','42'):'1(a):C01 1(b)(i):C05 1(b)(ii):C05 1(c)(i):C03 1(c)(ii):C04 1(d):C06',
('w24','41'):'1(b)(i):C05 1(b)(ii):C10 1(b)(iii):C10',
('w24','42'):'1(a)(i):C03 1(a)(ii):C04 1(b)(ii):C02 1(b)(iii):C16 1(b)(iv):C16 1(b)(v):C16',
('s25','41'):'1(c)(i):C11 1(c)(ii):C11 2(b)(i):C12 2(b)(ii):C12 2(c)(i):C12 2(c)(ii):C12 2(d)(i):C12 2(d)(ii):C12',
('s25','42'):'1(a):C01 1(b)(i):C03 1(b)(ii):C02 1(b)(iii):C01 1(b)(iv):C01 1(c):C07',
('w25','41'):'1(a):C05 1(b)(i):C03 1(b)(ii):C04 1(c)(i):C15 1(c)(ii):C02 1(c)(iii):C15 1(c)(iv):C15 1(d)(i):C15 1(d)(ii):C02 1(d)(iii):C15 1(e):C15',
('w25','42'):'1(a)(i):C03 1(a)(ii):C03 1(b)(i):C08 1(b)(ii):C05 1(b)(iii):C08'}
# 43 occurrences are retained, with the corresponding 41 occurrence noted for later visual duplicate audit.
for season,component in list(maps):
 if component=='41':maps[(season,'43')]=maps[(season,'41')]
def ms_rows(season,comp):
 text=(p/f'9702_{season}_ms_{comp}.txt').read_text(); rows={};cur=None;page=None
 for line in text.splitlines():
  pg=re.match(r'=== MERGED PAGE (\d+)',line)
  if pg:page=int(pg[1]);continue
  m=re.match(r'^\s*(\d+\([a-z]\)(?:\([ivx]+\))?)\s+(.*)',line)
  if m:
   cur=m[1];rows.setdefault(cur,{'page':page,'lines':[],'marks':0})
  if cur and line.strip() and not re.search(r'©|PUBLISHED|Mark Scheme|^\s*Question\s+Answer',line):
   rows[cur]['lines'].append(line.strip())
   mark=re.search(r'\s([BCMA])(\d+)\s*$',line)
   if mark:rows[cur]['marks']+=int(mark[2])
 return rows
records=[]
for (season,comp),mapping in maps.items():
 mr=ms_rows(season,comp)
 for item in mapping.split():
  q,tag=item.split(':'); assert q in mr,(season,comp,q)
  qp=inv[f'9702_{season}_qp_{comp}'];ms=inv[f'9702_{season}_ms_{comp}'];r=mr[q]
  records.append({'paper':f'9702_{season}_{comp}','question':q,'type':tag,'name':types[tag],'marks':r['marks'],'qp_start':qp['start'],'qp_end':qp['end'],'ms_page':r['page'],'status':'评分依据已定位；跨版本重复待视觉复核' if comp=='43' else '原题与评分依据已核对','duplicate_group':f'9702_{season}_41:{q}' if comp=='43' else '', 'mastery':'未学'})
for season,comp in [('s22','52'),('w23','51'),('s24','52')]:
 qp=inv[f'9702_{season}_qp_{comp}'];mr=ms_rows(season,comp)
 q1page={'s22':87,'w23':476,'s24':245}[season]
 for q,tag,marks,pg in [('1 变量','P01',2,q1page),('1 测量','P02',4,q1page),('1 分析','P03',3,q1page+(1 if season!='w23' else 0)),('1 细节','P04',6,q1page+(2 if season!='w23' else 1))]:
  records.append(dict(paper=f'9702_{season}_{comp}',question=q,type=tag,name=types[tag],marks=marks,qp_start=qp['start'],qp_end=qp['end'],ms_page=pg,status='样本评分维度已核对',duplicate_group='',mastery='未学'))
 mapping=[('2(a)','P03',1),('2(b)','P05',2),('2(c)(i)','P06',2),('2(c)(ii)','P07',2),('2(c)(iii)','P08',2),('2(c)(iv)','P09',2)]
 mapping+= [('2(d)(i)','P10',2),('2(d)(ii)','P11',1)] if season=='w23' else [('2(d)','P10',3)]
 mapping+=[('2(e)','P12',1)]
 for q,tag,marks in mapping:
  assert q in mr
  records.append(dict(paper=f'9702_{season}_{comp}',question=q,type=tag,name=types[tag],marks=marks,qp_start=qp['start'],qp_end=qp['end'],ms_page=mr[q]['page'],status='原题与评分依据已核对',duplicate_group='',mastery='未学'))
for paper in ['9702_s22_52','9702_w23_51','9702_s24_52']:
 assert sum(r['marks'] for r in records if r['paper']==paper)==30
with (o/'首批题型索引与掌握记录.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
(p/'ledger.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
(p/'types.json').write_text(json.dumps(types,ensure_ascii=False,indent=2))
with (o/'个人题型掌握表.csv').open('w',encoding='utf-8-sig',newline='') as f:
 fields=['考法编号','考法名称','当前状态','关联记录数','首次学习日期','典型题独立作答证据','变式与解释证据','错误类别','下一步补救','延迟复测日期','延迟混合测试结果']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for code,name in types.items():
  row=dict.fromkeys(fields,'');row.update({'考法编号':code,'考法名称':name,'当前状态':'未学','关联记录数':sum(r['type']==code for r in records)})
  w.writerow(row)
print('records',len(records),'P4',sum(r['type'][0]=='C' for r in records),'P5',sum(r['type'][0]=='P' for r in records))
print('unpaired',[r['id'] for r in inventory if r['kind']=='qp' and r['id'].replace('_qp_','_ms_') not in inv])
print('zero marks',[r for r in records if r['marks']==0])
