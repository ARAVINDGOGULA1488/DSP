#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 02:38:58 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt
f1=input('enter a frequency of first wave')
f2=input('enter a frequency of second wave')
n=np.linspace(0,100,100)
y=np.sin(2*np.pi*n*f1)
z=np.sin(2*np.pi*f2*n)
x=y+z
fig=plt.figure()
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)
ax1=fig.add_subplot(3,1,1)
ax1.set_xlabel('----->time')
ax1.set_ylabel('Amplitude')
ax2=fig.add_subplot(3,1,2)
ax2.set_xlabel('----->time')
ax2.set_ylabel('Amplitude')
ax3=fig.add_subplot(3,1,3)
ax3.set_xlabel('----->time')
ax3.set_ylabel('Amplitude')
ax1.plot(n,y)
ax2.plot(n,z)
ax3.plot(n,x)
ax1.set_title("first wave")
ax2.set_title("second wave")
ax3.set_title("resultant wave")