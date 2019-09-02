>## 第十二次作业
- 作业 4.16 4.18 4.20

## 摘要
本文主要探讨了太阳、地球及木星组成的三体问题，观察木星质量的变化以及初始速度变化对地球运动轨迹的影响。  

## 背景介绍
前面讨论的双星问题，我们都是只考虑太阳的引力影响，但是木星质量不可忽略，相比较太阳与地球的两体运动，对于三体运动我们需要考虑木星对地球及太阳的影响。  

## 正文
假设三者处在同一平面x-y平面，我们利用牛顿第二定律以及万有引力公式可以得到地球x方向上的运动方程： 

![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter4/exercise_12/公式1.png)

同理可得到地球运动y方向的运动方程，以及木星x，y方向上的运动方程。

本文计算使用欧拉-克拉默方法，可得[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/12.1.py)。 

已知太阳质量，地球质量和木星质量分别为：![](https://github.com/XiaobudianChen/computationalphysics_N2013301020075/blob/master/chapter4/exercise_12/公式2.png)

- 标准状态

三者质量为标准状态时，可以得到如下运动轨迹： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.1.png)

可见此时太阳保持不动，木星与地球绕太阳做圆周运动，三者保持稳定运动状态。这是由于太阳的质量相对其余二者而言相当大，木星对地球的影响可以忽略。

- 木星质量增大10倍

将木星质量增大至10倍,此时三者运动轨迹为： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.2.png)

可以看到地球的运动开始受到影响，太阳也不再固定不动，但三者仍能稳定运动。

- 木星质量增大100倍

将木星质量增大至100倍,此时三者运动轨迹为： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.3.png)

此时地球运动变得复杂，太阳做圆周运动。

- 木星质量增大1000倍

将木星质量增大至1000倍,此时三者运动轨迹为： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.4.png)

由于此时木星质量与太阳质量已经相当，引力无法束缚住太阳和木星，它们相互远离。由于地球一开始与太阳距离更近，在之后地球跟随着太阳运动。

- 改变木星初始速度

将木星质量增大至1000倍后，太阳与木星的质量已经相当，我们希望看到二者做稳定的两体运动于是我们减小木星的初速度，分别为0.9，0.8,0.7,0.6倍原初始速度，得到三者运动轨迹：

0.9倍，时间为40.0： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.5.png)

0.8倍，时间为40.0： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.6.png)

0.7倍，时间为30.0： 

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.7.png)

0.6倍，时间为20.0：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_12/figure_12.8.png)

可以看到地球的运动变得不可预测，而木星与太阳做稳定的两体运动。  

## 结论
通过文中的探讨，我们可以得出以下结论：

1.木星对地球有引力的影响，且随着其质量的增大，这种影响也会变大。

2.当有多于一个恒星时，如果地球离其中一个很近的话，之后可能会围绕着该恒星运动。

3.当木星质量与太阳相当时，改变木星的初始速度对地球的运动影响很大。  

## 致谢
- 计算物理（第二版），清华大学出版社；
- 本文参考了团长同学的作业报告，万分感谢！
