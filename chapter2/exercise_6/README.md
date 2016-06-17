>## 第六次作业
- 作业L1 2.9题
- 作业L2 2.10题强化版（引入风阻）————“辅助精确打击系统”
- 作业L3 发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差1%，速度有5%的误差，风阻误差10%，可以考虑引入Coriolis force等，以炮弹落点与打击目标距离差平方均值最小为优胜）

##摘要
　　通过对抛体运动的分析，同样使用Euler法对抛体运动中的物理过程进行算法求解。其间从没有空气阻力的理想情况开始，逐次考虑有均匀的空气阻力、有随高度变化的空气阻力等具体情况，来对抛体运动进行研究，并得到相应结论。
##背景介绍
　　继续拓展第一章的落体运动至二维平面，即为通常所说的抛体运动，而炮弹的发射为典型的抛体运动，对其的研究可以得到相应的抛体运动问题的定性解。

　　在炮弹发射问题中，初速度一定的情况下，发射距离与发射角度存在一定的关系，而这一关系也会随着空气阻力的有无以及空气密度变化的不同而不同，我们通过研究不同情况下的炮弹发射距离与发射角之间的关系可以获知外界空气阻力因素对这两这关系的影响。

　　一般情况下（不考虑科里奥利力），炮弹运动方程可以分解为垂直方向上的两个二阶常微分方程，求解这两个方程可以对炮弹的运动过程进行相应的研究。
##正文
　　假设重力加速度为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式1.png),初速度v=1000m/s,则分别从以下几种情况讨论炮弹落点与相关影响因素的关系。
###无空气阻力
　　无空气阻力的情况下，水平x方向不受力，设发射角度为θ，则有：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式2.png)

　　落地时有：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式3.png)

　　求解得：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式4.png)

　　这即是炮弹发射的水平距离与初始发射角的关系方程。

　　转化为迭代微分形式：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式5.png)



![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.1.png)

###有均匀的空气阻力

####空气阻力系数一定

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.2.png)

####发射角一定

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.3.png)

###有变化的空气阻力

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.4.png)

##结论
##致谢
- 老师的[代码示例](https://github.com/caihao/computational_physics_whu/tree/master/chapter2)；
- [丁冬冬](https://www.zybuluo.com/Memorieddd/note/365009)同学的代码参考。
