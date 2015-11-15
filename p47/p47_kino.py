# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name,'r')
    N = int(f.readline())
    R = int(f.readline())
    X = []
    for x in f:
        X.append(int(x))
    X.sort()
    return N,R,X

def calc(N,R,X):
    L = X[-1] - X[0]
    M = L / R -1
    if M > N:
        return N
    else:
        return M
    
def test(file_name):
    N,R,X = read_input(file_name)
    #print N,R,X
    print calc(N,R,X)

test('p47.in')
