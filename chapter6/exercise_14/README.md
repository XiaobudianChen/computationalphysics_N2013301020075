>## 第十四次作业
- 作业 6.6 6.12 6.16

##摘要
本文主要解决了计算物理课本6.6题，并分析画出figure6.10能谱图。
##背景介绍
波动是质点群联合起来表现出的周而复始的运动现象。其成因是介质中质点受到相邻质点的扰动而随着运动，并将形振动形式由远及近的传播开来，各质点间存在相互作用的弹力。波动是一种常见的物质运动形式。例如绳上的波、空气中的声波、水面波等，这些波都是机械振动在弹性介质中的传播，称为机械波。
##正文
波动方程可以写成如下形式：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/公式1.png)

其中c是波速。

本文主要研究软绳上的纵波性质，考虑软绳受力以及牛顿第二定律，要解出绳波的运动状态，必须给定一定的边界条件。常见的边界条件有自由边界条件和固定边界条件等。为简单起见，这里取固定边界条件，即绳端总是不发生横向位移。对于非端点的元段，则可以让其离散化，然后通过如下的迭代方法逐步求解绳波随时间的演化： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/公式2.png)

此处![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/公式3.png)分别是时间和元段位置坐标。初始条件通过如下方法给出：在连续两个时刻，给出绳波位移，这样即可开始迭代，给出绳波随时间的演化。

- 软绳有质量的波动
如下图由[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/14.1.py)给出了模拟不同质量绳子波动时的3D图：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/figure_14.1.gif)

可以看出，相同劲度系数不同质量的软绳，质量越大其振幅越小，相应的振动频率越小。

- 高斯干扰

考虑一维弦上的波动。y代表弦上各点相对于其平衡位置的位移，x代表各点在弦上的坐标，t代表时间，c代表波在弦上的传播速度。 

接下来考察初始时刻在弦上施加一个高斯型的干扰后，弦上波的传播情况。这里我们选择弦长为1m，c=300m/s，dx=0.01m，dt=dx/c。边界点固定。在弦上施加的干扰为![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/公式4.png)其中x0=0.3m，k=1000m^(-2)。([**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/14.2.py))

弦上波的传播情况如下： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/figure_14.2.gif)

由图可知，高斯型的干扰变为了两个相反方向的波传播，这两个波的峰值为原干扰的一半。且当其传播到了边界点时，波峰变为波谷，波谷变为波峰，这对应于半波损失，即波从光疏介质传播到光密介质时相位会减少180°。

- 波的传播与叠加

齐次线性偏微分方程的一个重要特征是有限个解的线性组合也是方程的解。由此，在弦上运动的两个波包的运动是独立的。可以在弦上的x=0.3m，0.7m处各施加一个峰值不同的高斯型扰动，观察之后波包的运动。([**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/14.3.py))

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/figure_14.3.gif)

由图可知，各个波之间没有相互干扰，其在相遇前后的振幅和波速均没有变化。由此可知，这几个波作为弦的运动的解，是相互独立的。

- 波的能谱

和上面分析相同的情况下，在弦的中心位置加上高斯型的扰动后，距离x=0处端点距离为弦长的5%的点的振动大小随时间的变化情况和能谱如下([**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/14.4.py))：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter6/exercise_14/figure_14.4.png)

由理论推导可知，频率与波长之间存在关系fc=λ,,由于波长只允许为λ=2L/m,其中m为整数，因此频率只能取f=mc/2L,与理论相当吻合。
##结论
本文通过对软绳有质量的波动、叠加与传播和能谱研究，得出了一系列相关结论，其本质为介质中质点受到相邻质点的扰动而随着运动，并将振动形式由远及近的传播开来，各质点间存在相互作用的弹力。
##致谢
- 计算物理（第二版），清华大学出版社；
- 本文参考了李云龙同学的报告，万分感谢！
