# 使用说明与学习路线

这份手册用于从零建立 Cambridge 9702 A2 Physics Paper 4 的模型，再按题型练习和查缺补漏。它覆盖本项目已核实的2022至2025年25份P4与各自评分标准，不包括P5，也不声称涵盖这些年份网站上每一份可下载试卷。考纲依据为2025至2027版；若参加其他年份考试，应先重新核对适用考纲。

与已经学过FS后“熟悉考法”的路线不同，你的P4路线应是“概念与条件→讲解代表题→独立变式→解释为什么→延迟混合复测”。不要第一遍就拿完整卷反复试错。读懂例题也不等于能够独立选择模型。

完整性分成两件事：本手册的资料整理可以完成，你的个人掌握需要后续作答证据。全部掌握状态初始为未学；本文件没有把任何题型标记为已掌握。手册是一份全册参考，不要求你一次学完85条。

建议按以下顺序分组，每组是否进入下一组由理解证据决定，不按固定天数硬赶：X基础与C圆周→G引力；T温度→K气体→H热力学；S振动；E电场→D电容；B磁场→I感应→A交流；Q量子→N核物理；M医学与Z天体。首次学习可把每次训练限制在一个模型或两个紧密相关的条目。

一轮训练建议用45至75分钟：先用15分钟梳理定义与符号，读一条代表题的模型与解法；盖住答案复述关键因果关系；再独立完成该条“下一道变式”。遇到障碍先诊断是没学过概念、识别错题型还是运算问题，再只补对应环节。时间建议可以按你的节奏调整。

后续刷卷时先看题型树，选择未掌握条目。独立作答应保留受力图、方程来源、单位和文字推理，不能只记最终数值。典型题过关后隔2至3天做一次不提示类型的混合复测；隔约一周再检查迁移。复测间隔是学习建议，不是官方要求。

## 怎样使用题号与索引

本手册用s24/42 Q1(c)(i)这样的短引用：s表示May/June，w表示October/November，m表示February/March；24表示2024年；42是试卷版本。完整源文件名为9702_s24_qp_42及9702_s24_ms_42。两个版本的答案不能混用。

每个条目给出代表小问、分数、原题大题起始位置和精确MS页码。“QP合并页”是项目题卷合并PDF的页码，从1计数，指该大题起始页；小问可能在随后页。“MS合并页”是评分PDF中该小问条目起始页。它们不一定等于纸面页脚号。

附录的逐卷索引包含每个小问及其分值和主类型；“+”后是交叉关联。每小问仅在主类型统计中计分一次，关联条目数量可以重复。条目内的完整题源索引可反向找题；逐卷附录可从任意题号查所属模型。

代表题解法用中文重述与解释。B是独立陈述/结论分，M是方法分，A是依赖方法的准确性分，C是可由正确后续结果隐含体现的补偿分；实际评分以该题完整MS及其通则为准。条目中标出的字母分是该代表小问的具体评分点，不是未来所有同类题的固定分配。英文句是可用的物理表达，除明确指定为该小问答案外，不代表整句在所有题中都必需。

# 入门所需的AS工具

矢量 vector 同时有大小与方向；标量 scalar 只有大小。力、速度、加速度、电场与磁场是矢量；速率、能量、电势和温度是标量。直观上，标量可以直接带符号相加，矢量必须先考虑方向和分量。

Newton’s second law: the resultant force equals the rate of change of momentum. 质量不变时ΣF=ma，合力等于质量乘加速度。ΣF是resultant force合力(N)，m是mass质量(kg)，a是acceleration加速度(m s⁻²)。先找受力来源，后写“合力用来做什么”；“向心力”不应与重力、张力并列为额外相互作用。

Kinetic energy is the energy associated with motion. K=½mv²是经典动能(J)，v为speed速率(m s⁻¹)；momentum p=mv是动量(kg m s⁻¹)，有方向。这些经典式用于非相对论情境；有光子的题用p=E/c而不是mv。

Work is the energy transferred by a force acting through a displacement. W=Fs cosα是功(J)，s为displacement位移(m)，α为力和位移的夹角。平行力做功，垂直力不做功。Power is energy transferred per unit time，P=ΔE/Δt是功率(W)，不是总能量。

