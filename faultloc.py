#!/usr/bin/env python 
import math
import sys
import os
import re

def main():
    lineDict = {}
    ochiaiLst = []
    totalFail = 0
    for i in range(1, len(sys.argv)):
        mPass = re.match('pass[0-9]+.gcov', sys.argv[i])
        mFail = re.match('fail[0-9]+.gcov', sys.argv[i])
        if (mPass):
            #print(sys.argv[i])
            with open(sys.argv[i]) as file:
                line = file.readline()
                while (line):
                    line = file.readline()
                    r = re.findall('([0-9]+\:\s[0-9]+)\:', line)
                    if len(r) > 0:
                        r2 = r[0].split(":")
                        #numRun = int(r2[0])
                        lineNum = r2[1].strip()
                        inDict = lineDict.get(lineNum, None)
                        if inDict != None:
                            lineDict[lineNum][0] += 1
                        else:
                            lineDict[lineNum] = [1, 0]
                        
        if (mFail):
            totalFail += 1
            #print(sys.argv[i])
            with open(sys.argv[i]) as file:
                line = file.readline()
                while (line):
                    line = file.readline()
                    r = re.findall('([0-9]+\:\s[0-9]+)\:', line)
                    if len(r) > 0:
                        r2 = r[0].split(":")
                        #numRun = int(r2[0])
                        lineNum = r2[1].strip()
                        inDict = lineDict.get(lineNum, None)
                        if inDict != None:
                            lineDict[lineNum][1] += 1
                        else:
                            lineDict[lineNum] = [0, 1]

    for k in lineDict.keys():
        ochiaiVal = lineDict[k][1]/math.sqrt(totalFail * (lineDict[k][0] + lineDict[k][1]))
        ochiaiLst.append((int(k),ochiaiVal))
    ochiaiLst.sort()
    ochiaiLst.sort(key = lambda x: x[1], reverse=True) 
    if len(ochiaiLst) > 100:
        print(ochiaiLst[:100])
    else:
        print(ochiaiLst)
if __name__== "__main__":
	main()