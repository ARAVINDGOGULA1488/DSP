#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 03:39:22 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt
f=input('enter the frequency')
F=input('enter the sample frequency')
m=np.linspace(0,100,100)
n=np.linspace(0,100,50)
x=np.sin(2*np.pi*(float(f))*m)
y=np.sin(2*np.pi*(float(f)/float(F))*n)
fig=plt.figure()
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)
ax1=fig.add_subplot(2,1,1)
ax1.set_xlabel('----->time')
ax1.set_ylabel('Amplitude')
ax2=fig.add_subplot(2,1,2)
ax2.set_xlabel('----->time')
ax2.set_ylabel('Amplitude')
ax1.plot(m,x)
ax2.stem(n,y)
ax1.set_title("sine wave")
ax2.set_title("sampled sine wave")