Density is mass per unit volume，ρ=M/V。ρ是density密度(kg m⁻³)，M为总质量(kg)，V为volume体积(m³)。弹簧的F=k_s x中k_s是spring constant劲度系数(N m⁻¹)，x是相对自然长度的extension伸长(m)；已有预拉伸时比较增量ΔF=k_sΔx。

Electric current is charge flow per unit time，I=ΔQ/Δt。I是current电流(A)，Q是charge电荷(C)，t是time时间(s)。漂移模型I=nAqv_d中n是number density数密度(m⁻³)，A是cross-sectional area截面积(m²)，q是单载流子电荷量(C)，v_d是drift speed漂移速率(m s⁻¹)。这里的n不是气体方程的摩尔数。

运算底线：1 cm=10⁻² m，因此1 cm²=10⁻⁴ m²、1 cm³=10⁻⁶ m³；μ=10⁻⁶，n=10⁻⁹，p=10⁻¹²。角度代入圆周或正弦随时间方程时使用rad。指数和对数中的量必须无量纲。最终有效数字通常随题给精度，中间多留几位，图读数范围以MS为准。

图像的gradient斜率是纵量变化/横量变化，area面积是纵量×横量，intercept截距是横量为零时纵值。切线斜率给瞬时变化率，连接两点给平均变化率。请先读轴标签和倍率，再看形状；不能看到直线就固定说斜率为某常数。

# C 圆周运动的基础模型

Angular displacement is the angle swept out about the centre. 角位移θ表示绕圆心转过的角(rad)，θ=s/r，其中s为arc length弧长(m)，r为轨道radius半径(m)。直观上，弧长占半径的几倍就是转过多少弧度。

Angular speed is angular displacement per unit time. 角速率ω=dθ/dt(rad s⁻¹)衡量转角快慢；匀速时ω=2π/T，θ=ωt。T为period周期(s)，f为frequency频率(Hz)，f=1/T。ω=2πf将每秒圈数换成每秒弧度数。

Tangential speed equals radius times angular speed. v=rω，线速率v(m s⁻¹)是沿轨迹走路的快慢。相同ω下外圈一秒走过的路更多，所以v更大。r必须量到运动物体中心，不能量到外边缘。

Centripetal acceleration is the inward acceleration of circular motion. 向心加速度大小a=v²/r=rω²(m s⁻²)，方向向圆心；所需径向合力ΣF_r=ma。速率恒定而方向变化，仍然需要加速度。仅有垂直于速度的合力不会改变动能。

# G 引力场的基础模型

Gravitational field strength is force per unit mass. g=F/m是单位测试质量所受引力(N kg⁻¹，等同m s⁻²)。直观上，它表示“把1 kg物体放在这里会受多大引力”，与该测试质量自身无关。

Newton’s law gives F=GMm/r²，G为gravitational constant引力常量(N m² kg⁻²)，M为source mass源质量(kg)，m为test mass测试质量(kg)，r为中心间距(m)。球外均匀球体可等效球心点质量；由此g=GM/r²，场线指向质量。

Gravitational potential is work done per unit mass in bringing a small test mass from infinity to a point. φ=−GM/r是引力势(J kg⁻¹)，以无穷远为零。中文精确定义是从无穷远移来单位小测试质量时对应的外力功；直观上是每kg所处的能量高度，靠近吸引源更低。

U=mφ=−GMm/r为gravitational potential energy引力势能(J)。能量守恒K_i+U_i=K_f+U_f用于落体与逃逸；v_escape=√(2GM/r)是从静止位置出发恰好到无穷远的所需初速，条件是不再推进、无阻力，末速趋零。圆轨道v_orbit=√(GM/r)则来自径向受力，不是相同任务。

# T 温度与热量的基础模型

Thermal equilibrium means equal temperature with no net heat transfer. 热平衡意味着温度相同、接触时无净热传递；不意味着两个物体内能相等。Thermodynamic temperature热力学温度T的单位是K，不依赖任一特定物质的测温性质；T/K=θ/°C+273.15。

Specific heat capacity is thermal energy per unit mass per unit temperature rise. 比热容c_th=Q/(mΔT)，单位J kg⁻¹ K⁻¹；Q为供热能量(J)，m为质量(kg)，ΔT为温差(K)。直观上，c越大，同样质量升一度越费热量。Heat capacity热容量C_th=mc_th，单位J K⁻¹，描述整个物体；不要与电容C混淆。

