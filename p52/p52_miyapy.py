# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name,'r')
    n = int(f.readline())
    W = int(f.readline())
    L = [] 
    list_temp =[]
    lines = f.readlines()

    for l in lines:
        l=l.rstrip('\n')
        list_temp = l.split(',')
        L.append(list_temp)
    
    return n,W,L

def solve(n,W,L):
    
    return sum

def func(num,id,sum,n,W,max):
    if sum + L[id][1] < W:
        max += L[id][2]
        func(num+1,id+1,sum,n,W,max)
    if sum + L[id][1] >W
        if id==n:
            func(num)
def test(file_name):
    n,W,L = read_input(file_name)
    print n,W,L
    #print solve(N,L)


test('p52.in')
