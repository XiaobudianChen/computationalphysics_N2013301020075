"""
Spyder Editor

This is a script file for exercise 1.1 in Chapter 1.
"""
#python
from pylab import *
import pickle
#
v = []
t = []
g = 9.8
dt = float(input('time step='))
v.append(0)
t.append(0)
end_time=10
f=open('1.1.txt','w')
for i in range(int(end_time/dt)):
    v.append(v[i]-g*dt)
    t.append((i+1)*dt)
    print t[-1],v[-1]
    print >> f,t[-1],v[-1]
f.close() 
   
plot(t,v)
legend(('t','v'))
title('problem 1.1',fontsize=20)
xlabel('t/s')
ylabel('v')
savefig('1.1.png')
show()