Specific latent heat is thermal energy per unit mass for a change of state at constant temperature. 比潜热L_h=Q/m，单位J kg⁻¹，是单位质量在温度不变条件下完成相变所需热量；L_f为熔化潜热，L_v为汽化潜热。直观上，能量用于改变分子间安排而非升温。升温段与相变段应分开记账。

Energy supplied by a constant-power heater is Q_in=Pt. P为加热功率(W)，t为时间(s)；液体实际获得Q_liquid=Pt−Q_container−Q_loss。热量守恒并非“两个数永远相等”，而是所有输入输出去向必须列齐。

# K 理想气体的基础模型

An ideal gas obeys pV proportional to thermodynamic temperature for a fixed amount of gas. 理想气体固定数量时pV∝T。p为pressure压强(Pa)，V为volume体积(m³)，n为amount of substance物质的量(mol)，R为molar gas constant摩尔气体常量(J mol⁻¹ K⁻¹)，状态方程pV=nRT。

One mole contains Nₐ particles. 一摩尔含阿伏伽德罗常量Nₐ个粒子，Nₐ单位mol⁻¹，N=nNₐ。Boltzmann constant k=R/Nₐ是单粒子尺度的常量(J K⁻¹)，所以pV=NkT；N为分子个数，非摩尔数。直观上两套式子只是整mol和逐分子两种计数。

Pressure results from molecular momentum changes at the walls. 气体压强来自分子碰壁的动量交换；模型假设随机运动、弹性碰撞、分子体积可忽略、碰撞外相互作用可忽略。pV=(1/3)Nm⟨c²⟩，m为单分子质量(kg)，⟨c²⟩为mean-square speed均方速率(m² s⁻²)。

Mean translational kinetic energy depends only on temperature. 单分子平均平动动能⟨K⟩=(3/2)kT=(1/2)m⟨c²⟩。c_rms=√⟨c²⟩为root-mean-square speed均方根速率(m s⁻¹)。温度相同代表平均平动动能相同，不代表所有分子同速；同温重分子rms更低。

# H 热力学的基础模型

Internal energy is the microscopic kinetic and potential energy of a system. 内能U是系统粒子随机运动及相对安排对应的动能、势能之和(J)，与整个物体整体平移不同。相同状态内能相同；供热或做功都可能改变它。

The first law is conservation of energy for the system. 第一律ΔU=Q+W_on；ΔU为内能增加(J)，Q为流入系统的热能(J)，W_on为外界对系统做的功(J)。若使用对外功W_by，则ΔU=Q−W_by。直观上，入账为正、出账为负，但同一题不能中途换记账约定。

At constant external pressure, W_by=pΔV. 外压恒定时气体对外功为p乘体积增加，单位Pa m³=J；W_on=−pΔV。变压过程功由p-V图面积给出。等容ΔV=0所以功为零；绝热Q=0不等于温度不变；等温理想气体ΔU=0不等于无热交换。

For the ideal-gas energy model used here, U=(3/2)NkT=(3/2)pV. 固定分子数量下内能正比于绝对温度。用于本考纲给定的平动动能模型；不要把它推广成所有真实多原子气体任何温度下的全部内能公式。周期过程末态回到初态，ΣΔU=0，但各段Q和W一般不为零。

# S 振动的基础模型

Simple harmonic motion has acceleration proportional to displacement and directed towards equilibrium. 简谐运动满足a=−ω²x；x为从equilibrium position平衡位置量起的displacement位移(m)，ω为angular frequency角频率(rad s⁻¹)。负号表示拉回去，比例表示偏得越远拉回加速度越大。

Amplitude is the maximum magnitude of displacement. 振幅x₀是最大位移大小(m)，不含正负；若给绝对高度h的最大最小值，h_eq=(h_max+h_min)/2，x₀=(h_max−h_min)/2。Period T和frequency f同圆周定义，ω=2π/T。

For one choice of initial phase, x=x₀sinωt and v=ωx₀cosωt. v为velocity速度(m s⁻¹)，v₀=ωx₀为最大速率；a与x反相。一般v=±ω√(x₀²−x²)，同一位置可能向两个方向运动。Phase difference相位差Δφ=2πΔt/T(rad)，表示两个周期状态错开多少圈。

In undamped SHM, total energy is constant. 无阻尼时E=½mω²x₀²，K=½mω²(x₀²−x²)，U_osc=½mω²x²；三者单位J，m为振动物体质量(kg)。U_osc是以平衡点为零的系统恢复势能；竖直弹簧情景需把重力和弹簧势能合起来理解。能量在K和U_osc间转换。

