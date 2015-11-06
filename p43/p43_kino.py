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
	return N,S,T

def choose_next(s_now,N,S,T):
	#next t -> s
	n_now = S.index(s_now)
	t_now = T[n_now]
	t_min = 10**9
	for n in range(N):
		if T[n] > t_now and T[n] < t_min and S[n] > t_now:
			t_min = T[n]
	if t_min == 10**9:
		t_min = t_now
	n_min = T.index(t_min)
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
	len_work = T[N-1] - S[0]
	schedules = make_schedules(N,S,T)
	decide_schedule(schedules,N)

test("p43.in")
test("p43_1.in")
test("p43_2.in")
test("p43_3.in")
