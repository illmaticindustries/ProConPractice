#/opt/local/bin
# -*- coding:utf-8 -*-


def read_input(file_name):
	f = open(file_name, 'r')
	N = int(f.readline())
	S = f.readline()
	return N,S

def test(file_name):
	N,S = read_input(file_name)
	print N,S

test('p45.in')
