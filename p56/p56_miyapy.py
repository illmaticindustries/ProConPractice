# -*- coding:utf-8 -*-

#input data
def read_input(file_name):
    f = open(file_name,'r')
    n = int(f.readline())
    m = int(f.readline())
    s = f.readline().strip('\n')
    t = f.readline().strip('\n')
    
    return n,m,s,t

def rec(i,j):
    if dp[i][j]>=0:
        return dp[i][j]

    if i==n_-1:
        res = 0
    elif j<L_[i][0]:
        res = rec(i+1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-L_[i][0])+L_[i][1])

    dp[i][j] = res
    return res
   
def solve(n,m,s,t):

    
    # main_test function
def test(file_name):
    n,m,s,t = read_input(file_name)
    solve(n,m,s,t) 



test('p56.in')

