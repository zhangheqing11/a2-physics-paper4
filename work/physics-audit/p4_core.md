# CIE 9702 P4 核心概念与公式
学习与刷题查漏参考

本册按 Cambridge 9702 2025至2027年考纲第12至25章整理，仅覆盖 Paper 4 的 A2 理论，并补充必要的 AS 接口知识。它与《P4 学习与题型全册》配套：本册查“是什么、为什么、何时能用”，题型全册查“题目如何识别和求解”。

尚未学过 A2 时，每章先读概念，再读公式的条件，最后到题型全册看代表题并独立做变式。能背出公式不等于掌握；至少应能说明每个量、为什么能用，以及条件改变后哪里需要重建模型。

本册的“核心”指考纲明确要求的概念和关系；“推导”指从核心关系得到的常用结论；“接口”指所需 AS 或先修知识。公式标签不代表考试是否提供该式，考试中仍应阅读该卷数据表。英文定义是可用于学习和作答的物理表述，不是逐题评分标准的替代品。

## 阅读顺序与导航
先读通用工具，再按圆周与引力、温度与气体与热力学、振动、电场与电容、磁场与感应与交流、量子与核物理、医学与天体的顺序学习。各章标题采用官方编号，在 Word 导航窗格中可直接跳转。

各章先给中英概念及直观解释，再列公式、符号单位和条件，最后给图像与易错点。公式中的同一字母在不同章可能表示不同量；以下标和本章符号表为准。

## A2 教学顺序与公式阅读法
本页参考《A-Level Physics Lecture Notes》的章节推进：先用圆周运动建立角量和向心模型，再进入引力场；随后学习温度、理想气体和热力学，把“微观粒子运动”连接到宏观状态量；再学习振动、电场、电容、磁场与电磁感应、交流；最后进入量子、核物理、医学物理和天体物理。这个顺序的主线是“运动与力 → 场与能量 → 粒子模型 → 周期与传输 → 微观与宇宙尺度”。

每条公式按四步阅读：先说它描述的现象，再写最基础的守恒关系或定义，接着说明代入了哪条定义得到当前形式，最后检查单位、方向和适用条件。例如圆轨道由引力提供向心力，先写 `GMm/r² = mv²/r`，再得到 `v = √(GM/r)`；电容储能由 `W = ∫V dQ` 出发，线性电容使用 `V = Q/C` 后得到 `W = QV/2`；放电则由回路方程 `IR + Q/C = 0` 与 `I = -dQ/dt` 得到指数式。刷题时先判断题目给的是哪种现象，再回到对应的基础式，避免把结论公式当作无条件公式。

本页的推导式只保留考试和题型识别中有用的中间链条；教材中标有星号的电子学、通信和拓展内容不纳入 P4 主线，但可作为延伸阅读。

# 通用工具与 AS 接口
## 基本量和关系
Vector quantities have magnitude and direction. 矢量既有大小又有方向；相加时必须考虑方向或分量。Scalar quantities have magnitude only. 标量没有空间方向，但按参考零点定义的势和能量仍可为负。

Velocity is the rate of change of displacement. 速度是位移的变化率。Acceleration is the rate of change of velocity. 加速度衡量速度矢量变化的快慢，因此速率不变也可能有加速度。

Work is the energy transferred by a force acting through a displacement. 功是力通过位移传递的能量；只取力沿位移的分量。Power is energy transferred per unit time. 功率是能量传递率。Momentum is mass multiplied by velocity. 动量是质量与速度的乘积，是矢量。

符号：s displacement 位移(m)；u initial velocity 初速度、v velocity 速度(m s⁻¹)；a acceleration 加速度(m s⁻²)；t time 时间(s)；m mass 质量(kg)；F force 力(N)；p momentum 动量(kg m s⁻¹)；W work 功、E energy 能量(J)；P power 功率(W)。

@接口|ΣF = ma ; p = mv ; F = \frac{Δp}{Δt}|合力决定加速度；后一式给平均合力，瞬时关系取变化率。惯性质量不变的经典力学模型。
@接口|v = u + at ; s = ut + \frac{1}{2}at^{2}|仅适用于加速度恒定的同一方向分量，不能直接用于方向不断改变的圆周速度。
@接口|E_{k} = \frac{1}{2}mv^{2} ; W = Fs cos θ ; P = \frac{W}{t}|θ为恒力与位移夹角；P式给平均功率。速率接近光速时不能使用经典动能。
@接口|ΔE_{p} = mgΔh ; P = Fv|前式要求g近似恒定；后式要求取力沿速度的分量，适用于瞬时机械功率。
@接口|Q = It ; V = \frac{W}{Q} ; P = VI ; V = IR|电荷Q(C)，电流I(A)，电势差V(V)，电阻R(Ω)；Q=It要求电流恒定。V=W/Q表示每库仑转移的能量。
@接口|I = nAqv_{d} ; v_{wave} = fλ|n载流子数密度(m⁻³)，A截面积(m²)，q电荷量大小(C)，v_d漂移速率(m s⁻¹)；波速=频率(Hz)×波长(m)。

## 单位和图像
代入前统一 SI。milli 毫为10⁻³，micro 微为10⁻⁶，nano 纳为10⁻⁹，pico 皮为10⁻¹²；kilo 千为10³，mega 兆为10⁶。1 cm²=10⁻⁴ m²，1 cm³=10⁻⁶ m³。指数与对数的自变量必须无量纲，角位移代入正弦和圆周公式时用弧度。

斜率单位等于纵轴单位除以横轴单位；面积单位等于二者相乘。切线斜率给瞬时变化率。先确认横纵轴、倍率和零点，再判断斜率、截距与面积的物理意义。

常用常量取值：c=3.00×10⁸ m s⁻¹；e=1.60×10⁻¹⁹ C；h=6.63×10⁻³⁴ J s；G=6.67×10⁻¹¹ N m² kg⁻²；ε₀=8.85×10⁻¹² F m⁻¹；k=1.38×10⁻²³ J K⁻¹；N_A=6.02×10²³ mol⁻¹；R=8.31 J mol⁻¹ K⁻¹；σ=5.67×10⁻⁸ W m⁻² K⁻⁴；m_e=9.11×10⁻³¹ kg；u=1.66×10⁻²⁷ kg。计算优先采用题给数值。

# 12 圆周运动
对应考纲12.1至12.2
## 核心概念
A radian is the angle subtended at the centre of a circle by an arc equal in length to its radius. 一弧度是弧长等于半径时对应的圆心角；它以“弧长相当于多少个半径”衡量角度。

Angular speed is the rate of change of angular displacement. 角速率是角位移的变化率。Period is the time taken for one complete cycle. 周期是完成一圈所需时间。Frequency is the number of complete cycles per unit time. 频率是每单位时间完成的圈数。

Centripetal acceleration is directed towards the centre of the circular path. 向心加速度指向圆心。匀速圆周运动的速度方向不断变化，因此有向心加速度；恒定大小、始终垂直于速度的合力不改变速率，只改变运动方向。

