# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name,'r')
    N = int(f.readline())
    L = []
    for l in f:
	L.append(int(l.rstrip('\n')))
    f.close()
    return N,L

def test(file_name):
    N,L = read_input(file_name)
    print N,L

test('p49.in')

