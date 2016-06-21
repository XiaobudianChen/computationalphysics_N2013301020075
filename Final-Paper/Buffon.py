# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 2016

@author: ChenZheng
"""

import random

a = input ("a=")
l = input ("l=")
step = input("step=")

m = 0
if a > 0 and l < a:
    for i in range(step):
        a = random.randint(0,60)
        b = random.randint(0,60)
    if abs(a-b)<=10:
        m += 1
    else:
        m = m
    print float(m)/step
else:
   print "You have input the wrong number!Please input a>0,l<a"
