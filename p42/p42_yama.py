#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys



if __name__ == '__main__':
	
	#input	
	c1 = int(raw_input())
	c5 = int(raw_input())
	c10 = int(raw_input())
	c50 = int(raw_input())
	c100 = int(raw_input())
	c500 = int(raw_input())
	A = int(raw_input())
	rest = A
	u1 = 0
	u5 = 0
	u10 = 0
	u50 = 0
	u100 = 0
	u500 = 0
	while(c500 > 0 and rest >= 500):
		rest = rest - 500
		u500 += 1
		c500 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) +  " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) +  " 100 : " + str(u100) + " 500 : " + str(u500) 
	while(c100 > 0 and rest >= 100):
		rest = rest - 100
		u100 += 1
		c100 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) + " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) + " 100 : " + str(u100) + " 500 : " + str(u500) 
	while(c50 > 0 and rest >= 50):
		rest = rest - 50
		u50 += 1
		c50 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) + " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) + " 100 : " + str(u100) + " 500 : " + str(u500) 
	while(c10 > 0 and rest >= 10):
		rest = rest - 10
		u10 += 1
		c10 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) + " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) + " 100 : " + str(u100) + " 500 : " + str(u500) 
	while(c5 > 0 and rest >= 5):
		rest = rest - 5
		u5 += 1
		c5 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) + " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) + " 100 : " + str(u100) + " 500 : " + str(u500) 
	while(c1 > 0 and rest >= 1):
		rest = rest - 1
		u1 += 1
		c1 -= 1
		if(rest == 0):
			print " 1 : " + str(u1) + " 5 : " + str(u5) + " 10 : " + str(u10) +  " 50 : " + str(u50) + " 100 : " + str(u100) + " 500 : " + str(u500) 
	
	

