#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
	#input	
	ans = 0
	L = []
	N = int(raw_input())	
	for i in range(N):
		L.append(int(raw_input()))
	
	L.sort()
	L.reverse()
	for k in range(N-1):
		ans = ans + L.pop(0)
		for j in range(len(L)):
			ans = L[j] + ans

	print ans
