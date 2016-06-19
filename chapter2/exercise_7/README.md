>## 第七次作业
- 作业L1 2.19题
> 建议：可以使用argparse和ConfigParser两个包设置程序初始参数

>- 作业L2 使用vpython可视化炮弹发射或者棒球运动
> 建议：可参考一些[例子](http://www.visualrelativity.com/vpython/)

##摘要
　　本文主要对在考虑棒球旋转的情况下的棒球的运动轨迹进行探究。
##背景介绍
　　棒球运动是典型的抛体运动，而且相对于第六次作业的炮弹发射模型，棒球的运动还会有额外的受力分析，就是其由于自旋而受到的Magnus力，受力分析图如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/棒球受力分析图.png)

　　对这一模型的综合考虑和分析将会得出棒球运动与求自旋角速度等的关系。
##正文
###运动分析
　　由棒球的受力图可以得出其运动方程：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/公式1.png)

　　其中m是棒球质量，g是重力加速度，v0是速度方向的单位矢量，ω是棒球旋转角速度。上式中的第二项为空气阻力项，而第三项即为要考虑的Magnus力。在此我们假设S0为一常量，而其中的B2关乎空气阻力，则与速度有关，对其有一近似：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/公式2.png)

　　结合前两式，由Euler法可以得出棒球飞行运动的差分方程组，如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/公式3.png)

　　由此即可迭代求出棒球运动的运动轨迹，为减小误差，选择较小的Δt可有利于得出相对更为精确的Euler解。
###程序实现
- 角速度沿水平方向
　　我们假设棒球初速度为110mph，发射角度为45°，阻力系数B2/m前式定值，而Magnus力的系数S0/m=4.1E-4,（无空气阻力时两系数均为0），写出相应[计算程序](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/7.1.py),由此可以求出棒球在有无空气阻力下的最大射程及对应发射角：

阻力有无    | 发射角大小|最大射程
--------    | ---|-----
无空气阻力  | 45°|251.9m
有空气阻力  | 35°|123.2m

　　选取Δt=0.1s,再由[画图程序](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/7.2.py)作出不同旋转角速度情况下的棒球运动轨迹（附上无空气阻力时的运动轨迹作比），如下图：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/figure_7.1.png)
- 角速度沿垂直方向（3D）
　　我们再来考虑旋转角速度沿垂直方向，这将使得棒球的飞行偏离发射面而成为一个三维运动轨迹。但是同样可以用Euler法解决方程的求解，运行[程序](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/7.3.py)可得棒球的运动轨迹，作图如下:

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_7/figure_7.2.png)

##结论
- 由结果可知，空气阻力大大地减少了棒球的射程，而且棒球自身的倒旋对其射程也有一定的影响；
- 当旋转角速度在垂直方向上时，棒球的旋转角速度影响了其偏离发射面的程度，而且旋转方向不同带来的偏转也不同。
##致谢
- [vpython](http://www.visualrelativity.com/vpython/)的一些例子；
- 蔡老师给的[代码示例](https://github.com/caihao/computational_physics_whu/tree/master/chapter1)；
- 参考了[陈洋遥](https://github.com/ChenYangyao/computationalphysics_N2013301020169)同学的程序；
- 参考了[刘星辰](https://github.com/Xcliu/computationalphysics_N2013301020167)同学的受力分析图。
