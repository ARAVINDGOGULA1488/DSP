#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 02:14:12 2019

@author: rgukt
"""

a=input('enter no.of rowsof matrix 1: ')
b=input('enter no. of columns of matrix 1: ')
c=input('enter no.of rowsof matrix 2: ')
d=input('enter no. of columns of matrix 2: ')
if (b==c):
	p={ }
	for i in range (0,a,1):
		for j in range (0,b,1):
			p[i,j]=input('enter a number for matrix 1: ')
	q={ }
	for m in range (0,c,1):
		for n in range (0,d,1):
			q[m,n]=input('enter a number for matrix2:')

	r={ }
	for i in range (0,a,1):
		for j in range (0,d,1):
			r[i,j]=0
	for i in range (0,a,1):
		for j in range (0,d,1):
			for x in range (0,b,1):
				r[i,j]=r[i,j]+p[i,x]*q[x,j]
	print r
else :
	 print'matrix multiplication is not possible'