“向心力”是径向合力的名称，不是额外的一种力。拉力、重力、摩擦力或电磁力可以提供这份合力。受力图中画真实相互作用，再把径向分量相加。

## 公式与符号
θ angular displacement 角位移(rad)；s arc length 弧长(m)；r radius 半径(m)；ω angular speed 角速率(rad s⁻¹)；T period 周期(s)；f frequency 频率(Hz)；v tangential speed 切向速率(m s⁻¹)；m质量(kg)，a加速度(m s⁻²)，F力(N)。
@核心|θ = \frac{s}{r} ; ω = \frac{Δθ}{Δt} ; ω = \frac{2π}{T} = 2πf|中间式为平均角速率；匀速时也是任意时刻角速率。一周为2π rad，f=1/T。
@核心|v = rω ; a = \frac{v^{2}}{r} = rω^{2}|同一角速率下半径越大，线速率越大。比较加速度时须先说清固定的是v还是ω。
@核心|ΣF_{r} = \frac{mv^{2}}{r} = mrω^{2}|以指向圆心为径向正方向；ΣF_r是径向合力，不一定等于某一单独的力。
@推导|F_{r} = \frac{4π^{2}mr}{T^{2}}|由ω=2π/T代入，适用于匀速圆周运动。

## 条件和易错点
竖直圆周中重力的径向分量随位置变化，速率也可能变化，不能自动视作匀速。顶部若圆心在下方，重力通常与拉力共同指向圆心；底部通常是拉力减重力。绳只能拉，接触面支持力不能变成“吸引力”，临界失去约束时相应力为零。

共轴刚体各点角速率相同，线速率未必相同；无滑动皮带接触轮缘的线速率相同，角速率未必相同。圆周半径量到运动物体的中心，而不是系统外缘。

# 13 引力场
对应考纲13.1至13.4
## 核心概念
A gravitational field is a region in which a mass experiences a gravitational force. 引力场是质量会受到引力的区域。Gravitational field strength is gravitational force per unit mass. 引力场强是单位测试质量受到的引力；直观上是“每千克在这里受多大力”。场线指向源质量，越密表示场越强。

Newton’s law of gravitation states that the force between two point masses is proportional to the product of their masses and inversely proportional to the square of their separation. 两点质量间的引力与质量乘积成正比，与间距平方成反比，方向沿连线且相互吸引。

Gravitational potential is the work done per unit mass in bringing a small test mass from infinity to the point. 引力势是从无穷远把单位小测试质量缓慢移到该点时外力所做的功，取无穷远为零。引力势为负，表示该处的能量比无穷远更低；它是标量，不是场强。

Geostationary means remaining above the same point on the Earth’s surface. 地球静止卫星相对地面同一点不动：圆轨道位于赤道平面，自西向东，与地球自转同向，周期按考纲取24小时。仅有“周期24小时”还不够。

## 公式与符号
M source mass 源质量、m test mass 测试质量(kg)；r centre separation 中心间距(m)；G引力常量；g field strength 场强(N kg⁻¹)；φ potential 引力势(J kg⁻¹)；U potential energy 势能(J)；R星体半径(m)；h离表面高度(m)。
@核心|F = \frac{GMm}{r^{2}} ; g = \frac{F}{m} = \frac{GM}{r^{2}}|给出大小。点质量适用；均匀球体外部可等效为球心点质量，r=R+h，不是h。
@核心|φ = -\frac{GM}{r} ; U = mφ = -\frac{GMm}{r}|无穷远取零；U是两质量系统的引力势能。向外移动时势能增加，虽仍可能为负。
@推导|v_{orbit} = \sqrt{\frac{GM}{r}} ; T^{2} = \frac{4π^{2}r^{3}}{GM}|圆轨道且引力独自提供向心力。轨道半径增大，速率减小而周期增大。
@推导|E_{k} = \frac{GMm}{2r} ; E_{total} = -\frac{GMm}{2r}|只适用于上述圆轨道；总能量为动能加引力势能，不是势能本身。
@推导|ΔU = GMm(\frac{1}{r_{1}}-\frac{1}{r_{2}}) ; v_{escape} = \sqrt{\frac{2GM}{r}}|逃逸速率假设出发后无推进、无阻力，刚好到无穷远时速率为零。不是圆轨道速率。
@推导|g_{r} = -\frac{dφ}{dr} ; E_{k1}+U_{1}=E_{k2}+U_{2}|r向外为正，所以g_r为负。能量式要求没有其他非保守功；多源时势代数叠加、场矢量叠加。

## 图像和易错点
g的大小按1/r²下降；φ为负且随r增大趋于零。近地面高度变化远小于R时g近似恒定，才可用mgΔh。g=0并不意味着φ=0；重力失重感并不等于没有引力，轨道中物体与舱体都在自由落体。

# 14 温度与热量
对应考纲14.1至14.3
## 核心概念
Thermal equilibrium means equal temperature and no net transfer of thermal energy between bodies in thermal contact. 热平衡是温度相同，热接触时无净热传递。热能自发从高温处流向低温处；温度相同不代表内能相同。

A thermometric property is a measurable physical property that varies with temperature. 测温性质是随温度改变的可测物理性质，如液体密度或体积、定压气体体积、金属电阻、热电偶电动势。用某物质刻度前需要校准；不同性质不一定随温度线性变化。

Thermodynamic temperature does not depend on a property of a particular substance. 热力学温标不依赖某一具体物质的测温性质。Absolute zero is the lowest possible thermodynamic temperature, zero kelvin. 绝对零度为0 K；不能把它表述为摄氏零度，也不宜泛称一切微观运动完全停止。

Specific heat capacity is the energy required per unit mass per unit temperature rise without a change of state. 比热容是物质不发生相变时，单位质量升高单位温度所需的能量；它衡量“升温难不难”。

Specific latent heat is the energy required per unit mass to change state without a change in temperature. 比潜热是在温度不变时单位质量发生相变所需能量。Fusion是熔化，vaporisation是汽化；逆过程释放对应能量。相变期间供热主要改变粒子间势能，不提高平均随机动能。

## 公式与符号
T thermodynamic temperature 热力学温度(K)；θ Celsius temperature 摄氏温度(°C)；Q thermal energy 热量(J)；m mass 质量(kg)；c specific heat capacity 比热容(J kg⁻¹ K⁻¹)；L specific latent heat 比潜热(J kg⁻¹)；C heat capacity 热容量(J K⁻¹)，勿与电容混淆。
@核心|\frac{T}{K} = \frac{θ}{°C}+273.15 ; ΔT = Δθ|后式指温差的数值：升高1 K与升高1°C相同。温度的比值和气体方程必须用K。
@核心|Q = mcΔT ; Q = mL|第一式用于无相变升降温且c近似恒定；第二式用于相变。混合过程分阶段相加。
@推导|C = mc ; Q_{in} = Pt|P heater power 加热功率(W)，t时间(s)；恒功率且全部计入输入能量。容器吸热、散热都要另计。
@推导|Q_{released} = Q_{absorbed} ; θ = 100\frac{X-X_{0}}{X_{100}-X_{0}}|热平衡能量式须包含各物体及损失。后式只适用于按0°C和100°C固定点线性校准的测温性质X。

