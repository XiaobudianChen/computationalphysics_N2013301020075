# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:33:09 2016

@author: Administrator
"""

import numpy as np
import math
import matplotlib.pyplot as plt

g=9.8
l=9.8
class CHAOS():
    def __init__(self,_omg0,_theta0,_dt,_time,_t0,_q,_FD,_Omega):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.time=_time
        self.dt=_dt
        self.n=int(_time/_dt)
        self.q=_q
        self.FD=_FD
        self.Omega=_Omega
    def calculate(self):
        global g,l
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*math.sin(self.theta[-1])*self.dt-self.q*self.omg[-1]*self.dt+self.FD*math.sin(self.Omega*self.t[-1])*self.dt)
            if self.theta[-1]+self.omg[-1]*self.dt>math.pi:
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt-2*math.pi)
            elif self.theta[-1]+self.omg[-1]*self.dt<-math.pi:
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt+2*math.pi)
            else: 
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot(self,color,label):
        plt.plot(self.theta,self.omg,color,label="F=$%.1f$"%(self.FD))
        
        
fig=plt.figure(figsize=(10,6))
a1=plt.subplot(121)
a=CHAOS(0,0.2,0.04,100,0,0.5,0.5,2./3.)
a.calculate()
a.plot('b-',label="")
plt.xlabel(r"$\theta$(radians)")
plt.ylabel("$\omega$(radians/s)")
plt.title(r'$\omega$'+'   versus   '+r'$\theta$'+'   FD=0.5')

a2=plt.subplot(122)
a=CHAOS(0,0.2,0.04,200,0,0.5,1.2,2./3.)
a.calculate()
a.plot('b-',label="")
plt.xlabel(r"$\theta$(radians)")
plt.ylabel("$\omega$(radians/s)")
plt.title(r'$\omega$'+'   versus   '+r'$\theta$'+'   FD=1.2')

plt.show()