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


def dd(p, c):
	#print("%s: dd(p=%s, c=%s)" % (sys.argv[0], p, c))
	if len(c) <= 1:
		return [c[0]]
	p1 = c[:len(c)//2]
	p2 = c[len(c)//2:]
	s1 = " ".join(str(i) for i in union(p, p1))
	s2 = " ".join(str(i) for i in union(p, p2))
	#print("%s: calling %s %s" % (sys.argv[0], command, s1))
	if os.system("%s %s" % (command, s1)):
		return dd(p, p1)
	#print("%s: calling %s %s" % (sys.argv[0], command, s2))
	if os.system("%s %s" % (command, s2)):
		return dd(p, p2)
	else:
		return union(dd(union(p, p2), p1), dd(union(p, p1), p2))


def main():
	size_n = int(sys.argv[1])
	global command
	command = " ".join(sys.argv[2:])
	c = list(range(0, size_n))
	result = dd(list(), c)
	print(result)


if __name__== "__main__":
	main()
