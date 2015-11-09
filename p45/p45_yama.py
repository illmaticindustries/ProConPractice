#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

def head(Scp,Tcp):
	if(len(Scp)==0):
		Alist.append(Tcp)
		return

	#head=foot
	if(Scp[0]==Scp[len(Scp)-1]):
		if(len(Tcp)==0):
			Tcp.append(Scp[0])
			Scp.pop(0)
		elif(Scp[0]<=Tcp[0]):
			Tcp.insert(0,Scp[0])
			Scp.pop(0)
		else:
			Tcp.append(Scp[0])
			Scp.pop(0)

	elif(Scp[0]<Scp[len(Scp)-1]):
		if(len(Tcp)==0):
			Tcp.append(Scp[0])
			Scp.pop(0)
		elif(Scp[0]<=Tcp[0]):
			Tcp.insert(0,Scp[0])
			Scp.pop(0)
		else:
			Tcp.append(Scp[0])
			Scp.pop(0)
	else:
		if(len(Tcp)==0):
			Tcp.append(Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)
		elif(Scp[len(Scp)-1]<Tcp[0]):
			Tcp.insert(0,Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)
		else:
			Tcp.append(Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)

	head(Scp,Tcp)
	foot(Scp,Tcp)
def foot(Scp,Tcp):
	if(len(Scp)==0):
		Alist.append(Tcp)
		return

	#head=foot
	if(Scp[0]==Scp[len(Scp)-1]):
		if(len(Tcp)==0):
			Tcp.append(Scp[0])
			Scp.pop(0)
		elif(Scp[len(Scp)-1]<=Tcp[0]):
			Tcp.insert(0,Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)
		else:
			Tcp.append(Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)

	elif(Scp[0]<Scp[len(Scp)-1]):
		if(len(Tcp)==0):
			Tcp.append(Scp[0])
			Scp.pop(0)
		elif(Scp[0]<=Tcp[0]):
			Tcp.insert(0,Scp[0])
			Scp.pop(0)
		else:
			Tcp.append(Scp[0])
			Scp.pop(0)
	else:
		if(len(Tcp)==0):
			Tcp.append(Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)
		elif(Scp[len(Scp)-1]<Tcp[0]):
			Tcp.insert(0,Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)
		else:
			Tcp.append(Scp[len(Scp)-1])
			Scp.pop(len(Scp)-1)

	head(Scp,Tcp)
	foot(Scp,Tcp)


if __name__ == '__main__':

	#input	
	Scp = []
	Tcp = []
	Alist = []
	N = int(raw_input())	
	str = raw_input()
	Scp=list(str)
	
	head(Scp,Tcp)
	foot(Scp,Tcp)

	Alist.sort()	
	print Alist[0]
