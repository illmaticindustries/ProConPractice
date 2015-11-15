#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
	#input	
	X = []
	C = []
	ans = 0
	N = int(raw_input())	
	R = int(raw_input())	
	for i in range(N):
		X.append(int(raw_input()))
	
	X.sort()

	for j in range(N):
		if(j==0 or X[j-1] < (X[j] - R)):
			if(j == N-1 or (X[j+1] > (X[j] + R))):
				if(X[j] not in C):
					C.append(X[j])
					ans += 1
			else:
				C.append(X[j+1])
				ans += 1
		elif(X[j] > (C[len(C)-1] + R)):
			if(j == N-1 or (X[j+1] > (X[j] + R))):
				if(X[j] not in C):
					C.append(X[j])
					ans += 1
	print ans
	print C
