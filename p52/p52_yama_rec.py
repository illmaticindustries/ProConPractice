#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

def rec(i, j, n):
	res = 0
	if(i == n):
		res = 0
	elif (j < int(w[i][0])):
		res = rec(i + 1, j, n)
	else:
		res = max(\
			rec(i + 1, j, n),\
			rec(i + 1, j - int(w[i][0]),n) + int(w[i][1]))
			
	
	return res


if __name__ == '__main__':
	#input	
	w = []
	N = int(raw_input())	
	W = int(raw_input())
	s = ''
	for i in range(N):
		s = raw_input()
		w.append(s.split(","))
	print rec(0, W, N)

