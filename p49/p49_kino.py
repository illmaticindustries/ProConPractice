# -*- coding:utf-8 -*-
"""
    L_1 =< L_2 =< ... =< L_N
    cost = sum_1 + sum_2 + ... + sum_N-1

    sum_1 = L_1 + L_2 + ... + L_N
    sum_2 = L_1 + L_2 + ... + L_N-1
    .
    .
    .
    sum_N-1 = L_1 + L_2

"""


def read_input(file_name):
    f = open(file_name,'r')
    N = int(f.readline())
    L = []
    for l in f:
	L.append(int(l.rstrip('\n')))
    f.close()
    L.sort()
    return N,L

def solve(N,L):
    sum = 0
    #in case len(L) > 2
    while len(L) > 2:
	for l in L:
	    sum = sum + l
	L.pop()
    
    #in case len(L) = 2
    for l in L:
	sum = sum + l
    return sum

def test(file_name):
    N,L = read_input(file_name)
    print N,L
    print solve(N,L)

test('p49.in')
test('p49_1.in')
test('p49_2.in')
