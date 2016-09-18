#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import heapq
#from heapq import nlargest
#enque the stands within your fuel
def pushStands(start, fuel, A, hq):
	stand = int(A.pop(0))
	x = int(start + fuel)
	ans = 0
	#if stand within fuel, pop it and pop first one from B
	if stand <= x:
		gas = int(B.pop(0))
		heapq.heappush(hq,gas)
		return pushStands(start, fuel, A, hq)
	else:
		A.insert(0, stand)
		ans =  int(max(hq))
		return ans

if __name__ == '__main__':
	#input	
	N = int(raw_input())	
	L = int(raw_input())	
	P = int(raw_input())	
	A = raw_input().split(",") 
	B = raw_input().split(",") 
	hq = []
	pos = 0
	dis = 0
	
	for k in range(N):
		dis =  pushStands(pos, P, A, hq)
		if dis >= L:
			break
		pos = pos + dis
	print k

