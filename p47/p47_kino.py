# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name,'r')
    N = int(f.readline())
    R = int(f.readline())
    X = []
    for x in f:
        X.append(int(x))
    return N,R,X

def test(file_name):
    N,R,X = read_input(file_name)
    print N,R,X

test('p47.in')
