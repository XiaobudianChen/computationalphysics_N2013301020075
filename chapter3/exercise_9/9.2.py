# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:31:29 2016

@author: Administrator
"""

import numpy as np
import math
import matplotlib.pyplot as plt

g=9.8
l=9.8
class CHAOS(object):
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
        plt.plot(self.t,self.theta,color,label="F=$%.1f$"%(self.FD))
class CHAOS_VIA(object):
    def __init__(self,_FD,_theta01=0.2,_theta02=0.2-1E-3):
        self.FD=_FD 
        self.theta0=[_theta01,_theta02]
    def calculate(self):
        self.cal=CHAOS(0,self.theta0[0],0.04,50,0,0.5,self.FD,2./3.)
        self.cal.calculate()
        self.t=self.cal.t
        self.theta1=self.cal.theta
        self.cal=CHAOS(0,self.theta0[1],0.04,50,0,0.5,self.FD,2./3.)
        self.cal.calculate()
        self.theta2=self.cal.theta
        self.theta=np.array(self.theta1)-np.array(self.theta2)
        self.theta=np.abs(self.theta)
    def plot_via(self,_ax):
        _ax.semilogy(self.t, self.theta,'-r')

fig=plt.figure(figsize=(10,6))
ax1=plt.subplot(121)
plt.title(r'$\Delta \theta$'+'  versus  '+r'time'+ '   FD=0.5',fontsize=10)
plt.xlabel('time(s)')
plt.ylabel(r'$\Delta \theta$(radians)')
ax2=plt.subplot(122)
plt.title(r'$\Delta \theta$'+'  versus  '+r'time'+ '   FD=1.2',fontsize=10)
plt.xlabel('time(s)')
plt.ylabel(r'$\Delta \theta$(radians)')
A=CHAOS_VIA(0.5)
A.calculate()
A.plot_via(ax1)
B=CHAOS_VIA(1.2)
B.calculate()
B.plot_via(ax2)

plt.show()