Damping is energy loss due to resistive forces. 阻尼使振动机械能减少；轻阻尼多次过平衡点，临界阻尼最快且不振荡返回，重阻尼更慢而不振荡。Resonance共振是在考纲模型中驱动频率等于自然频率时达到最大振幅；其图是振幅对驱动频率，不是位移对时间。

# E 电场的基础模型

Electric field strength is force per unit positive charge. E=F/q是electric field strength电场强度(N C⁻¹或V m⁻¹)，F是电力(N)，q是测试电荷(C)。直观上它表示正电荷在此处被推向哪里、每库仑推多强；负电荷受力反向。

For point charges in free space, F=k_e abs(Qq)/r² and k_e=1/(4πε₀). Q为源电荷(C)，r为中心间距(m)，ε₀为permittivity of free space真空介电常量(F m⁻¹)，k_e单位N m² C⁻²。点电荷场E的径向分量为k_eQ/r²；电荷符号和坐标方向要统一。

Electric potential is work done per unit positive charge in bringing a small test charge from infinity to a point. V=k_eQ/r是electric potential电势(J C⁻¹即V)。直观上它是每单位正电荷的能量高度；多个源的电势按正负代数相加。U=qV是electric potential energy电势能(J)。

The field is the negative potential gradient. 一维E_x=−dV/dx；x为位置(m)，斜率单位V m⁻¹。匀强平行板间场强大小E=abs(ΔV)/d，d为板间距(m)，方向从高势到低势。板内粒子加速度a=qE/m；能量变化ΔK=−qΔV。前者用力和时间，后者用端点能量，二者应一致。

# D 电容的基础模型

Capacitance is stored charge per unit potential difference. C=Q/V，C为capacitance电容(F)，Q为一板电荷大小(C)，V为两板potential difference电势差(V)。孤立球的V是球相对无穷远的电势。直观上，C越大，同样电势下能存更多电荷。

In parallel, voltages are equal and charges add; in series, charges are equal and voltages add. 并联C_eq=ΣC_i；串联1/C_eq=Σ(1/C_i)。这些关系来自Q=CV与节点约束，不是独立于电路拓扑的口诀。

Stored energy is W=½QV=½CV²=Q²/(2C)，单位J。V-Q图纵轴为V时，面积直接是做功；直观上充入后来的一库仑需克服更高电势，所以平均电势只有末值的一半。重连后常见总电荷守恒而电场能减少。

The time constant controls the fractional decay. τ=RC(s)，R为resistance电阻(Ω)。固定R、C放电时x=x₀exp(−t/τ)，x可代表Q、V或I；t为从该放电段起点计的时间(s)。每经过τ剩下之前的1/e，不是减去固定值。I₀=V₀/R，放电流方向由电路定义决定。

# B 磁场的基础模型

Magnetic flux density is force per unit current per unit perpendicular wire length. B为magnetic flux density磁通密度(T)，垂直时B=F/(IL)。一般F=BIL sinθ，I为传统电流(A)，L为场中有效导线长度(m)，θ为电流与场夹角。直观上B描述同样电流同样长度受到多大磁力。

For a moving charge, F=B abs(q) v sinθ. q为电荷(C)，v为速率(m s⁻¹)，θ为v与B夹角。方向同时垂直二者，负电荷反向。在纯磁场中磁力不做功，垂直入射形成圆轨道r=mv/(abs(q)B)，T=2πm/(abs(q)B)，适用于经典质量不随速度变化的模型。

Velocity selection requires balanced opposite electric and magnetic forces. 选择器满足v=E/B，E为电场强度，B为磁通密度。它让特定速度直行；不是将粒子加速到该速度。

Hall voltage results from sideways charge separation. 霍尔电压V_H=BI/(n t q)，n为carrier number density载流子数密度(m⁻³)，t为与几何定义对应的样品thickness厚度(m)，q取载流子电荷量大小(C)。由横向电场力与磁力平衡，再结合I=nAqv_d可推导；V_H单位V。薄样品、小n产生较大霍尔信号。

# I 电磁感应的基础模型

Magnetic flux is magnetic flux density times area perpendicular to the field. Φ=BA为magnetic flux磁通(Wb)，A为垂直有效面积(m²)；若平面法线与B夹角α，则Φ=BA cosα。N匝的flux linkage磁通链Λ=NΦ，N是匝数，无量纲。

