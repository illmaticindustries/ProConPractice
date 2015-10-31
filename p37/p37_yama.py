#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys


def bfs(r,c):
	for dx in [-1,1]:
		dy = 0
		nx = c + dx
		ny = r + dy
		if (0 <= nx and nx < int(max_col) and 0<= ny and ny < int(max_raw)):
		#if(warr[ny][nx] == "#"):
				
			if(warr[ny][nx] == "G"):
				return "goal"
			elif(warr[ny][nx] == "."):
				buf.append([ny,nx])

	for dy in [-1,1]:
		dx = 0
		nx = c + dx
		ny = r + dy
		if (0 <= nx and nx < int(max_col) and 0<= ny and ny < int(max_raw)):
		#if(warr[ny][nx] == "#"):
				
			if(warr[ny][nx] == "G"):
				return "goal"
			elif(warr[ny][nx] == "."):
				buf.append([ny,nx])


	

if __name__ == '__main__':

	max_raw = raw_input()
	max_col = raw_input()
	warr = []
	s_raw = 0
	s_col = 0
	for i in range(0,int(max_raw)):
		try:
			arr = list(raw_input())
			if ("S" in arr):
				s_raw = i
				s_col = arr.index("S")
			warr.append(arr)
		except (EOFError):
			break

	q = []
	buf = []
	goal = 1
	q.append([s_raw,s_col])
	while (True):
		r = q[0][0]
		c = q[0][1]
		q.pop(0)

		warr[r][c] = "#"

		str = bfs(r,c)
		if (str == "goal"):
			print str	
			break
		if (len(q) == 0):
			goal+=1
			q = q + buf
			del buf[:]
