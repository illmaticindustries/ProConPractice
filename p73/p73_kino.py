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
    use = [p]
    can_use = []
    for i in range(N):
        if l + sum(can_use) >= int(A[i]):
            can_use.append(int(B[i]))
            while l - int(A[i]) <= 0:
                use.append(max(can_use))
                can_use.remove(max(can_use))
                l = sum(use)
        if l >= L:
            count = len(use) - 1
            return count
    while l - L <= 0:
        use.append(max(can_use))
        can_use.remove(max(can_use))
        count = len(use) - 1
        return count
    return -1

def test(file_name):     
    N,L,p,A,B = read_input(file_name)
    return expedition(N,L,p,A,B)    
    
def test_check(file_name, act_ans):
    my_ans = test(file_name)
    print file_name
    if my_ans == act_ans:
        print 'OK'
    else:
        print my_ans, 'is NG'

test_check('p73.in',2)
test_check('p73_2.in',2)
test_check('p73_3.in',3)

