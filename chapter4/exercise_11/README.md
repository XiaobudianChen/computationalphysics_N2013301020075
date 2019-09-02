>## 第十一次作业
- 作业 4.7 4.9 4.11
> **5月12日的课程希望大家能按时上课，为物理学院的教学评估做出贡献！**

## 摘要
通过牛顿万有引力理论和双体模型研究了行星运动的轨迹等相关问题。  

## 背景介绍
行星运动的轨迹因其可以忽略空气阻力的影响而比较独特。一般来说只考虑引力相互作用，其轨迹为圆锥曲线（具体形式与初始条件有关）。我们可以胸万有引力出发来研究双星系统的运动特性。  

## 正文
由牛顿的万有引力方程，可以得出引力关系：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/公式1.png)

结合牛顿第二定律可以得出行星运动的轨迹方程。

考虑到太阳的有效质量引入折合质量u，![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/公式2.png)，来解决行星的二体问题。

通过积分我们可以求出行星的运动轨迹方程为

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/公式3.png)

其中：

- ![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/公式4.png)，
- e为运动轨道的离心率，e<1,则为椭圆轨道;e=1为抛物线轨道，e>1则为双曲线轨道

### 引力满足平方反比的双星轨迹
假设双星质量满足M1/M2=2，通过前面的操作，运用[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/11.1.py)，可以求出双星系统的运动轨迹图：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/figure_11.1.png)

可以看出初始条件不同时，二者的轨迹不一样，前者为同心圆，后者为相交椭圆，但是二者均可以稳定运动。
### 引力不满足平方反比的轨迹
假设万有引力不严格满足于平方反比定律，运动轨迹则与上面有很大不同，会发生进动等新的物理现象。

此时的运动满足方程：![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/公式5.png),其中a不等于2，而是在2附近的一个值。

分别假设β=a=2.05和1.95，运行[**程序**](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/11.2.py)对双星系统进行修正求解.

- β=2.05时，行星运动轨迹可能如下图所示：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/figure_11.2.png)

图中，（a）表明初始值合适，仍能形成稳定的圆轨道，（b）（c）则发生了行星运动轨迹偏离圆周，轨道不闭合，而是发生了进动，离心率越大，进动越明显，图（d）则给出了进动速率对离心率变化的规律。

- β=1.95时，行星运动轨迹如下图所示：
 
![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter4/exercise_11/figure_11.3.png)

我们可以看出，这时得到了与β=2.05同样的结论。其中图（a）展示了初始值一定的稳定圆轨道，图（b）（c）则展示了轨道的进动现象，图（d）则表示了轨道进动速率与离心率的关系。  
  
## 结论
当万有引力严格遵守平方反比定律时，行星的运动轨迹是严格的圆锥曲线，但是当其不严格遵守平方反比定律时，只在特定的情况下形成稳定的圆锥曲线轨迹，而大多数会出现圆轨道的进动现象，这有助于我们更好地了解和研究行星的运动和天文的预测。  
  
## 致谢
- 计算物理（第二版），清华大学出版社；
- 本文参考了[老王](https://github.com/Wangzhengwhu)的报告，在此感谢。
