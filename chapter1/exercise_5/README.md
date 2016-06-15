>## 第五次作业
- 继续用第一章的练习题熟悉python编程，并熟练撰写markdown文档

##摘要
习题1.1是对于最简单自由落体运动中的常微分方程的Euler法求解，但是在实际过程中物体下落过程会受到空气阻力的影响，则速度与时间的关系不是绝对的线性关系，参照习题1.3，本文进一步运用Euler法对较复杂的常微分方程进行求解，并优化作图细节。
##背景介绍
通常情况下作用在物体上的阻力会随着其速度的增大而增加。一个常见的例子就是跳伞运动员：跳伞的作用就是在空气的作用下增大跳伞员所受到的阻力，而这是比没有跳伞时的阻力大得多，而速度越快阻力越大，最终会达到一个平衡，本文就对这一过程进行讨论研究。
##正文
###问题分析
我们考虑一个简单的例子，即阻力只依赖于速度。假设物体的速度方程如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/公式1.png)

这里a和b是常数。你可以假设a来自于物体所受到的外力，比如落体运动中的地心引力，而b则来自于阻力，注意到阻力是负的（假设b>0）,而且其随着速度同数量级增长。

对公式进行Euler展开有（略去高次项）

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/公式3.png)

整理可得：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/公式4.png)

这就是待计算的迭代方程。
###代码程序设计
由分析所得，运用Euler法，程序语言简化为

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/公式2.png)

由此写出[完整程序](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/exercise_5.py)（包含作图语句）。
###程序实现
运行程序[](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_5/figure_1.png)
##结论
##致谢
