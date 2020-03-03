#!/usr/bin/env python 

import sys
import os


def to_set(data):
	try:
		return set(data)
	except TypeError:
		return {data}


def union(l1, l2):
	return sorted(list(to_set(l1) | to_set(l2)))


def dd(p, c, cov):
	print("%s: dd(p=%s, c=%s)" % (sys.argv[0], p, c))
	if len(c) <= 1:
		return [c[0]]
	p1 = c[:len(c)//2]
	p2 = c[len(c)//2:]
	s1 = " ".join(str(i) for i in union(p, p1))
	s2 = " ".join(str(i) for i in union(p, p2))
	print("%s: calling %s %s" % (sys.argv[0], command, s1))
    res1 = float(os.system("%s %s" % (command, s1)))
	if res1 > cov:
        print(res1)
		return dd(p, p1, res1)
	print("%s: calling %s %s" % (sys.argv[0], command, s2))
    res2 = float(os.system("%s %s" % (command, s2)))
	if res2 > cov:
        print(res2)
		return dd(p, p2, res2)
	else:
        print(cov)
		return union(dd(union(p, p2), p1, cov), dd(union(p, p1), p2, cov))


def main():
	size_n = int(sys.argv[1])
	global command 
	command = " ".join(sys.argv[2:])
	c = list(range(0, size_n))
	result = dd(list(), c, 0)
	print(result)
    

if __name__== "__main__":
	main()
