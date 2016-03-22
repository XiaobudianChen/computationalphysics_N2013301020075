#python

v = []
t = []
g = 9.8
#input
dt = float(input('time step='))
v.append(0)
t.append(0)
end_time=10
#calculation
f=open('chapter one 1.1.txt','w')
for i in range(int(end_time/dt)):
    v.append(v[i]-g*dt)
    t.append((i+1)*dt)
    print t[-1],v[-1]
    print >> f,t[-1],v[-1]
f.close()    
#plot
plot(t,v)
legend(('t','v'))
title('problem 1.1',fontsize=20)
xlabel('t/s')
ylabel('v')
savefig('chapter one 1.1.png')
show()    
