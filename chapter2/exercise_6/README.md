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

　　选择角度30°~60°（每隔5°取值）,由Euler法求出数值解，并绘出相应发射角度下的炮弹运动轨迹：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.1.png)

###有均匀的空气阻力
　　考虑空气阻力的情形下，假设空气均匀分布，即阻力一定，由空气阻力与速度的关系式![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式6.png)可得：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式7.png),

　　由此可得炮弹的运动方如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式8.png)

　　由此可见，此时影响炮弹射程的除了初始发射角度外，空气的稠密程度（对应于不同的空气阻力）对于射程也有影响。接下来分别控制不变的空气阻力和不变的初始发射角两个变量对炮弹发射轨迹进行分析。
####空气阻力系数一定
　　空气阻力系数一定，假设![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式9.png),发射角度为dragθ，选择角度dragθ=30°~60°（每隔5°取值），由Euler法求数值解，并画出炮弹运动轨迹如下（附上无阻力时的炮弹运动轨迹作比）：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.2.png)

####发射角一定
　　发射角一定，假设初始发射角为θ=45°，而对于空气阻力系数则设置不同的![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式10.png)，并同样由Euler法求解作图如下：
　　
![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.3.png)

###有变化的空气阻力
　　注意到炮弹运行过程中高度达到了万米，这时候空气的稀薄程度会出现变化，而不是问题所假设的空气密度均匀，而是随着而高度的增加，空气密度也是逐渐降低，即空气阻力也会随之减小，即空气阻力是高度的函数，则有：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式11.png)

　　近似认为空气为理想气体，考虑等温模型和绝热近似两种情况下的空气阻力对于炮弹轨迹的影响：
- 等温模型
　　等温近似下的空气压强满足关系![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式12.png)，其中m是单个空气分子的平均质量，kB是玻尔兹曼常数，y是距离参考点的高度，T是绝对温度，ρ0是海平面（y=0）的空气密度。而对于理想气体可得密度关系为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式13.png),则运动方程为：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式14.png)

- 绝热近似
　　绝热近似下，密度关系为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式15.png)，可得运动方程为：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/公式16.png)

　　选择初始发射角θ=45°，作出无空气阻力、有均匀空气阻力、等温模型下的空气阻力和绝热近似下的空气阻力四中情况下的炮弹发射轨迹图像，如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter2/exercise_6/figure_6.4.png)

##结论
###无空气阻力
　　从图像我们可以直观地看出对于绝对理想情况下的炮弹发射问题：
- **角度为45°**的发射角度对应于射程最远的情形；
- **初始发射角度和为90°**的两种情形会得到同样的炮弹射程，但是相对应的炮弹最大高度不一样，角度大的炮弹最大高度相对较高。

###有均匀的空气阻力
####空气阻力系数一定
　　从图像中可以看出：
- 空气阻力使得**同一角度发射**的炮弹，射程和最大高度都低于不考虑阻力的情况；
- 最远射程不再一定是发射角为45°的炮弹；
- 初始发射角度和为90°的两种情形的炮弹也不会得到相同的射程。

####发射角一定
　　在发射角一定的情况下，不同的空气阻力系数，对于炮弹的轨迹影响较大，可以看出**空气阻力系数越大，炮弹的射程和最大高度就越小**。

###有变化的空气阻力
　　由分析可知等温近似和绝热近似下，空气密度都是随着高度y的增加呈指数式下降，即空气密度变化极为明显，故在高度达到一定范围后，***空气密度的变化对于炮弹轨迹的影响也很大**，这一点也从作对比的图中可以看出。
　　
　　理想情况下（**没有空气阻力**）的炮弹射程最远，考虑**均匀空气密度的情况下射程最近**，而空气密度随着而高度变小的两种情况（等温近似和绝热近似）则居于二者中间。

##致谢
- 老师的[代码示例](https://github.com/caihao/computational_physics_whu/tree/master/chapter2)；
- [丁冬冬](https://www.zybuluo.com/Memorieddd/note/365009)同学的代码参考。
