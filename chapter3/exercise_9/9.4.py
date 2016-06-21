# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:34:17 2016

@author: Administrator
"""

import numpy as np
import math
import matplotlib.pyplot as plt

g=9.8
l=9.8
class CHAOS():
    def __init__(self,_omg0,_theta0,_t0,_q,_FD,_Omega,_size=100.,_timelim=400.):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.q=_q
        self.FD=_FD
        self.Omega=_Omega
        self.timelim=int(round(_timelim))
        self.size=int(round(_size))
        self.dt=(2.*math.pi/self.Omega)/self.size
        self.time=(2.*math.pi/self.Omega)*self.timelim
        self.n=int(round(self.time/self.dt))
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
            
    def plot_Poincare(self,_ax):        # the Poincare section plot    
        self.theta_Poincare=[]
        self.omg_Poincare=[]
        self.t_Poincare=[]
        for i in range(int(np.round(self.timelim))):
            self.t_Poincare.append(self.t[(i+1)*self.size])
            self.omg_Poincare.append(self.omg[(i+1)*self.size])
            self.theta_Poincare.append(self.theta[(i+1)*self.size])
        _ax.plot(self.theta_Poincare,self.omg_Poincare,'ob',markersize=2,label=r'$F_d = $'+' %.1f'%self.FD)
a=CHAOS(0,0.2,0,0.5,1.2,2./3.,100.,400.)
a.calculate()
ax=plt.subplot(111)
a.plot_Poincare(ax)
plt.xlabel(r"$\theta$(radians)")
plt.ylabel("$\omega$(radians/s)")
plt.title(r'$\omega$'+'   versus   '+r'$\theta$'+'   FD=1.2')

plt.show()