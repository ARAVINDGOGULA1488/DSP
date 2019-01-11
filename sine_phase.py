#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 04:19:47 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
f=input('enter the frequency')
phi=input('enter the phase angle')
m=np.linspace(0,100,1000)
x=np.sin(2*np.pi*(float(f))*m)
y=np.sin((2*np.pi*(float(f))*m)+phi)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.plot(m,x)
ax2.plot(m,y)
ax1.set_title("sine wave")
ax2.set_title("shifted sine wave")