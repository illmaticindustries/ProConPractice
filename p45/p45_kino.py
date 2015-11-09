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
	S = f.readline().rstrip('\n')
	S = S.upper()
	f.close()
	return N,S

def cow_line(N,S):
	T = ''
	S_buff = ''
	len_S = N
	while len(S) > 0:
		if len(T) == 0:
			""" first loop """
			T = T + S[0]
			S = S[1:]
			print S
			continue
		S_0 = S[0]
		S_f = S[-1]
		T_0 = T[0]
		T_f = T[-1]
		alpha_S_0 = alphabet.index(S_0)
		alpha_S_f = alphabet.index(S_f)
		alpha_T_0 = alphabet.index(T_0)
		alpha_T_f = alphabet.index(T_f)
		if alpha_S_0 == alpha_S_f:
			S_buff = S_buff + S_0
			S = S[1:-1]
			continue
		elif alpha_S_0 > alpha_S_f:
			""" append last to last"""
			T = T + S_buff + S_f
			s = ''
			if S_buff != '':
				for n in range(len(S_buff)):
					s = S_buff[n] + s
			S = s + S
			S = S[:-1]
			S_buff = ''
			print T,S
		else:
			""" append first to last"""
			T = T + S_buff + S_0
			S = S + S_buff
			S = S[1:]
			S_buff = ''
			print T,S
	T = T + S_buff
	return T

def test(file_name):
	N,S = read_input(file_name)
	print N,S
	T = cow_line(N,S)
	print T

test('p45.in')
test('p45_1.in')
test('p45_2.in')
