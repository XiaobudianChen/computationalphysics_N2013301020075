# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 2016

@author: ChenZheng
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 99, 100)
x_ave = np.zeros(100)
x_squ_ave = np.zeros(100)
x_y0 = np.zeros(100)
x = np.zeros(3000)
x_squ = np.zeros(3000)

for i in range(99):
    for j in range(3000):
        ruler = np.random.rand()
        if ruler<0.5:
            x[j] = x[j] + 1
        else:
            x[j] = x[j] - 1
            x_squ[j] = x[j]**2
    average = sum(x)/3000
    x_ave[i+1] = average
    average2 = sum(x_squ)/3000
    x_squ_ave[i+1] = average2    
       
fig=plt.figure(figsize=[11,5])
#x
ax=fig.add_subplot(1,2,1)
plt.scatter(steps,x_ave,c='yellow')
plt.plot(steps,x_y0)
plt.xlim(0,99)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x>')
plt.title('<x> of 3000 walkers')

#X^2
ax=fig.add_subplot(1,2,2)
para = np.polyfit(steps, x_squ_ave,2)
poly = np.poly1d(para)
y_fit = poly(steps)

plt.scatter(steps, x_squ_ave,s=2)
plt.plot(steps, y_fit, 'r', label = 'fit line')
plt.legend(loc='upper left')
plt.xlim(0,99)
plt.ylim(0,99)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x^2>')
plt.title('<x^2> of 3000 walkers')

plt.show()