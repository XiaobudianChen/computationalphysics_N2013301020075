>## 第八次作业
- 作业3.7 3.8

##摘要
　　本文主要对比了Euler法和Euler-Cromer法两种方法的不同，并利用这两种方法的研究了单摆、阻尼摆及驱动摆的一些性质。
##背景介绍
　　振动是自然界中常见的物理现象之一，而作为其中最简单一类的简谐振动（simple harmonic motion）由于其很好的可操作性而备受关注。简谐振动可以通过施加适当的阻尼和驱动力使其变得模式多样化，其中不同的阻尼振动可分为过阻尼运动、欠阻尼运动和临界阻尼运动三种情况。
　　单摆，作为简谐振动的一个简单模型，对其的研究可以帮助我们了解简谐振动的一般性规律和特性。
##正文
　　对单摆的受力分析如下：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/单摆受力分析图.png)

　　受力表达式为：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式1.png)，假设单摆满足小角度震动的理想状况，即![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式2.png),可以得到其运动方程：

　　![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式3.png)

　　对方程求解可得：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式4.png)，

　　其中：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_8/公式1.png),θ0和φ是初始状态下的常数。下面分别用Euler法与Euler-Cromer法对问题进行求解。

- Euler法

- Euler-Cromer法


##结论
##致谢
- 《计算物理》（第二版），清华大学出版社；
- [蔡浩](https://github.com/caihao/computational_physics_whu/tree/master/chapter2)老师的代码支持。
