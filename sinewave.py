#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 06:49:03 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
f=input('enter the frequency')
m=np.linspace(0,100,100)
x=np.sin(2*np.pi*(float(f))*m)
plt.plot(m,x)
plt.ylabel("amplitde")
plt.xlabel("time")
plt.title('sinusoidal wave')