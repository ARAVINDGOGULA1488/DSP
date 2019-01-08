#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:22:03 2019

@author: chenna
"""

import numpy as np
x=input("Enter the matrix A as [[a,b],[c,d]]:")
y=np.linalg.inv(x)
print x
print y