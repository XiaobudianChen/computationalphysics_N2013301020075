>## 第九次作业
- 作业L1 3.12
- 作业L2 3.16 3.21

##摘要
混沌现象很是常见，本文主要对一个简单的混沌现象模型——物理摆的混沌现象进行一些探讨与研究。
##背景介绍
混沌现象通常是指发生在确定性系统的随机的不规则运动，就是说在一个确定性理论描述的系统中，其表现出来的行为却是一种不可重复、不可预测的带有不确定性的这一现象。

通常情况下，牛顿确定性理论能够充分处理大多数线性系统，但是这些线性系统大都是由非线性系统简化而来，而现实中的很多问题都是基于非线性系统的。进一步研究表明，混沌是非线性动力系统普遍存在的现象，因此现实生活和生产中，混沌无处不在。通过对混沌现象的研究可以帮助我们更好地理解非线性系统，以便更好地利用和发展非线性系统。
##正文
###理论分析
混沌现象无处不在，我们选择前面研究过的物理摆模型来进行有关混沌现象的研究。

不同于前面研究问题时的假设，我们不再考虑小角度近似情况下的物理摆运动，而是采用非小角度近似，即非线性近似，来对物理摆模型进行更深入的探究，当然假设阻尼项和驱动项都是存在的。

由此我们可以很容易的写出物理摆所满足的运动方程：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/公式1.png)

将其化为一阶方程组并采用Euler-Cromer法对其进行求解可以得出以下计算关系式（假设θ处于![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/公式3.png)区间）：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/公式2.png)

###程序实现
- 混沌的产生

由计算关系式写出[**相应程序**]()，假设![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/公式5.png),考虑![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/公式4.png)时的θ-t曲线，如下：

![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/figure_9.1.png)

可以看出：

1.当![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=0时，摆为阻尼摆，摆在一段时间后停止运动

2.当![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=0.5时，摆能很快地进入稳定的周期性摆动状态

3.当![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=1.2时，摆的运动轨迹随时间变化毫无规律性，出现所谓的混沌现象。
- 微小扰动下的混沌

进一步研究混沌现象，假设有两个几乎相同的摆，唯一的区别在于二者摆的初始角度不同。与上面采用相同的参数，给其中一个摆施加一个初始的微小振动，使两摆初始角度相差0.001rad，通过[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/9.2.py)计算得到![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式7.png)与时间的关系曲线如下：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/figure_9.2.png)

当![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=0.5时，两摆的摆角差随时间变化是有规律的，Δθ会周期性地形成波峰，波峰的连线为一趋势线，满足关系![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式8.png)；

当![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=1.2时，变化毫无规律可循。

- 混沌线性的ω-θ曲线
利用相应[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter3/exercise_9/9.3.py)，画出![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=0.5和![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter3/exercise_9/公式6.png)=1.2时的ω-θ曲线，如下：

![]()

- 分形结构的观察


- 周期倍增下的混沌产生


##结论
##致谢
- 感谢[舟舟](https://github.com/1098605130/computationalphysics_N2013301020058)的程序代码和思路
- 《计算物理》，清华大学出版社
