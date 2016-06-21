1# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 2016

@author: ChenZheng
"""

import random
import math

a = input ("a=")
l = input ("l=")
step = input("step=")

m = 0
if a > 0 and l < a:
    for i in range(step):
        x = random.random()*0.5*a
        phi = random.random()*math.pi
        if x <= 0.5*l*math.sin(phi):
            m += 1
        else:
            m = m    
    print float(m)/step
else:
   print "You have input the wrong number!Please input a>0,l<a"
