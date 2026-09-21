from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import math
P=Path('work/physics-audit/figures');P.mkdir(exist_ok=True)
font='/System/Library/Fonts/Supplemental/Arial.ttf'
f=ImageFont.truetype(font,22);small=ImageFont.truetype(font,18);title=ImageFont.truetype(font,25)
def sheet(index,panels):
 im=Image.new('RGB',(1400,1200),'white');d=ImageDraw.Draw(im)
 for j,(label,xlabel,ylabel,xmin,xmax,ymin,ymax,curves,notes) in enumerate(panels):
  ox=(j%2)*700;oy=(j//2)*600;left=ox+88;right=ox+650;top=oy+85;bottom=oy+475
  d.text((ox+40,oy+22),label,font=title,fill='black')
  def xy(x,y):return (left+(x-xmin)/(xmax-xmin)*(right-left),bottom-(y-ymin)/(ymax-ymin)*(bottom-top))
  yzero=max(ymin,min(ymax,0));xzero=max(xmin,min(xmax,0));xx=xy(xzero,0)[0];yy=xy(0,yzero)[1]
  d.line([(left,yy),(right,yy)],fill='black',width=2);d.line([(xx,top),(xx,bottom)],fill='black',width=2)
  d.text((right-30,yy+10),xlabel,font=small,fill='black');d.text((left-55,top-28),ylabel,font=small,fill='black')
  for k,(fn,color,name) in enumerate(curves):
   pts=[xy(xmin+(xmax-xmin)*i/500,fn(xmin+(xmax-xmin)*i/500)) for i in range(501)]
   d.line(pts,fill=color,width=4)
   d.line([(ox+50+k*205,oy+522),(ox+75+k*205,oy+522)],fill=color,width=4)
   d.text((ox+82+k*205,oy+510),name,font=small,fill='black')
  d.text((ox+48,oy+557),notes,font=small,fill='black')
 im.save(P/f'graph-{index}.png')
blue='#245481';red='#9B433C';gray='#555555'
sheet(1,[
 ('1 SHM phase relationships','t/T','scaled',0,2,-1.2,1.2,[(lambda t:math.sin(2*math.pi*t),blue,'x/x0'),(lambda t:math.cos(2*math.pi*t),red,'v/v0'),(lambda t:-math.sin(2*math.pi*t),gray,'a/a0')],'v leads x by a quarter cycle; a opposes x.'),
 ('2 SHM energy against displacement','x/x0','E/Etotal',-1,1,0,1.2,[(lambda x:x*x,blue,'potential'),(lambda x:1-x*x,red,'kinetic'),(lambda x:1,gray,'total')],'Both endpoints: K = 0. Centre: U = 0.'),
 ('3 Exponential discharge or decay','t/tau','x/x_initial',0,4,0,1.2,[(lambda t:math.exp(-t),blue,'remaining fraction')],'At t = tau, the remaining fraction is 1/e.'),
 ('4 Gravitational potential outside a sphere','r/R','phi/(GM/R)',1,5,-1.2,0,[(lambda r:-1/r,blue,'potential')],'Negative, increasing towards zero at infinity.')])
sheet(2,[
 ('5 Flux and induced emf phases','t/T','scaled',0,2,-1.2,1.2,[(lambda t:math.cos(2*math.pi*t),blue,'flux linkage'),(lambda t:math.sin(2*math.pi*t),red,'emf')],'emf = -d(flux linkage)/dt; positive convention fixed.'),
 ('6 Rectified voltages with the same peak','t/T','V/V0',0,2,-.08,1.2,[(lambda t:abs(math.sin(2*math.pi*t)),blue,'full-wave'),(lambda t:max(0,math.sin(2*math.pi*t)),red,'half-wave')],'Red overlaps blue during positive input half cycles.'),
 ('7 Power of a sine wave in a resistor','t/T','P/Ppeak',0,2,0,1.2,[(lambda t:math.sin(2*math.pi*t)**2,blue,'instantaneous'),(lambda t:.5,gray,'mean')],'Power is never negative and has twice the frequency.'),
 ('8 Binding energy per nucleon','A','BE/A',1,250,0,10,[(lambda a:8.8*(1-math.exp(-a/12)) if a<=56 else 8.8*(1-math.exp(-56/12))-.006*(a-56),blue,'schematic only')],'Peak near A = 56; right branch decreases slowly.')])
print(P)
