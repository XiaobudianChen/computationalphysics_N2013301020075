>## 第十三次作业
- 作业 5.3 5.7 5.16

##摘要
本文主要介绍采用relaxation method求解计算物理课本习题5.3。
##背景介绍
静电势问题是经典电动力学的重要问题。在无源区域，静电势满足Laplace方程，从而只要在一定的边界条件下求解Laplace方程就可以得到静电势的空间分布。 
##正文
在无源区域中，静电势满足Laplace方程： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/公式1.png)

如果加上边界条件，理论上我们就可以解出电势V。但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。 

在直角坐标系下将上述方程离散化就可以得到数值求解的方法。可以将静电势方程离散化为下述形式： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/公式2.png)

理论分析表明，二维网格化离散的情况下，非边界上的点的电势相等于其周围最近的四个点的电势的平均值。 

在本文中我们使用的方法是relaxation method，这种方法可以用来数值求解以Laplace方程为代表的一类所谓的“椭圆偏微分方程”。relaxation method的三种具体情形包括Jacobi、Gauss-Seidel、simultaneous over-relaxation方法。
最简单的一种是Jacobi方法。Jacobi方法的精髓是从一个符合边界条件的猜测解开始，通过迭代，使得数值解收敛于真实的解。Jacobi方法的改进版是Gauss-Seidel方法。在计算中，我们总是算完一个点再算另一个点，也就是逐点更新计算结果。该方法主要的改进是在计算某一点的电势时，使用之前的点已经更新后的数据。Gauss-Seidel方法的改进版是simultaneous over-relaxation （SOR）方法。在这种方法中引入了参数α，从而增大了收敛速度。

- 平行板电容附近的电场

考虑平行板电容器的电势分布，为简单起见仅讨论二维问题，取两块平行板的电位分别为+1V、-1V，正方形边界的电势为0

首先使用Gauss-Seidel方法，对电容器附近的电势进行求解[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/13.1.py)，求得的电势等高分布如图所示：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/figure_13.1.png)

由Jacobi方法我们求得三维空间分布图像为： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/figure_13.2.png)

由图可知，空间中的电势场在左侧平板上呈现一个峰，在右侧平板上呈现一个谷。整体的分布情况与理论值相符。

由电势分布推得电场分布情况如下： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter5/exercise_13/figure_13.3.png)

由图可知，电场线主要从电势高的一侧侧板流向电势低的一侧侧板，板间的电场是均匀的。这与理论相符。
##结论
理论来讲，relaxation method三种不同方法迭代速率有一定差别，但是在应对电场的数值计算过程中，所得结果与电磁学理论相符，表明数值方法是可靠的。
##致谢
- 计算物理第二版，清华大学出版社；
- 本文参考了李云龙同学的报告，万分感谢！
