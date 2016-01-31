# -*- coding:utf-8 -*-

n_ = 0
W_ = 0
L_ = 0

#input data
def read_input(file_name):
    f = open(file_name,'r')
    n = int(f.readline())
    W = int(f.readline())
    L = [] 
    list_temp =[]
    lines = f.readlines()

    for l in lines:
        list_temp = l.rstrip('\n').split(',')
        w=int(list_temp[0])
        v=int(list_temp[1])
        L.append([w,v])
    
    global n_
    n_= n
    global W_
    W_ = W
    global L_
    L_ = L

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

def solve():
    dp = [[0]*(W_+1)]*(n_+1)
    
    for i in range(n_-1,-1,-1):
        
        for j in range(W_+1):
            print i,j
            if j<L_[i][0]:
                dp[i][j]=dp[i+1][j]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j-L_[i][0]]+L_[i][1])
    print dp[0][W_]
    print dp
    

# main_test function
def test(file_name):
    read_input(file_name)
    print n_,W_,L_
    #print rec(0,W_)
    print solve()
    #solve 
test('p52.in')
test('p52_1.in')