Faraday’s law relates induced e.m.f. to rate of change of flux linkage. ε=−dΛ/dt，ε为induced e.m.f.感应电动势(V)，t为时间(s)。负号表达楞次方向约定；仅求大小时取斜率绝对值。直观上“改变得快”才产生大电压，不是“穿过得多”就一定有电压。

Lenz’s law gives opposition to the change producing the e.m.f. 感应效应阻碍导致它的变化。闭合回路能有感应电流并产生磁力；开路也可能存在电动势，不能用“没有电流”断言“没有感应”。

For a perpendicular moving rod, ε=Blv. l为rod length导体长度(m)，v为speed速率(m s⁻¹)；条件是相互垂直的有效长度、速度和磁场。它可由扫过面积速率dA/dt=lv与法拉第定律获得，复杂转动题则先算每次扫过的面积和所用时间。

# A 交流与整流的基础模型

An alternating current changes direction periodically. 交流I=I₀sinωt或I₀cosωt，I₀为peak current峰值电流(A)，V₀为peak voltage峰值电压(V)，ω为角频率(rad s⁻¹)，T=2π/ω。初相位由图上t=0的值和方向确定。

The r.m.s. value gives the same mean heating power as a steady d.c. value. 有效值I_rms=√⟨I²⟩，不是平均I；其直观意义是“等效发热的直流大小”。对正弦I_rms=I₀/√2，V_rms=V₀/√2。

For a resistive load, P=I²R=V²/R. P为瞬时power功率(W)，R为固定电阻(Ω)。正弦平均功率⟨P⟩=P_peak/2；相同峰值的理想半波整流平均功率=P_peak/4，V_rms=V₀/2；全波平方后和原正弦相同，平均功率仍P_peak/2。非正弦要逐段平均平方，不能套√2。

Rectification makes the current unidirectional; smoothing reduces its ripple. 整流让电流单向，平滑减小波动。理想二极管近似正向导通、反向截止；桥式每半周两只导通。负载并联电容在峰间放电，RC较大相对峰间隔意味着纹波较小；题若给实际二极管压降，应按题修正。

# Q 量子物理的基础模型

A photon is a quantum of electromagnetic energy. 光子是一份离散电磁能量，E_γ=hf=hc/λ；h为Planck constant普朗克常量(J s)，f为频率(Hz)，c为真空光速(m s⁻¹)，λ为波长(m)，E_γ单位J。频率决定一份有多大，强度在固定频率下主要决定有多少份。

An electronvolt is the energy gained by an elementary charge through one volt. 1 eV=1.60×10⁻¹⁹ J，e为elementary charge元电荷大小(C)。Photon momentum光子动量p=E_γ/c=h/λ，单位N s；光束功率P=光子数率×E_γ，强度I_rad=P/A，单位W m⁻²。

Work function is the minimum energy needed to remove an electron from a surface. 功函数Φ_w为释放电子所需最小能量(J或eV)。阈频f₀=Φ_w/h是最低可致光电发射频率；阈波长λ₀=hc/Φ_w是最长可致发射波长。Einstein’s equation为hf=Φ_w+K_max，K_max=½m_ev_max²=eV_s，V_s为stopping potential遏止电压的大小(V)。

De Broglie wavelength is the wavelength associated with a moving particle. λ=h/p把物质粒子的动量与波长联系；直观上动量越大，波长越短，宏观物体波长常小到无法在普通缝隙观察衍射。非相对论带电粒子经电压V加速且初速可忽略时p=√(2m abs(q)V)。

Atomic line spectra arise from discrete energy changes. 原子能级E_n有离散允许值，跃迁光子满足hf=E_high−E_low。发射由高到低，吸收由低到高；孤立原子常把自由电子能量设0，束缚能级为负。频率与差值成正比，而波长与差值成反比。

# N 核物理的基础模型

Mass and energy are equivalent: E=mc². E为energy能量(J)，m为mass质量(kg)，c为光速。质量亏损Δm是自由组成核子质量和减去核质量；binding energy结合能B_E=Δmc²，是将核子完全分离到无穷远所需能量。原子质量单位u约为1.66×10⁻²⁷ kg。

Nucleon number A counts protons and neutrons; proton number Z counts protons. 核子数A=Z+N_n，N_n为中子数。每核子结合能B_E/A(J或MeV)可比较平均束缚强弱。核反应两边A、Z分别守恒；反应释放ε=(反应物总质量−产物总质量)c²。

