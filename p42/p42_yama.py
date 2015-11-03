#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys



if __name__ == '__main__':
	
	#input	
	c = []
	v = [1,5,10,50,100,500]

	for i in range(6):
		c.append(int(raw_input()))
	a = int(raw_input())
	ans = []

	for j in range(5,-1,-1):
		ans.append(min(a / v[j],c[5 - j]))
		a -= ans[5 - j] * v[j]
	print " 1yen : %d  5yen : %d  10yen : %d  50yen : %d  100yen : %d  500yen : %d" %(ans[5],ans[4],ans[3],ans[2],ans[1],ans[0])