## 图像和易错点
恒功率、无损失加热时，温度—时间图斜率为P/(mc)，斜率大代表总热容量小。相变平台表示温度不变但仍吸能，不能说内能不变。保温并不能保证实际完全无热损失；题目若给散热功率，应先从输入功率扣除。

# 15 理想气体
对应考纲15.1至15.3
## 核心概念
One mole contains a number of specified particles equal to the Avogadro constant. 一摩尔含阿伏伽德罗常量所对应数量的指定粒子；先明确数的是原子、分子还是其他粒子。

For a fixed amount of an ideal gas, pressure times volume is proportional to thermodynamic temperature. 固定数量的理想气体满足pV与绝对温度成正比。压强必须是绝对压强，摄氏温度不能直接代入。

动理论模型假设：分子数量很大并持续随机运动；分子可视作质点，体积相对容器可忽略；除碰撞外相互作用可忽略；碰撞完全弹性且碰撞时间相对两次碰撞间隔可忽略；运动方向没有优先性。稀薄、高温而远离液化条件的气体更接近该模型。

Gas pressure is caused by momentum transfer when molecules collide with the walls. 分子碰壁时动量改变，墙对分子施力，分子对墙施反作用力；许多碰撞的平均力除以面积形成压强。弹性碰撞不等于没有动量变化。

Root mean square speed is the square root of the mean of the squared molecular speeds. 均方根速率是先平方、再平均、再开根，不等于平均速率，也不等于平均速度。随机运动的平均速度可为零，但均方根速率不为零。

## 公式与符号
p pressure 压强(Pa)；V volume 体积(m³)；n amount of substance 物质的量(mol)；N number of molecules 分子数；N_A Avogadro constant(mol⁻¹)；R摩尔气体常量；k Boltzmann constant(J K⁻¹)；m单分子质量(kg)；M molar mass 摩尔质量(kg mol⁻¹)；ρ密度(kg m⁻³)；c分子速率(m s⁻¹)，此处不是光速。
@核心|N=nN_{A} ; k=\frac{R}{N_{A}} ; pV=nRT=NkT|n按摩尔计，N按粒子个数计，两套计数不可混用。m=M/N_A。
@推导|\frac{p_{1}V_{1}}{T_{1}}=\frac{p_{2}V_{2}}{T_{2}} ; n=\frac{m_{gas}}{M}|前式要求气体数量不变；漏气或分装时应分别追踪N或n，不能自动约掉。
@核心|pV=\frac{1}{3}Nm\langle c^{2}\rangle ; c_{rms}=\sqrt{\langle c^{2}\rangle}|均方速率为所有分子速率平方的平均值。1/3来自三维各方向均等。
@核心|\langle E_{k}\rangle=\frac{1}{2}m\langle c^{2}\rangle=\frac{3}{2}kT|单分子的平均平动动能只由T决定；同温不同气体平均平动动能相同，速率一般不同。
@推导|c_{rms}=\sqrt{\frac{3kT}{m}}=\sqrt{\frac{3RT}{M}} ; p=\frac{1}{3}ρc_{rms}^{2}|速率正比于温度平方根、反比于分子质量平方根。气体质量密度ρ=Nm/V。

## 必会推导
边长l的立方体内，一个分子垂直墙的速度分量为c_x。弹性碰壁时动量变化大小2mc_x，两次撞同一墙间隔2l/c_x，因此平均力为mc_x²/l。除以墙面积l²并对N个分子求和，得到pV=Nm〈c_x²〉。随机各向同性给出〈c_x²〉=〈c²〉/3，形成核心式。再与pV=NkT比较，得到平均平动动能3kT/2。

# 16 热力学
对应考纲16.1至16.2
## 核心概念
Internal energy is the sum of the microscopic kinetic and potential energies associated with the particles of a system. 内能是系统粒子微观随机运动动能与相互作用势能之和，由系统状态决定。整体平移的动能不是内能；热量是传递中的能量，不是系统“储存的热”。

The increase in internal energy equals the energy supplied by heating plus the work done on the system. 内能增加等于流入系统的热量加外界对系统的功，这就是采用“对系统做功为正”的热力学第一定律。

膨胀时气体向外推动活塞，对外做正功，外界对气体做负功；压缩相反。温度升高通常对应内能增加；相变时温度可以不变而内能变化。

## 公式与符号
U internal energy 内能(J)；Q heating energy 流入的热能(J)；W_on work done on gas 对气体做功(J)；W_by work done by gas 气体对外做功(J)；p external pressure 外压(Pa)；ΔV volume increase 体积增加(m³)。
@核心|ΔU=Q+W_{on}=Q-W_{by}|吸热Q正、放热Q负；压缩功W_on正、膨胀功W_on负。始终保持同一约定。
@核心|W_{by}=pΔV ; W_{on}=-pΔV|外压恒定。准静态过程可用气体p-V图；变压时功取有向曲线下的面积。
@推导|U=\frac{3}{2}NkT=\frac{3}{2}nRT ; ΔU=\frac{3}{2}nRΔT|用于仅计平动动能的理想单原子气体模型，且第二式n不变。不能当作所有多原子气体的通用内能公式。

## 四种过程
Isochoric 等容：ΔV=0，所以W=0，ΔU=Q。Isothermal 等温：理想气体内能不变，所以ΔU=0，吸热等于对外做功；不代表没有热交换。

Adiabatic 绝热：Q=0，所以ΔU=W_on；绝热膨胀通常降温。Cyclic 循环：末态回到初态，所以一周ΔU=0；各段内能、热量和功并不分别为零。顺时针p-V循环的气体净对外功为正，大小等于封闭面积。

## 易错点
用系统边界决定能量流入流出，不能凭“加热了”直接认定温度必定上升。若题目不给单原子或相应能量模型，优先用题给热容量或第一定律，而非擅自套3nRT/2。p-V图面积是功；不是p-t或V-t图面积。

# 17 振动
对应考纲17.1至17.3
## 核心概念
Simple harmonic motion is motion in which acceleration is proportional to displacement from a fixed equilibrium position and directed towards that position. 简谐运动的加速度大小与相对固定平衡位置的位移大小成正比，方向与位移相反。判据是a与x的关系，不是仅仅“来回运动”。

Amplitude is the maximum magnitude of displacement from equilibrium. 振幅是离平衡位置的最大位移大小。Natural frequency is the frequency at which a system oscillates freely. 自然频率是系统自由振动时的频率。Phase difference describes the difference in stage between periodic motions. 相位差表示周期状态相差多少。

Damping is the reduction of oscillation energy due to resistive forces. 阻尼使机械能耗散。轻阻尼仍振荡且振幅逐渐减小；临界阻尼最快地不振荡返回平衡；重阻尼也不振荡，但返回更慢。

