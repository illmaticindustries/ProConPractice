# -*- coding:utf-8 -*-

def read_input(file_name):
    f = open(file_name)
    N = int(f.readline())
    L = int(f.readline())
    p = int(f.readline())
    A = f.readline().rstrip('\n').split(',')
    B = f.readline().rstrip('\n').split(',')
    f.close()
    return N,L,p,A,B

def expedition(N,L,p,A,B):
    #init expected length l
    l = p
    count = 0
    for i in range(N):
        if l >= int(A[i]):
            l += int(B[i])
            count += 1    
        if l >= L:
            return count
    return -1

def test(file_name):     
    N,L,p,A,B = read_input(file_name)
    print expedition(N,L,p,A,B)    
    

test('p73.in')
