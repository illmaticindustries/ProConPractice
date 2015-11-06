#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys



if __name__ == '__main__':
	
	#input	
	s = []
	t = []
	w = []
	raw = int(raw_input())	
	work = 0

	for i in range(raw):
		s.append(int(raw_input()))
	for j in range(raw):
		t.append(int(raw_input()))
	
	ssort = s[:]
	tsort = t[:]
	ssort.sort()
	tsort.sort()
	time = 0
	idx = 0
	for k in range(raw):
		idx = t.index(tsort[0])
		tsort.pop(0)
		if(s[idx] > time):
			work += 1
			time = t[idx]
		
	print work
