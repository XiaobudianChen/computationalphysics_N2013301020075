>## 第四次作业
- 完成第一章的练习题（自己任选一题）
- 使用matplotlib完成图片的各种细节，认真写报告

*（第一次作业写在作业部落上，后来被自己不小心删除了，重写于此）*

##摘要
运用*Euler*法计算近地面自由落体运动的速度与时间的关系，并作图分析。
##背景介绍
近地面自由落体运动的速度*v*与时间*t*的关系满足下式：

![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_4/公式1.png)
这里加速度满足![](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_4/公式2.png).
##正文
###算法设计
首先由Euler法设计出源代码，即把常微分方程化差分方程并由此写出程序框架；
然后由待解常微分方程写出程序具体形式,为[1.1.py](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_4/1.1.py)。
###参数设置
由题，加速度已设，假设近地面自由落体初速度v=0,时间由t=0到t=10s。
###程序实现及作图
取时间间隔为0.1s,运行完整程序,可以得出算得的[近似解1.1.txt](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_4/1.1.txt)。

并利用matplotlib库作出相应近似解，图示如下。![图1.1.png](https://raw.githubusercontent.com/XiaobudianChen/computationalphysics_N2013301020075/master/chapter1/exercise_4/1.1.png)
##结论
可以看出，由Euler法所得的近似解与理论上的精确求解值吻合度极高，很好地得出了近地面自由落体运动的速度与时间的线性关系图像。
##致谢
本人编程小白，感谢[团长](https://github.com/Tuanzhang0531)的程序支持！
