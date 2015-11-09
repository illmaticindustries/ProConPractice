#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys



if __name__ == '__main__':
	
	#input	
	S = []
	T = []
	N = int(raw_input())	
	str = raw_input()
	S=list(str)
	
	if(S[0] < S[len(S)-1]):
		T.append(S.pop(0))
	else:
		T.append(S.pop(len(S)-1))
	
	
	for j in range(N-1):
		if(S[0] < S[len(S)-1]):
			if(S[0]<T[0]):
				T.insert(0,S[0])
				S.pop(0)
			else:
				T.append(S[0])
				S.pop(0)
		else:
			if(S[len(S)-1]<T[0]):
				T.insert(0,S[len(S)-1])
				S.pop(len(S)-1)
			else:
				T.append(S[len(S)-1])
				S.pop(len(S)-1)
	print T
