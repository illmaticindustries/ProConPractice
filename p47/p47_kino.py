# -*- coding:utf-8 -*-
# not correct answer

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
    """
    L : maximum length in X
    O : length for covering N nodes 
    """
    L = X[-1]-X[0]
    O = R*(N-1)
    M = (L/R)-1
    if L > O:
        return N 
    elif M > N:
        return N -1
    else:
        return M
    
def test(file_name):
    N,R,X = read_input(file_name)
    #print N,R,X
    print calc(N,R,X)

test('p47.in')
test('p47_1.in')
test('p47_2.in')
test('p47_3.in')
