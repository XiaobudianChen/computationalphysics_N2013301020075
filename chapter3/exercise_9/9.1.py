import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *

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
        plt.plot(self.t,self.theta,color,label="F=$%.1f$"%(self.FD))

figure(figsize=(8,6), dpi=80)
A=CHAOS(0,0.2,0.04,60,0,0.5,0.,2./3.)
B=CHAOS(0,0.2,0.04,60,0,0.5,0.5,2./3.)
C=CHAOS(0,0.2,0.04,60,0,0.5,1.2,2./3.)
A.calculate()
B.calculate()
C.calculate()
A.plot('b-',label="F=$0.5$")
B.plot('r-',label="F=$0.5$")
C.plot('g-',label="F=$1.2$")
plt.xlim(0,60)
plt.xlabel("time(s)")
plt.ylabel("$\Theta$(radians)")
plt.title("driven_pendulum")
plt.legend(fontsize=9,loc='best')

plt.show()