Resonance is the large response when a system is driven at its natural frequency. 按本考纲模型，驱动频率等于自然频率时响应振幅最大，称为共振。阻尼增大时峰值降低、峰变宽；实际阻尼系统峰位可有偏移，不能把该近似推广到所有精确模型。

## 公式与符号
x displacement 位移(m)；x₀ amplitude 振幅(m)；ω angular frequency 角频率(rad s⁻¹)；T周期(s)；f频率(Hz)；v速度(m s⁻¹)，a加速度(m s⁻²)；m质量(kg)；E总能量、K动能、U恢复势能(J)；φ初相位(rad)。
@核心|a=-ω^{2}x ; ω=2πf=\frac{2π}{T}|负号为恢复方向；a-x图是过原点的负斜率直线，斜率=-ω²。
@核心|x=x_{0}sin(ωt+φ) ; v=ωx_{0}cos(ωt+φ)|初相位由起始位置和速度决定；不能看到SHM就默认t=0时x=0。
@核心|v=±ω\sqrt{x_{0}^{2}-x^{2}} ; v_{max}=ωx_{0} ; a_{max}=ω^{2}x_{0}|同一位移可能有两个速度方向；最大加速度大小发生于两端。
@核心|E=\frac{1}{2}mω^{2}x_{0}^{2}|无阻尼时总振动能守恒；振幅加倍，能量变四倍。
@推导|U=\frac{1}{2}mω^{2}x^{2} ; K=\frac{1}{2}mω^{2}(x_{0}^{2}-x^{2})|U以平衡位置为零；竖直弹簧需把弹簧势能与重力势能共同计入恢复势能。
@推导|Δφ=\frac{2πΔt}{T} ; T=2π\sqrt{\frac{m}{k_{s}}}|相位差用同频运动的时间错位。弹簧周期要求线性胡克定律，k_s弹簧劲度系数(N m⁻¹)。
@推导|T=2π\sqrt{\frac{l}{g}}|单摆长度l(m)，g重力加速度；仅小角度、轻绳、可视作质点且阻尼可忽略，不是任意摆幅通式。

## 图像和易错点
位移到端点时v=0而加速度最大；过平衡位置时a=0而速率最大。v比x相位超前π/2，a与x反相。势能—位移图向上抛物线，动能图向下抛物线；总能量水平线。动能与势能一周期内各出现两次最大值。

共振图横轴为驱动频率，纵轴为稳态振幅；它不是振幅随时间的阻尼图。强迫振动的稳态频率由驱动源决定，不应写成永远等于系统自然频率。

# 18 电场
对应考纲18.1至18.5
## 核心概念
Electric field strength is force per unit positive charge. 电场强度是单位正测试电荷受到的力；方向按正电荷受力定义，负电荷受力相反。场线从正电荷指向负电荷或无穷远，不能交叉，密处场较强。

Coulomb’s law gives the inverse square force between point charges. 真空中两点电荷的作用力与电荷量乘积成正比，与间距平方成反比；同号相斥、异号相吸。球形导体外部可把电荷等效于球心点电荷。

Electric potential is the work done per unit positive charge in bringing a small test charge from infinity to the point. 电势是从无穷远将单位小正测试电荷缓慢移到该点时外力做的功；它表示每库仑正电荷的能量位置，可以正或负。电势差则比较两点。

等势面上移动电荷不改变电势能，电场垂直等势面。静电平衡导体内部E=0，整个导体等势；电势不一定为零。多个电荷的势按正负代数相加，场必须矢量相加。

## 公式与符号
E field strength 场强(N C⁻¹或V m⁻¹)；Q source charge 源电荷、q test charge 测试电荷(C)；r间距(m)；ε₀真空介电常量(F m⁻¹)；V potential 电势(V=J C⁻¹)；U potential energy 势能(J)；d板距(m)；m粒子质量(kg)。
@核心|F=qE ; F_{magnitude}=\frac{|Qq|}{4πε_{0}r^{2}}|第一式须按方向理解；后一式为力的大小，方向另由电荷正负与几何判断。
@核心|E_{r}=\frac{Q}{4πε_{0}r^{2}} ; V=\frac{Q}{4πε_{0}r}|径向向外为正；Q为带符号源电荷。势以无穷远为零，单源点电荷或球外适用。
@核心|U=qV=\frac{Qq}{4πε_{0}r} ; E_{x}=-\frac{dV}{dx}|电势能包含被放入的电荷q；E沿电势下降最快方向。V-x图负斜率对应正向电场。
@核心|E=\frac{|ΔV|}{d} ; a=\frac{qE}{m}|平行板内部近似匀强并忽略边缘效应；第二式为沿选定方向的分量。
@推导|ΔK=-qΔV ; W_{external}=qΔV|第一式要求只有电力做功；第二式是缓慢移动、动能不变时外力做功。负电荷向高电势运动时动能可增加。
@推导|t=\frac{l}{u} ; y=\frac{1}{2}\frac{qE}{m}(\frac{l}{u})^{2}|平行板粒子偏转：初速度u平行板面，板长l，初横向速度零、忽略其他力，y为有符号偏移。

## 易错点
E=0不推出V=0，V=0也不推出E=0。电场能改变粒子动能；纯磁场力则始终与瞬时速度垂直、不做功。比较引力时记住：质量总为正且相吸，电荷可正负且作用可斥可吸。

# 19 电容
对应考纲19.1至19.3
## 核心概念
Capacitance is charge stored per unit potential difference. 电容是储存的电荷量与电势差之比。平行板电容的Q指一块板上电荷的大小，两板分别为+Q与−Q，不能用两板代数和零作为Q。孤立导体的V相对于无穷远。

电容由导体形状、尺寸与介质决定；理想线性电容器上，增加Q会使V同比增加，不会自动使C增加。电容能量存储在电场中。

The time constant is the time for charge, voltage or current magnitude to fall to 1/e of its initial value during discharge. 时间常量是放电时电荷、电压或电流大小降到初值1/e所需时间；每隔同样时间衰减相同比例，而不是减去相同量。

## 公式与符号
C capacitance 电容(F)；Q charge 电荷(C)；V potential difference 电势差(V)；W stored energy 储能(J)；R resistance 电阻(Ω)；τ time constant 时间常量(s)；t时间(s)；下标0为该放电段的起始值。
@核心|C=\frac{Q}{V} ; C_{parallel}=C_{1}+C_{2}+…|并联各支路电势差相同，各电容板上电荷大小相加得到对应总电荷。
@核心|\frac{1}{C_{series}}=\frac{1}{C_{1}}+\frac{1}{C_{2}}+…|串联总电势差相加；常用等电荷条件来自初始中性且与外界绝缘的中间节点。
@核心|W=\frac{1}{2}QV=\frac{1}{2}CV^{2}=\frac{Q^{2}}{2C}|准静态充电从0到末态，V-Q图下方面积给能量。最后一个等式由Q=CV推导。
@核心|τ=RC ; Q=Q_{0}e^{-t/(RC)} ; V=V_{0}e^{-t/(RC)}|通过恒定电阻R放电，C也恒定，不存在外部继续充电源。
@核心|I_{mag}=\frac{V_{0}}{R}e^{-t/(RC)}|给放电电流大小。若把流入正板为正，电流为dQ/dt，放电时带负号。
@推导|ln(\frac{V}{V_{0}})=-\frac{t}{RC} ; t_{half}=RC ln2|对数图斜率=-1/(RC)；电荷、电压、电流大小有相同半衰时间。
@推导|W=W_{0}e^{-2t/(RC)} ; t_{half,energy}=\frac{RC ln2}{2}|储能正比于V²，因此能量衰减更快，不能用Q的半衰时间代替。
@推导|C_{sphere}=4πε_{0}r ; C_{plates}=\frac{εA}{d}|球式由球面电势推导；板式为常用扩展关系，要求匀强场、忽略边缘效应，ε介质介电常量，A正对面积。

