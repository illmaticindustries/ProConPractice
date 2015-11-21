# -*- coding:utf-8 -*-
"""
cube puzzzle like TSUMIKI

"""
import numpy

def read_input(file_name):
    f = open(file_name,'r')
    N =int(f.readline())
    parts = []
    for part in f:
	parts.append(part.rstrip('\n'))
    return N,parts

def test(file_name):
    N,parts = read_input(file_name)
    print N,parts

test('cube.in')
