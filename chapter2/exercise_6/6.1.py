# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:33:46 2016

@author:chenzheng
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:25:55 2016

@author: ChenZheng
"""
from pylab import *
from math import *

g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
	next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
	global x,y        
	x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

a = cannon(flight_state(0, 0, 1000*cos(pi*30/180), 1000*sin(pi*30/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'r',label = r'$\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
a_final = x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*35/180), 1000*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'orange',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*40/180), 1000*sin(pi*40/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'yellow',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*45/180), 1000*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'g',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*50/180), 1000*sin(pi*50/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'blue',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*55/180), 1000*sin(pi*55/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='cyan',label=r'$\theta=55^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 1000*cos(pi*60/180), 1000*sin(pi*60/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='purple',label=r'$\theta=60^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

title('trajectory of cannon shell')
xlabel('x(km)')
ylabel('y(km)')
show()