## 电路约束和图像
并联推导：总Q=各C乘共同V的和。串联推导：总V=共同Q乘各1/C的和。变式题先画清节点，不要看到元件“排成一排”就认定串联。

V-Q图斜率1/C，Q-V图斜率C；只有V-Q图下方面积直接表示逐步充电功。重连时追踪同一绝缘节点的带符号电荷守恒；电场能通常部分转为热、辐射等，不可再强行设电容储能守恒。电池保持连接时V固定，移去电池后孤立系统才常有Q固定。

# 20 磁场与电磁感应
对应考纲20.1至20.5
## 磁力的核心概念
Magnetic fields are produced by moving charges and permanent magnets. 磁场由运动电荷或永磁体产生。磁场线构成闭合曲线，磁体外由北极指向南极；点表示出纸面，叉表示入纸面。

Magnetic flux density is force per unit current per unit length on a straight conductor perpendicular to the field. 磁通密度是垂直置于磁场中的直导线，每单位电流、单位有效长度受到的力；单位tesla。Fleming左手定则按传统电流方向判断力；负电荷运动对应的传统电流方向与速度相反。

直导线磁场为同心圆，用右手握线规则判断；圆线圈轴上场线穿过圈面；长螺线管内部近似均匀、外部较弱，右手手指顺电流、拇指指向内部场及北端。铁磁芯可显著增强场。同向平行电流相吸，反向相斥，是各自磁场对另一导线中电流作用的结果。

Hall voltage is the transverse potential difference caused by charge separation in a current-carrying material placed in a magnetic field. 霍尔电压是载流材料在磁场中因载流子横向分离而产生的电势差。电荷积累直到横向电场力与磁力平衡。保持电流和几何固定后，霍尔电压可用于测量B；调探头方向寻找最大读数。

## 磁力公式与符号
B magnetic flux density 磁通密度(T)；I传统电流(A)；l场内导线长(m)；q电荷量(C)；v速率(m s⁻¹)；θ电流或速度与B夹角；r轨道半径(m)；n carrier density 载流子数密度(m⁻³)；t霍尔片沿B方向的厚度(m)；w霍尔电压跨越的宽度(m)。
@核心|F=BIl sinθ ; F=B|q|v sinθ|给大小，方向垂直于I或v与B所在平面。平行于B时磁力为零。
@推导|r=\frac{mv}{|q|B} ; T=\frac{2πm}{|q|B}|匀强场、速度垂直B、无其他力且经典非相对论。磁力只改变方向，动能不变。
@推导|v=\frac{E}{B}|速度选择器：电场力与磁力大小相等、方向相反。只是筛选能直行的速率，不是把所有粒子加速到此值。
@核心|V_{H}=\frac{BI}{nt|q|}|大小式；载流子正负决定哪一侧电势高。电流沿片长，B沿厚度t，电压跨宽w。
@推导|qE_{H}=qv_{d}B ; V_{H}=E_{H}w ; I=ntw|q|v_{d}|霍尔推导取力的大小。消去E_H、v_d、w，得到上式；不要把宽w误代为厚t。

## 感应的核心概念
Magnetic flux is magnetic flux density multiplied by the area normal to the field. 磁通为磁通密度与垂直于场的有效面积的乘积。Flux linkage is the sum of magnetic flux through all turns. 磁通链为各匝磁通之和；每匝磁通相同时为NΦ。

Faraday’s law states that induced e.m.f. is proportional to the rate of change of magnetic flux linkage. 法拉第定律把感应电动势与磁通链变化率联系起来。Lenz’s law states that the induced effect opposes the change that produces it. 楞次定律说感应效应阻碍导致它的变化，而非永远反对原来的磁场。

感应实验中，磁体相对线圈静止时无持续电动势，移入和移出时偏转相反；运动更快、磁场更强、匝数更多通常使电动势更大。双线圈实验中，改变原线圈电流才会在另一线圈感应，稳定直流不产生持续互感电动势。

## 感应公式与符号
Φ magnetic flux 磁通(Wb)；A area 面积(m²)；α场与面积法线夹角；N匝数；Λ flux linkage 磁通链(Wb，常写Wb turn)；ε induced e.m.f. 电动势(V)；t时间(s)。
@核心|Φ=BA cosα ; Λ=NΦ|匀强场、平面线圈；α是与法线而非与平面夹角。场垂直圈面时磁通最大。
@核心|ε=-\frac{dΛ}{dt} ; ε_{average}=-\frac{ΔΛ}{Δt}|负号表示楞次方向约定；只求大小则取变化率绝对值。磁通很大但不变时，ε仍为零。
@推导|ε=Blv ; I=\frac{ε}{R}|导体杆的有效l、速度v、B相互垂直；电流式要求回路闭合且总电阻为R，忽略其他电动势。
@推导|Λ=NBA cosωt ; ε=NBAω sinωt|匀速转动的理想线圈，t=0时法线平行B，磁场均匀。峰值ε₀=NBAω。

## 图像和易错点
ε-t图来自磁通链图的负斜率：磁通极大或极小时电动势为零，变化最快时电动势大小最大。ε-t图的有向面积为磁通链变化的负值。开路可能有电动势但无电流；闭合后的阻碍力要求外力做功，机械能转为电能，符合能量守恒。

# 21 交流与整流
对应考纲21.1至21.2
## 核心概念
Alternating current reverses direction periodically. 交流电流周期性反向；峰值是最大大小，不能与峰峰值混淆。Root mean square current is the direct current that produces the same mean heating power in a resistor. 电流有效值是同一电阻上产生相同平均热功率的直流电流大小。

Rectification converts alternating current into unidirectional current. 整流让负载电流单向，不保证电压恒定。半波用单二极管只通过一个半周；全波桥式用四只二极管，每半周由不同的两只导通，负载电流方向保持不变。

Smoothing reduces the variation in rectified voltage. 平滑减小整流后的纹波。电容与负载并联，在峰附近充电；源电压低于电容电压时二极管截止，电容经负载放电。C或负载R增大，峰间放电更慢、纹波更小。

