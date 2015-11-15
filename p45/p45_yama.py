#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

def solve(S,T):
	if(S==[]):
		return T

	if(S[0]==S[len(S)-1]):
		Srv = S[:]
		Srv.reverse()
		if(S<=Srv):
			T.append(S[0])
			S.pop(0)
		else:
			T.append(S[len(S)-1])
			S.pop(len(S)-1)
	elif(S[0]<S[len(S)-1]):
		T.append(S[0])
		S.pop(0)
	else:
		T.append(S[len(S)-1])
		S.pop(len(S)-1)

	return solve(S,T)

if __name__ == '__main__':
	#input	
	Sin = []
	Tin = []
	N = int(raw_input())	
	str = raw_input()
	Sin=list(str)

	print solve(Sin,Tin)

