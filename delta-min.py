#!/usr/bin/env python

import sys
import os


def is_interesting(l):
    cov = 0
    sum = 0
    for i in range(0, 31881):
        for test in l:
            cov = cov or x[test].get(i, 0)
        if cov == 1:
            sum++
        cov = 0
    if round(sum/10606, 2) >= 37.97
        return 1

    return 0


def to_set(data):
	try:
		return set(data)
	except TypeError:
		return {data}


def union(l1, l2):
	return sorted(list(to_set(l1) | to_set(l2)))


def dd(p, c):
	print("%s: dd(p=%s, c=%s)" % (sys.argv[0], p, c))
	if len(c) <= 1:
		return [c[0]]
	p1 = c[:len(c)//2]
	p2 = c[len(c)//2:]
	l1 = union(p, p1))
	l2 = union(p, p2))
	print("%s: calling %s on %s" % (sys.argv[0], command, l1))
	if is_interesting(l1):
		return dd(p, p1)
	print("%s: calling %s on %s" % (sys.argv[0], command, l2))
	if is_interesting(l2):
		return dd(p, p2)
	else:
		return union(dd(union(p, p2), p1), dd(union(p, p1), p2))


def main():
	size_n = int(sys.argv[1])
	global command
	command = "is_interesting()"
	c = list(range(0, size_n))
	result = dd(list(), c)
	print(result)


if __name__== "__main__":
	main()
