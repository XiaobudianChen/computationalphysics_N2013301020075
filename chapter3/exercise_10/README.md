>## 第十次作业
- 作业L1 3.26
- 作业L2 3.29 3.31
- 作业L3 将以上题目使用vpython进行一个3D展示

##摘要
前面研究了混沌现象的一个例子——单摆混沌，而作为混沌大家庭中的洛伦兹模型，也是研究混沌的一个重要模型，本文就对这一模型进行相关的探究。
##背景介绍
洛伦兹模型是洛伦兹（E.N.LORENZ）从气象问题中抽象出来的一个极简化的模型，能够很好地产生混沌现象，并对相应的机制有所展示。
##正文
洛伦兹模型是从流体力学中的Navier-Stokes方程在Rayleigh-Benard问题中简化得到的一个方程组，其反映了速度、温度、密度变量随时间演化的规律：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/公式1.png)

其中x,y,z分别为流体温度、密度和速度，而r放映由温差带来的驱动效果，b则反映了流体的阻尼。上式对实际问题太过简化，但足以产生混沌现象供我们研究。

Euler法在数值求解此问题时仍然能够提供不错的计算精度，故而仍然采用Euler法求解该问题。

Lorenz模型内流体运动显著依赖于驱动r，当改变驱动r的大小时，即可观察到混沌的产生与消失。

- 混沌出现

取实验参量为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/公式2.png)，初始值x=1,y=z=0,时间间隔为dt=0.0001，写出[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/10.1.py)
在不同的r值时画出速度z随时间变化的曲线：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/figure_10.1.png)

当r=5,10 时，驱动幅度较小时，没有混沌产生，流体在经过一段暂态的过程后进入稳恒的对流运动过程；

当r=25时，强驱动情况下，此时流体发生了复杂的混沌运动。

- 相图分析
 
作出x,y,z相空间的图形，更能揭示混沌现象的内在规律性（[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/10.2.py)）。

取r=25，其他参量不变，分别作出x-z,y-z相空间的曲线关系，如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/figure_10.2.png)

可以看出，相空间的轨迹表现为明显的混沌现象。

其它参数不变，进一步取r=25，利用相应[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/10.3.py)作出相空间截面图如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/figure_10.3.png)

由此可以看出，界面对应的曲线关系与初值无关，也就是说尽管混沌对于初值极其敏感，但是其相空间截面却与初值无关，即混沌现象内在存在一定的可预测性。

- 周期倍增

继续增大r值，去到r=160和r=163.8，其他参量不变，利用[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/10.4.py)作出相应的曲线变化图：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_10/figure_10.4.png)

可以看到在r=160时，系统在一段时间后作周期运动。但是当继续增大r至163.8时，系统整体呈现除周期性趋势，但是混杂着混沌现象。
##结论
混沌现象是极其普遍的，其对于初值的敏感性也是极其严重的，初始阶段的微小扰动都会使得最终结果产生极大误差，这也是即是所谓的“蝴蝶效应”。
##致谢
本文参考了[团长](https://github.com/Tuanzhang0531/computationalphysics_N2013301020065)同学的报告。
