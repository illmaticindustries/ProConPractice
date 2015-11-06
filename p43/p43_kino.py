# -*- coding:utf-8 -*-

def read_input(file_name):
	S = []
	T = []
	f = open(file_name, "r")
	N = int(f.readline())
	#input s
	for n in range(N):
		S.append(int(f.readline()))
	#input t
	for n in range(N):
		T.append(int(f.readline()))
	f.close()
	S_,T_ = sort_input(N,S,T)
	return N,S_,T_

def sort_input(N,S,T):
	S_buff = []
	for s in S:
		S_buff.append(s)
	S_buff.sort()
	T_buff = []
	for s_buff in S_buff:
		n = S.index(s_buff)
		T_buff.append(T[n])
		S.pop(n)
		T.pop(n)
	return S_buff,T_buff


def choose_next(s_now,N,S,T):
	#next t -> s
	n_now = S.index(s_now)
	t_now = T[n_now]
	t_min = 10**9
	n_min = 100000
	for n in range(N):
		if T[n] > t_now and T[n] < t_min and S[n] > t_now:
			t_min = T[n]
			n_min = n
	s = S[n_min]
	return s

def append_schedule(s_now,schedule,N,S,T):
	t_now = T[S.index(s_now)]
	if s_now > T[N-1] or s_now >= S[N-1] or t_now > S[N-1]:
		return schedule
	else:
		s_next = choose_next(s_now,N,S,T)
		schedule.append(s_next)
		if s_next >  T[N-1] or s_next >= S[N-1]: 
			return schedule
		else:
			append_schedule(s_next,schedule,N,S,T)

def make_schedules(N,S,T):
	schedules = []
	for s in S:
		schedule = []
		schedule.append(s)
		append_schedule(s,schedule,N,S,T)
		schedules.append(schedule)
	return schedules

def decide_schedule(schedules,N):
	len_schedule = []
	for n in range(N):
		len_schedule.append(len(schedules[n]))
	max_schedule = max(len_schedule)
	act_schedule = len_schedule.index(max_schedule)
	print schedules[act_schedule]

def test(file_name):
	N,S,T = read_input(file_name)
	S.sort()
	T.sort()
	schedules = make_schedules(N,S,T)
	decide_schedule(schedules,N)

test("p43.in")
test("p43_1.in")
test("p43_2.in")
test("p43_3.in")
