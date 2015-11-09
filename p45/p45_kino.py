#/opt/local/bin
# -*- coding:utf-8 -*-


alphabet = ['A','B','C','D','E',
			'F','G','H','I','J',
			'K','L','M','N','O',
			'P','Q','R','S','T',
			'U','V','W','X','Y','Z']

def read_input(file_name):
	f = open(file_name, 'r')
	N = int(f.readline())
	S = f.readline()
	return N,S

def cow_line(N,S):
	T = ""
	len_S = N
	for n in range(N):
		if len(T) == 0:
			""" first loop """
			T = T + S[0]
			S = S[1:]
			len_S = len_S - 1
			print S
			continue
		S_0 = S[0]
		S_f = S[len_S-1]
		T_0 = T[0]
		T_f = T[n-1]
		alpha_S_0 = alphabet.index(S_0)
		alpha_S_f = alphabet.index(S_f)
		alpha_T_0 = alphabet.index(T_0)
		alpha_T_f = alphabet.index(T_f)
		if alpha_S_0 >= alpha_S_f:
			""" append last to"""
			if alpha_T_0 > alpha_S_f:
				""" first """
				T = S_f + T
				S = S[:(len_S-1)]
				len_S = len_S - 1
				print n,T,S
			else:
				""" last """
				T = T + S_f
				S = S[:(len_S-1)]
				len_S = len_S - 1
				print n,T,S
		else:
			""" append first to"""
			if alpha_T_0 > alpha_S_0:
				""" first """
				T = S_0 + T
				S = S[1:]
				len_S = len_S - 1
				print n,T,S
			else:
				""" last """
				T = T + S_0
				S = S[1:]
				len_S = len_S - 1
				print n,T,S
	return T

def test(file_name):
	N,S = read_input(file_name)
	print N,S
	T = cow_line(N,S)
	print T

test('p45.in')
