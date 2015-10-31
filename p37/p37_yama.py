#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys


def bfs(r,c):
	#search right,left
	for dx in [-1,1]:
		dy = 0
		nx = c + dx
		ny = r + dy
		if (0 <= nx and nx < int(max_col) and 0<= ny and ny < int(max_raw)):
				
			if(warr[ny][nx] == "G"):
				return "goal"
			elif(warr[ny][nx] == "."):
				buf.append([ny,nx])
	#search up,down
	for dy in [-1,1]:
		dx = 0
		nx = c + dx
		ny = r + dy
		if (0 <= nx and nx < int(max_col) and 0<= ny and ny < int(max_raw)):
				
			if(warr[ny][nx] == "G"):
				return "goal"
			elif(warr[ny][nx] == "."):
				buf.append([ny,nx])


	

if __name__ == '__main__':
	
	#input	
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
	#set start raw,col
	q.append([s_raw,s_col])
	
	rc = []
	r = 0
	c = 0
	#search loop
	while (True):
		#dequeue
		rc = q.pop(0)
		r = rc[0]
		c = rc[1]
		
		#mark already visit
		warr[r][c] = "#"

		#bfs
		str = bfs(r,c)
		
		#if arrive to goal, return answer
		if (str == "goal"):
			print str	
			break
		
		#if queue is empty, goal + 1 and enqueue next level
		if (len(q) == 0):
			goal+=1
			q = q + buf
			del buf[:]