## 公式与符号
I₀ peak current 峰值电流(A)；V₀ peak voltage 峰值电压(V)；I_rms、V_rms有效值；R负载电阻(Ω)；P功率(W)；ω角频率(rad s⁻¹)；f输入频率(Hz)，T周期(s)；C平滑电容(F)。
@核心|I=I_{0}sinωt ; V=V_{0}sinωt ; ω=2πf|同相形式用于纯电阻负载；起始相位不同时按题目图像调整。
@核心|I_{rms}=\frac{I_{0}}{\sqrt{2}} ; V_{rms}=\frac{V_{0}}{\sqrt{2}}|只适用于完整正弦交流；不是所有波形通式。正弦周期平均电流为零，但有效值非零。
@核心|P=I^{2}R=\frac{V^{2}}{R} ; \overline{P}=I_{rms}^{2}R=\frac{V_{rms}^{2}}{R}=\frac{P_{max}}{2}|最后一个等式要求正弦纯电阻；瞬时功率始终非负，变化频率为交流频率的两倍。
@推导|I_{rms}=\sqrt{\langle I^{2}\rangle}|任何波形先平方、对时间平均、再开方；非正弦要按实际波形计算。
@推导|V_{rms,half}=\frac{V_{0}}{2} ; \overline{P}_{half}=\frac{V_{0}^{2}}{4R}|理想无平滑半波整流；平方非零时间只有原来的一半，不能仍除以√2。
@推导|V_{rms,full}=\frac{V_{0}}{\sqrt{2}} ; f_{ripple,full}=2f|理想无平滑全波整流。半波峰间隔1/f，全波峰间隔1/(2f)。
@推导|RC \gg Δt_{peaks} ; ΔV \approx \frac{I_{load}Δt_{peaks}}{C}|前式为小纹波的常用条件，后式假设负载电流近似恒定且纹波较小；不是任何整流波形的精确式。

## 易错点
实际二极管有压降时应扣除题给值，桥式每条导通路径通常包含两只二极管。平滑后不可把输出当作未平滑正弦来套有效值公式。输电接口：给定传送功率时提高电压可减小电流，从而减少线路I²R损耗；理想变压器匝比关系属于先修常识，不应把升压误说成增加总功率。

# 22 量子物理
对应考纲22.1至22.4
## 光子和光电效应
A photon is a discrete quantum of electromagnetic energy. 光子是电磁能量的一份量子；同频光子的能量相同。单色光强变大通常意味着单位面积单位时间到达的光子更多，不是每个光子更有能量。

An electronvolt is the energy gained by an elementary charge moving through a potential difference of one volt. 电子伏特是一个元电荷通过一伏电势差获得的能量，是能量单位，不是电压单位。

The work function is the minimum energy required to remove an electron from a material’s surface. 功函数是使电子逸出材料表面所需的最小能量。Threshold frequency is the minimum frequency causing photoelectric emission. 阈频是产生光电发射的最低频率；阈波长是可产生发射的最长波长。

一个光子与一个电子交换能量。频率低于阈频时，提高强度也不能在通常单光子模型下产生发射；频率够高时几乎无可测等待。固定频率下提高强度，会提高发射电子数率和可收集电流，而不改变最大动能。不同电子逸出前能量损失不同，所以题目强调“最大”动能。

## 波粒二象性与能级
干涉和衍射支持电磁辐射的波动性，光电效应支持粒子性。Electron diffraction provides evidence for the wave nature of electrons. 电子通过晶体形成衍射图样，说明运动粒子也有波动性；粒子动量越大，其德布罗意波长越小。

Electrons in isolated atoms occupy discrete energy levels. 孤立原子电子只能处于离散能级。高能级到低能级发出光子，反向跃迁吸收恰好匹配能量差的光子。低密度受激气体产生暗底亮线发射谱；连续光经过较冷气体后，某些波长被吸收，形成连续背景上的暗线。能级离散对应谱线离散。

## 公式与符号
E_γ photon energy 光子能量(J)；h普朗克常量(J s)；f频率(Hz)，λ波长(m)，c光速(m s⁻¹)；p momentum 动量(kg m s⁻¹)；Φ work function 功函数(J或eV)；K_max最大动能(J)；e元电荷(C)；V_s stopping potential 遏止电压大小(V)；m粒子质量(kg)。
@核心|E_{γ}=hf=\frac{hc}{λ} ; p=\frac{E_{γ}}{c}=\frac{h}{λ}|真空光；光子无静止质量但有能量和动量，不能用mv并取m=0断言光子动量为零。
@核心|1 eV=1.60×10^{-19} J ; hf=Φ+K_{max}|爱因斯坦光电方程为能量守恒；同一方程各能量先统一J或eV。
@核心|K_{max}=\frac{1}{2}m_{e}v_{max}^{2} ; Φ=hf_{0}=\frac{hc}{λ_{0}}|f₀阈频、λ₀阈波长；经典电子动能式适用于非相对论速率。
@推导|K_{max}=eV_{s} ; \dot{N}_{γ}=\frac{P}{hf} ; I_{photo}=e\dot{N}_{e}|P入射功率(W)，光子率和收集电子率(s⁻¹)。若量子效率不足1或收集不全，电子率小于光子率。
@核心|λ=\frac{h}{p} ; hf=E_{high}-E_{low}|前式为德布罗意关系；后式取正能级差，对发射和匹配吸收都适用。
@推导|λ=\frac{h}{\sqrt{2m|q|V_{acc}}}|带电粒子从近似静止经加速电压V_acc获得动能，忽略损失且非相对论。

## 图像和易错点
K_max-f直线斜率h，纵截距−Φ，横截距f₀；V_s-f斜率h/e。强度变化不改变这些直线在同一材料下的位置。能级常以自由静止电子为零，束缚能为负；从能级E到电离所需能量为−E。最大能级差对应最短光子波长。

# 23 核物理
对应考纲23.1至23.2
## 质量与结合能
Mass defect is the difference between the total mass of the separate nucleons and the mass of the nucleus. 质量亏损是分离核子的总质量减去所组成原子核的质量。Binding energy is the energy required to separate a nucleus completely into its nucleons. 结合能是把原子核完全拆散为相互远离的核子所需能量；形成核时释放同样大小的能量。

Binding energy per nucleon is binding energy divided by nucleon number. 每核子结合能比较平均束缚强弱。曲线从轻核快速上升，铁镍附近达到最大，重核端缓慢降低。轻核聚变和重核裂变都可能使产物平均结合更紧，从而释放能量。

Fusion combines light nuclei into a heavier nucleus. 聚变把轻核合成较重核。Fission splits a heavy nucleus into lighter nuclei. 裂变把重核分成较轻核；核反应还可能放出中子等粒子，必须全部计入质量账本。

## 衰变的核心概念
Radioactive decay is random and spontaneous. 随机表示不能预测某个核何时衰变，只能谈概率；自发表示不需要外部触发，通常不受温度、压强或化学状态影响。稳定条件下短时间计数有涨落，是随机性的证据。

