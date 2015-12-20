# -*- coding:utf-8 -*-

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
        
    return n,W,L

#saiki
def func(num,id,sum,sum_v,n,W,L,max):
    print num,id,max
    if num==n-1:
        print "end" 
        return max

    if sum + L[id][0] <= W:
        if id<n-1:
            sum += L[id][0]
            sum_v+=L[id][1]
            if (max<sum_v):
                max = sum_v 
            return func(id,id+1,sum,sum_v,n,W,L,max)
        else:
            sum += L[id][0]
            sum_v+=L[id][1] 
            if (max<sum_v):
                max = sum_v  
            return func(num+1,num+2,sum-L[num][0],sum_v-L[num][1],n,W,L,max)
            
    if sum + L[id][0] > W:
        if id==n-1:
            return func(num+1,num+2,sum-L[num][0],sum_v-L[num][1],n,W,L,max)
        else:
            return func(num,id+1,sum,sum_v,n,W,L,max)
    

# main_test function
def test(file_name):
    n,W,L = read_input(file_name)
    print n,W,L
    print L[3][1]
    print func(0,1,L[0][0],L[0][1],n,W,L,0)

#solve 
test('p52.in')
test('p52_1.in')
