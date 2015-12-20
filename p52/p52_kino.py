# -*- coding:utf-8 -*-
dp = []

def read_input(file_name):
    f = open(file_name)
    N = int(f.readline())
    W = int(f.readline())
    w_v =[]
    for l in f:
        l = l.rstrip('\n').split(',')
        w = int(l[0])
        v = int(l[1])
        w_v.append([w,v])
    f.close()

    return N,W,w_v

def rec(i,j,N,W,w_v):
    global dp

    if dp[i][j] >= 0:
        return dp[i][j]

    res = 0
    if i == N:
        res = 0
    elif j < w_v[i][0]:
        res = rec(i+1,j,N,W,w_v)
    else:
        res = max(rec(i+1,j,N,W,w_v), rec(i+1,j-w_v[i][0],N,W,w_v)+w_v[i][1])
    dp[i][j] = res
    return dp[i][j]

def test(file_name):
    N,W,w_v = read_input(file_name)
    global dp
    dp_n = []
    dp_w = -1
    for n in range(N+1):
        for w in range(W+1):
            dp_n.append(dp_w)
        dp.append(dp_n)
        dp_n = []
    print rec(0,W,N,W,w_v)

    

test('p52.in')