Activity is the number of nuclear decays per unit time. 活度是单位时间的衰变次数。Decay constant is the probability of decay per unit time for an undecayed nucleus. 衰变常量给单个尚未衰变核单位时间衰变概率的尺度；短时间内衰变概率约为λΔt。

Half-life is the time for the number of undecayed nuclei, or the activity, to fall to half its initial value. 半衰期是未衰变核数或活度减半所需时间。样品越少每秒衰变越少，但同种核的半衰期不因剩余数量而改变。

## 公式与符号
A核子数、Z质子数、N_n中子数，无单位；B_E binding energy 结合能(J或MeV)；Δm质量亏损(kg或u)；N未衰变核数；A_act activity 活度(Bq=s⁻¹)；λ decay constant 衰变常量(s⁻¹)；t_half半衰期(s)，勿把这里的λ当波长。
@核心|E=mc^{2} ; Δm=Zm_{p}+(A-Z)m_{n}-m_{nucleus} ; B_{E}=Δmc^{2}|m_p、m_n分别为质子、中子质量。若用原子质量须一致处理电子，不能随意混核质量和原子质量。
@核心|E_{released}=(Σm_{before}-Σm_{after})c^{2}|反应物减产物；质量减少才放能。所有反应产物包括自由中子等都要计入。
@推导|E_{released}=ΣB_{products}-ΣB_{reactants} ; 1u c^{2}\approx931.5 MeV|结合能方法以核子构成总数匹配为前提；给每核子结合能时先乘相应核子数，再作差。
@核心|A_{act}=λN ; λ=\frac{ln2}{t_{half}}|活度为正的衰变率大小。若t用天，λ必须按天⁻¹；计算Bq时转成秒⁻¹。
@核心|N=N_{0}e^{-λt} ; A_{act}=A_{0}e^{-λt}|单一核素且无额外生成或混入。指数函数描述统计平均趋势，不是逐秒精确计数。
@推导|\frac{N}{N_{0}}=(\frac{1}{2})^{t/t_{half}} ; t=\frac{ln(N_{0}/N)}{λ}|衰变掉的核数为N₀−N，不是N；多种独立核素的总活度需逐项相加。
@推导|C_{net}=C_{measured}-C_{background} ; C_{net}=ηA_{act}|C计数率(s⁻¹)，η综合探测比例；几何、效率等不变时净计数率随活度同比衰减，不必数值相等。

## 核方程和图像
核方程两侧总核子数A、总电荷数守恒：α衰变使母核A减4、Z减2；β⁻使A不变、Z加1；β⁺使A不变、Z减1；γ发射不改A、Z。β过程还涉及相应中微子或反中微子，以题目要求完整写出。

净计数率的对数—时间图斜率为−λ。含背景的原始计数率趋于非零背景值，必须先扣背景再求半衰期。结合能高不是说原子核“更容易释放核子”；恰恰意味着分开它们需要更多能量。

# 24 医学物理
对应考纲24.1至24.3
## 超声
A piezoelectric crystal changes shape when a p.d. is applied and generates an e.m.f. when its shape changes. 压电晶体把电变化和机械形变互相转换。交流使它振动发射超声；回波使晶体形变并产生电信号。脉冲发出后留时间接收，不能让相邻脉冲回波混淆。

Specific acoustic impedance is the product of density and sound speed. 比声阻抗是介质密度与其中声速的乘积，反映界面两侧的声学匹配。阻抗差越大，反射通常越强；凝胶消除探头与皮肤间空气层，减小严重失配。

回波时间用于定位界面，回波强度与反射系数及沿途衰减共同有关。频率高、波长短通常提高细节分辨能力，但组织衰减通常也更强，穿透深度受限。

## X 射线与 CT
X-rays are produced when fast electrons strike a metal target. 热阴极发射电子，高电压使其加速撞击金属靶；快速减速产生连续X射线谱，靶原子内层跃迁可产生特征线。大部分输入能量变成热，靶需散热。加速电压控制最高光子能量；管电流主要影响单位时间电子数与强度。

Contrast is the difference in image signal between adjacent structures. 对比度是不同结构对应的图像信号或明暗差异，来自不同衰减；不能只说“图片更清楚”。单幅投影将沿射线路径的结构叠加，CT由同一截面不同角度的投影重建二维截面，再组合多个截面成三维图像。

## PET
A tracer contains radioactive nuclei and is taken up by the tissue being studied. 示踪剂含放射性核素，并被待研究组织吸收。PET使用β⁺核素，发出的正电子与组织电子相遇后湮灭，近静止情况下产生一对近反向γ光子。

探测器对符合事件的到达时间进行处理，确定事件所在连线，结合大量事件重建示踪剂浓度分布；飞行时间差可进一步约束线上位置。PET主要显示示踪剂分布和相关功能，CT主要给结构信息。湮灭同时守恒总能量与总动量。

## 公式与符号
c_s sound speed 声速(m s⁻¹)；t echo time 往返时间(s)；d深度(m)；ρ密度(kg m⁻³)；Z acoustic impedance 比声阻抗(kg m⁻² s⁻¹)；I intensity 强度(W m⁻²)；μ attenuation coefficient 衰减系数(m⁻¹)；x路程(m)；V_acc加速电压(V)。
@推导|d=\frac{c_{s}t}{2} ; t=2Σ\frac{d_{i}}{c_{i}}|单一均匀介质用前式，分层介质用后式；t是去和回的总时间。
@核心|Z=ρc_{s} ; R_{I}=\frac{I_{R}}{I_{0}}=(\frac{Z_{2}-Z_{1}}{Z_{2}+Z_{1}})^{2}|法向入射的强度反射系数，范围0到1；别当作振幅反射系数。无界面吸收时透射比例为1−R_I。
@核心|I=I_{0}e^{-μx} ; \frac{I}{I_{0}}=e^{-Σμ_{i}x_{i}}|第一式适用于均匀材料；后式为多层单程传播，不包含另外的界面反射损失。μ与x须用匹配单位。
@推导|x_{half}=\frac{ln2}{μ} ; \frac{I_{echo}}{I_{incident}}=R_{I}e^{-2μd}|回波式是假设单界面、同一均匀介质且不再计其他透射损失的简化模型；往返衰减路程为2d。
@核心|E_{γ,max}=eV_{acc} ; λ_{min}=\frac{hc}{eV_{acc}}|一个电子把全部获得的动能转成一个X光子时达到极限，实际多数光子能量更低。
@核心|E_{γ}=m_{e}c^{2}\approx0.511 MeV|近静止电子与正电子湮灭的两个光子各有此能量；总能量为1.022 MeV，非单个光子能量。
@推导|λ_{γ}=\frac{h}{m_{e}c} ; |Δx|=\frac{c|Δt|}{2}|波长式用上述近静止湮灭光子。时间差式给相对两探测器中点的位移大小，假设探测路径为同一直线。

