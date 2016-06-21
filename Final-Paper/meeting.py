# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 2016

@author: ChenZheng
"""
import random

step = input("step=")
m = 0
for i in range(step):
    a = random.randint(0,60)
    b = random.randint(0,60)
    if abs(a-b)<=10:
        m += 1
    else:
        m = m
print float(m)/step