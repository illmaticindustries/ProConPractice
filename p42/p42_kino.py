#-*-coding:utf8-*-
C1 = 1
C5 = 5
C10 = 10
C50 = 50
C100 = 100
C500 = 500

coins = [C500, C100, C50,C10, C5, C1]

def read_input(file_name):
	f = open(file_name,"r")
	#[c1,c5,c10,c50,c100,c500,A]
	f_input = []
	for line in f:
		f_input.append(int(line))
	return f_input

def payment(change,amount):
	flag = False
	for c in coins:
		if amount >= c:
			cn = coins.index(c)
			for m in range(cn,len(change)):
				if change[m] > 0:
					flag = True
					amount = amount - coins[m]
					change[m] = change[m] - 1
					break
		if flag:
			break
	if amount != 0:
		payment(change,amount)
	else:
		return 

def calc_payment(money,change):
	pay = 0
	for n in range(6):
		pay = pay + money[n] - change[n]
	return pay

def test(file_name):
	f_input = read_input(file_name)
	amount = f_input.pop()
	money = list(reversed(f_input))
	change = list(reversed(f_input))
	payment(change,amount)
	pay = calc_payment(money, change)
	print pay

test("p42.in")
test("p42_1.in")
