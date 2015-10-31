#-*-coding:utf-8-*-
N = 0
M = 0
solve = []

def read_input(file_name):
	f = open(file_name,"r")
	#N,M:row,column
	f_N = int(f.readline())
	f_M = int(f.readline())
	f_input = []
	for line in f:
		l = []
		for m in range(f_M):
			l.append(line[m])
		f_input.append(l)
	return f_N,f_M,f_input

def find_start(maze_input):
	for n in range(N):
		for m in range(M):
			if maze_input[n][m] == "S":
				return n,m

def find_que(que,p):
	for q in que:
		if q == p:
			return True
	return False

def find_next(count,que,p,maze_input):
	global solve
	p_u = [p[0]-1,p[1]]
	p_d = [p[0]+1,p[1]]
	p_l = [p[0],p[1]-1]
	p_r = [p[0],p[1]+1]
	que.append(p)
	if p_u[0] >= 0:           
		if maze_input[p_u[0]][p_u[1]] == "G":
			solve.append(count + 1)
			print que
			return
		if maze_input[p_u[0]][p_u[1]] != "#" and not find_que(que,p_u):
			find_next(count+1,que,p_u,maze_input)
	if p_d[0] < N:
		if maze_input[p_d[0]][p_d[1]] == "G":
			solve.append(count + 1)
			print que
			return
		if maze_input[p_d[0]][p_d[1]] != "#" and not find_que(que,p_d):
			find_next(count+1,que,p_d,maze_input)
	if p_l[1] >= 0:
		if maze_input[p_l[0]][p_l[1]] == "G":
			solve.append(count + 1)
			print que
			return
		if maze_input[p_l[0]][p_l[1]] != "#" and not find_que(que,p_l):
			find_next(count+1,que,p_l,maze_input)
	if p_r[1] < M:
		if maze_input[p_r[0]][p_r[1]] == "G":
			solve.append(count + 1)
			print que
			return
		if maze_input[p_r[0]][p_r[1]] != "#" and not find_que(que,p_r):
			find_next(count+1,que,p_r,maze_input)
	return


def test(file_name):
	global N,M,solve
	solve = []
	f_N,f_M,maze_input = read_input(file_name)
	N = f_N
	M = f_M
	print N,M,maze_input
	n,m = find_start(maze_input)
	p0 = [n,m]
	q0 = []
	find_next(0,q0,p0,maze_input)
	print solve


test("p37.in")
test("p37_2.in")
test("p37_3.in")
test("p37_4.in")