## 易错点
超声是机械波，X和γ是电磁波；超声不是电离辐射。介质衰减与边界反射必须分别处理。两光子“严格反向且各511 keV”依赖初始总动量近零；题若给明显初动能或非零总动量，应重新用能量和动量守恒。

# 25 天体与宇宙学
对应考纲25.1至25.3
## 核心概念
Luminosity is the total power of radiation emitted by a star. 光度是恒星辐射的总功率，与观察距离无关。Radiant flux intensity is received power per unit area. 辐射通量密度是每单位面积接收到的功率，距离增大时减小。

A standard candle is an object of known luminosity. 标准烛光是光度已知的天体。测得它的通量密度后便可反推距离；已知的不是它“看起来有多亮”。

恒星表面可近似为黑体。更热的黑体在按波长绘制的光谱中峰值移向短波长，单位表面积总辐射功率也增大。Wien定律给温度，Stefan–Boltzmann定律再把温度、半径与总光度联系起来。

Redshift is the fractional increase of observed wavelength relative to its emitted value. 红移为观测波长相对发射波长的增加比例；需比较同一条已识别谱线。远处星系整体呈退行趋势，且越远平均退行越快，支持空间尺度在膨胀。

Hubble’s law relates recession speed to distance. 哈勃定律把退行速度与距离联系。向过去回推，宇宙尺度更小、密度和温度更高，导向热而致密的早期宇宙图景；不是从某个已确定的地球中心向外爆炸。

## 公式与符号
L luminosity 光度(W)；F radiant flux intensity 通量密度(W m⁻²)；d observer distance 观测距离(m)；r stellar radius 恒星半径(m)；T surface temperature 表面温度(K)；λ_max谱峰波长(m)；σ斯特藩常量；b维恩常量约2.90×10⁻³ m K；H₀哈勃常量(s⁻¹)；v退行速度(m s⁻¹)。
@核心|F=\frac{L}{4πd^{2}} ; d=\sqrt{\frac{L}{4πF}}|假设各向同性辐射，且吸收可忽略或已校正。距离加倍，接收强度变四分之一。
@核心|λ_{max}T=b ; L=4πr^{2}σT^{4}|恒星近似黑体，λ_max为按波长绘制的谱峰。r是恒星半径，不是到观察者的距离d。
@推导|r=\sqrt{\frac{L}{4πσT^{4}}} ; \frac{L_{1}}{L_{2}}=(\frac{r_{1}}{r_{2}})^{2}(\frac{T_{1}}{T_{2}})^{4}|同模型下做比值可减少常量计算；固定光度时更热的恒星半径更小。
@核心|z=\frac{λ_{obs}-λ_{0}}{λ_{0}} \approx \frac{v}{c}|z为红移，无量纲；λ₀实验室或发射波长。低速线性近似，不能用于任意高红移精确宇宙学。
@核心|\frac{f_{0}-f_{obs}}{f_{0}} \approx \frac{v}{c} ; v \approx H_{0}d|频率式写的是减少量的正大小。哈勃关系用于大尺度退行趋势，近邻星系的自身运动可能显著。
@推导|t_{H}=\frac{1}{H_{0}}|哈勃时间给时间尺度；把它直接当宇宙精确年龄还需假设，实际膨胀历史可能变化。

## 图像和易错点
v-d图斜率为H₀，考纲计算用SI。光谱图总面积与总辐射有关，最高点高度本身不是光度。按频率绘图的谱峰不能简单用c除以按波长绘图的峰值得到。一个天体更暗，可能光度小，也可能更远；必须有额外信息才能区分。

# 跨章节查漏
## 三类场与能量
引力：单位质量受到的力为g，单位质量的势能为φ，势能为mφ。电场：单位正电荷受到的力为E，单位正电荷的势能为V，势能为qV。磁场：磁力依赖电流或运动电荷，纯磁场对点电荷不做功。

场强是矢量，势是标量。场为零不保证势为零；势为零可能仅是零点选择或正负相消。用受力决定加速度，用能量决定端点速率，两个方法的适用条件必须分别成立。

## 四种常见指数关系
电容放电：自变量为t，比例常量1/(RC)。核衰变：自变量为t，比例常量λ。介质衰减：自变量为x，比例常量μ。电容能量：自变量为t，比例常量2/(RC)。只有“衰减率与当前剩余量成正比”的模型才形成指数规律。

@推导|y=y_{0}e^{-kx} ; ln(\frac{y}{y_{0}})=-kx ; x_{half}=\frac{ln2}{k}|统一数学形式。此处k只是衰减比例常量，不是玻尔兹曼常量；x可为时间或距离，单位随场景改变。

## 常见图像读法
F-x图面积是功；p-V图面积是气体对外功；V-Q图面积是电容储能；磁通链-t图负斜率是感应电动势；V-x图负斜率是电场分量；v-t图面积是位移。轴一旦交换，不能保留原来的斜率或面积结论。

## 单位与符号检查
看到C，先确认是库仑单位、电容还是热容量；看到T，先确认是温度、周期还是特斯拉单位；看到λ，先确认是波长还是衰变常量；看到A，先确认是面积、核子数还是活度。光强I与电流I、压强p与动量p也要靠上下文区分。

能量用eV时，和h、c、m的SI数值联用前转为J。半衰期用小时而活度单位为Bq时，先把衰变常量换成s⁻¹。指数中μx、λt和t/(RC)必须没有单位。

## 自测标准
每章完成后，合上资料回答：这个量衡量什么；能否用一句英文准确给定义；主公式每个符号及单位是什么；哪些条件不满足就不能用；图像斜率或面积代表什么。再到题型全册独立完成一道变式，并说明选模型的理由。

错误可标为概念、条件、模型选择、方向符号、单位、运算、图像或英文表达。下次复习先回到对应条目，再做一道变式验证，而不是只重复抄同一公式。

# 来源与覆盖核对
主要依据为 Cambridge International AS and A Level Physics 9702 syllabus for 2025 2026 and 2027，官方正文第26至39页。第12至25章的所有小节均已作为本册覆盖核对项；章首列出对应编号。AS接口与标为“推导”的内容服务于核心模型理解，不代表每一条都是考纲独立列出的背诵要求。

官方考纲 https://www.cambridgeinternational.org/Images/664565-2025-2027-syllabus.pdf

配套资料为本项目《CIE9702 P4 学习与题型全册 2022至2025》。本册负责概念和公式，真题小问、代表题解与精确配对的评分标准索引见题型全册。医学章节仅讨论考试中的物理原理，不构成诊断或治疗建议。

覆盖核对：12.1至12.2 圆周；13.1至13.4 引力；14.1至14.3 温度；15.1至15.3 理想气体；16.1至16.2 热力学；17.1至17.3 振动；18.1至18.5 电场；19.1至19.3 电容；20.1至20.5 磁场与感应；21.1至21.2 交流；22.1至22.4 量子；23.1至23.2 核物理；24.1至24.3 医学；25.1至25.3 天体，共44个小节。

适用考纲年份为2025至2027。若参加其他年份考试，应先核对对应版本。编制日期2026年9月17日。
