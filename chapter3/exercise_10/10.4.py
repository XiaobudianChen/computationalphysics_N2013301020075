# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color):
        plt.plot(self.t,self.z,color,label='r=$%.1f$'%self.r)
plt.figure(figsize=(8,8))
ax1=plt.subplot(211)
A=Position(160)
A.calculate()
A.plot('k-')
plt.title('Lorenz model,z vetsus time,r=160')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,30)
plt.legend(loc='upper right')

ax2=plt.subplot(212)
B=Position(163.8)
B.calculate()
B.plot('k-')
plt.title('Lorenz model,z vetsus time,r=163.8')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,30)
plt.legend(loc='upper right')

plt.show()