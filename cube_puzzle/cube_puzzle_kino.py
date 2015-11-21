# -*- coding:utf-8 -*-
"""
cube puzzzle like TSUMIKI

"""
import numpy

class Parts(object):
    points = []
    def __init__(self,name):
	self.name = name
    def set(self,file_name):
	f = open(file_name,'r')
	for p in f:
	    self.points.append(p.rstrip('\n'))
	f.close()

def read_input(file_name):
    f = open(file_name,'r')
    #number of blocks
    N = int(f.readline())
    #one length of cube 
    M = int(f.readline())
    parts_files = []
    for parts in f:
	parts_files.append(parts.rstrip('\n'))
    f.close()
    return N,parts_files

def make_parts_dict(parts_names):
    dict_p = {}
    for name in parts_names:
	dict_p[name] = Parts(name)
    return dict_p

def set_parts_point(parts_dict,parts_list):
    for file_name in parts_list:
	name = file_name.rstrip('.in')
	parts_dict[name].set(file_name)

    

def test(file_name):
    N,parts_files = read_input(file_name)
    print N,parts_files
    #parts_colors = ['Clear','Yellow','Black','Red','Purple','White','Blue','Green']
    #print parts_colors
    parts_names = ['parts0','parts1','parts2','parts3','parts4','parts5','parts6','parts7']
    parts_dict = make_parts_dict(parts_names)
    print parts_dict
    set_parts_point(parts_dict,parts_files)


test('cube.in')
