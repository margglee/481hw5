#!/usr/bin/env python
import sys
import os

def is_interesting(l):
	cov = 0
	sum = 0
	for i in range(0, 32000):
		for test in l:
			r = dataDict[test].get(i, 0)
			cov = cov or r
		if cov == 1:
			sum += 1
		cov = 0
	print(sum)
	print(sum/10606 * 100, 2)
	print(round(sum/10606 * 100, 2))
	if round(sum/10606 * 100, 2) >= 19.73:
		print("true")
		return 1
	return 0



def main():
	size_n = int(sys.argv[1])
	filename = sys.argv[2]
	global dataDict
	currentDirectory = os.getcwd()
	with open(currentDirectory + '/' + filename, 'r') as f:
		data = f.read()
		f.close()
	dataDict = eval(data)
	c = list(range(0, size_n))
	print(is_interesting(c))

if __name__== "__main__":
	main()
