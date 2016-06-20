>## 第八次作业
- 作业3.7 3.8

##摘要
　　本文主要对比了Euler法和Euler-Cromer法两种方法的不同，并利用这两种方法的研究了单摆、阻尼摆及驱动摆的一些性质。
##背景介绍
　　振动是自然界中常见的物理现象之一，而作为其中最简单一类的简谐振动（simple harmonic motion）由于其很好的可操作性而备受关注。简谐振动可以通过施加适当的阻尼和驱动力使其变得模式多样化，其中不同的阻尼振动可分为过阻尼运动、欠阻尼运动和临界阻尼运动三种情况。
　　单摆，作为简谐振动的一个简单模型，对其的研究可以帮助我们了解简谐振动的一般性规律和特性。
##正文
###理想单摆的分析
####理论分析

　　对单摆的受力分析如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/单摆受力分析图.png)

　　受力表达式为：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式1.png)，假设单摆满足小角度震动的理想状况，即![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式2.png),可以得到其运动方程：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式3.png)

　　对方程求解可得：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式4.png)，

　　其中：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式5.png),θ0和φ是初始状态下的常数。下面分别用Euler法与Euler-Cromer法对问题进行求解。

- Euler法
　　由上式我们可以得出单摆运动的一阶方程组：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式6.png)

　　通过Euler分布计算方法可得：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式7.png)

- Euler-Cromer法
　　考虑到系统能量的守恒，![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式8.png),且同样有小角近似，可得：

　　![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_8/公式9.png)

　　可以得到Euler-Cromer法的分布计算公式如下：

　　![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_8/公式10.png)

　　由上式可以看出两种方法的公式区别在于θ的由来不一样。

####程序实现

　　由上面两种方法作为算法，假设摆长为l=1m，初始角度为θ0=10°，设计[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/8.1.py)并作图。分别选择时间间隔Δt=0.05s和0.01s,得出曲线图如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/figure_8.1.png);![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/figure_8.2.png)

###其它摆的分析
####阻尼摆

　　考虑阻尼摆的情况，运动方程可以写为如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式11.png)

　　欠阻尼情况下，其解析解为：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式12.png)；

　　过阻尼情况下，解析解为：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式13.png)

　　临界阻尼下的解析解：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式14.png).

　　同样，由Euler-Cromer法写出相应[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/8.2.py),假设摆长为l=1m,初始角速度ω0=0rad/s,初始角度为θ0=10°，时间间隔取Δt=0.01s.作图如下所示：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/figure_8.3.png)

####驱动摆

　　在阻尼摆的运动方程中加入驱动力项就可得到驱动摆的运动方程如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式16.png)

　　其中![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式17.png)为驱动项。

　　在假设摆长l=1m，初始角速度ω0=0rad/s,初始角度为θ0=10°，时间间隔取Δt=0.01s，阻尼系数q=1.0的情况下对驱动项的影响进行分析,写出相应的[**程序代码**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/8.3.py)，并用控制变量法进行分析：
- 保持ΩD=2.0不变，选用不同的F=0.4,0.8,1.2,得到振动图像如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/figure_8.4.png)

- 保持FD=0.4不变，选用不同的ΩD=1.0,2.0,3.0，得到振动图像如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/figure_8.5.png)
##结论
###理想单摆的分析
　　利用Euler法和Euler-Cromer法可以看出，前者得出的曲线与实际并不太符合，摆的振幅和能量都随着时间的增大而增大，偏差也越来越大；而Euler-Cromer法的算的结果则比较吻合，且相对比较稳定，故而后续的分析都采用Euler-Cromer法来进行。

###其它摆的分析
- 阻尼摆

　　由实验结果可以看出，欠阻尼情况下的单摆是以频率为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式15.png)摆动的，并且振幅因为能量的损耗而随时间不断减小直至为０；过阻尼情况下单摆摆角随时间呈指数形式递减；临界阻尼情况下，单摆则恰好不能起振。

- 驱动摆

1.两个变量逐一分析的情况下有一个共同点就是摆在经历一段时间的不稳定后会趋向于稳定在一个单一的振幅和频率情况下摆动，即达到稳定状态。

2.保持Ω不变的情况下，摆在稳定之后摆动的频率一定，振幅有差异；而保持F不变的情况下，稳定时的摆振幅基本相同，频率有所差异。可以看出二者影响着不同的驱动摆特性。
##致谢
- 《计算物理》（第二版），清华大学出版社；
- [蔡浩](https://github.com/caihao/computational_physics_whu/tree/master/chapter2)老师的代码支持。