Activity is the number of nuclear disintegrations per unit time. 活度A_act=λ_d N，单位Bq=s⁻¹，N为未衰变核数，λ_d为decay constant衰变常量(s⁻¹)，代表单个核单位时间衰变概率的尺度。这里A_act不是核子数A。

Half-life is the time for the number of undecayed nuclei or the activity to halve. 半衰期t_half单位与题一致，λ_d=ln2/t_half。N=N₀exp(−λ_dt)，A_act=A₀exp(−λ_dt)；宏观指数下降来自剩余核越少、每秒衰变机会越少。Random随机与spontaneous自发的含义见N03，不互相替代。

For symmetric electron-positron annihilation at rest, each photon has energy m_ec². 电子与正电子总静能2m_ec²转成两个反向光子，每个约0.511 MeV；总动量为零保证两者动量等大反向。若有初动能或非零总动量，应从整体能量动量重新计算，不能无条件套固定光子能量。

# M 医学物理的基础模型

A piezoelectric crystal converts between electrical and mechanical changes. 压电晶体受电势差作用变形，反过来变形产生电势差。超声pulse脉冲往返同一均匀介质时depth d=c_s t/2；c_s为sound speed声速(m s⁻¹)，t为回波时间(s)。不同介质路径需分段累计时间。

Specific acoustic impedance is density times sound speed. Z_a=ρc_s为比声阻抗(kg m⁻² s⁻¹)，ρ为介质密度(kg m⁻³)。正入射界面intensity reflection coefficient强度反射系数R_I=I_R/I₀=[(Z₂−Z₁)/(Z₂+Z₁)]²；I_R为反射强度，I₀为入射强度(W m⁻²)。阻抗越不匹配越容易反射。

Attenuation is exponential loss of intensity with distance. I=I₀exp(−μx)，μ为attenuation coefficient衰减系数(m⁻¹或cm⁻¹)，x为介质路程，I为透射强度。μx必须无量纲；去回超声的同段路程需计两次，X射线单程按实际层厚算。界面反射与介质内衰减是两个不同环节。

The maximum X-ray photon energy is eV_acc. V_acc为加速电压(V)，故λ_min=hc/(eV_acc)。对比度是不同结构对应图像明暗/黑化程度的差异，来自探测强度差；CT用多个角度多个层面重建，不只是一幅二维投影变大。

PET measures the distribution of a positron-emitting tracer. PET示踪剂含β⁺放射性核，被组织吸收后产生正电子，再与电子湮灭。体外γ探测事件及到达时间用于定位并积累浓度图像；不要把结构成像和示踪剂分布完全等同。

# Z 天体与宇宙学的基础模型

Luminosity is the total power radiated by a star. 光度L_star单位W，与观察者距离无关。Radiant flux intensity F_rad is power received per unit area，辐射通量密度F_rad=L_star/(4πd²)，单位W m⁻²；d为源到观察者距离(m)。标准烛光是已知光度的天体，不是“看起来一样亮”的天体。

Wien’s displacement law relates the peak wavelength to surface temperature. λ_max T=b，T为表面热力学温度(K)，λ_max为按波长表示的黑体谱峰(m)，b为维恩常量(m K，数值按题给定)。直观上更热的表面峰移向更短波长。

The Stefan-Boltzmann law gives luminosity from surface area and temperature. L_star=4πσr_star²T⁴，σ为Stefan-Boltzmann constant斯特藩常量(W m⁻² K⁻⁴)，r_star为恒星半径(m)。与测距公式中的d不同。把谱峰求得的T和总光度结合，才可反推恒星半径。

Redshift is an increase in observed wavelength relative to the emitted wavelength. z=(λ_obs−λ₀)/λ₀近似v/c，v为退行速度(m s⁻¹)，λ₀为发射/实验室波长。频率对应降低，(f₀−f_obs)/f₀在小v/c下近似相同。高速或宇宙学精确模型超出这里的线性近似，考试按题给关系使用。

Hubble’s law relates recession speed to distance on large scales. v≈H₀d，H₀为Hubble constant哈勃常量(s⁻¹)。直观上越远的星系平均退行越快，支持宇宙膨胀。回推过去尺度更小、密度更高形成大爆炸图景；不应把H₀当作某个天体的角速度。
