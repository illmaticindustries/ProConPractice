# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name)
    N = int(f.readline())
    W = int(f.readline())
    w_v =[]
    for l in f:
        l = l.rstrip('\n').split(',')l
        w = int(l[0])
        v = int(l[1])
        w_v.append([w,v])
    f.close()

    return N,W,w_v

def test(file_name):
    print read_input(file_name)

test('p52.in')
