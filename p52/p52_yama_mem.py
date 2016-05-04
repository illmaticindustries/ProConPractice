#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

#dp = []
#dp = [[0 for m in range(W + 1)] for n in range(N + 1)]
def rec(i, j, n, dp):
	res = 0
	if(dp[i][j] != -1):
		return dp[i][j]
	if(i == n):
		res = 0
	elif (j < int(w[i][0])):
		res = rec(i + 1, j, n,dp)
	else:
		res = max(\
			rec(i + 1, j, n,dp),\
			rec(i + 1, j - int(w[i][0]),n,dp) + int(w[i][1]))
			
	
	dp[i][j] = res
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
	dp = [[-1 for m in range(W + 1)] for n in range(N + 1)]
	print rec(0, W, N,dp)

