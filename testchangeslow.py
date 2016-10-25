#!/usr/bin/env python

import time
import os
'''
Divide and Conquer Coin Change Algorithm

Let MC(k) represent the minimum number of coins required
to make change of amount K and then the options are:

    -Select 1st coin (value = v1). Now smaller problem is minimum
	number of coins required to make change of amount(k-v1)
	so call MC(k-v1)
	-Select 2nd coin (value = v1). Now smaller problem is minimum
	number of coins require to make change of amount (k-v2)
	so call MC(k-v2)
	-Likewise up to n
	-Select nth coin (value=vn). Now smaller problem is minimum number 
	of coins required to make change of amount (k-vn) so call MC(k-vn)
	
Select the min from the smaller problems and add 1 because a coin is 
selected. Smaller problems will be solved recursively.

A = amount to make
V = list of denominations
'''
def divideConquer(V,A):
	name = "Divide & Conquer"
	coinMin = A
	listMin = [0] * len(V)
	
	#for each denomination in the list
	loop = range(0,len(V))

	for i in loop:
		if (V[i] <= A):
			listTemp, coinsTemp,dummyName = divideConquer(V, A - V[i])
			#increment counts
			coinsTemp += 1
			listTemp[i] += 1				

			#find min coin
			if coinMin > coinsTemp:
				coinMin = coinsTemp
				listMin = listTemp

	return listMin, coinMin, name

def readFile(file):
	with open(file) as f:
		#remove list notation characters
		lines = f.readline().replace('[','').replace(']','').rstrip('\n').strip(',')
		lines2 = int(f.readline())
	#remove commas
	lines = map(int,lines.split(','))
	return lines, lines2

def main():
	timeArr = []
	sum = 0
	file = raw_input("Enter a file name: ")
	V,A = readFile(file)
	for x in range(10):
		start = time.time()
		listMin,coinMin,algName1 = divideConquer(V,A)
		finish = time.time()
		runTime = finish - start
		timeArr.append(runTime)
		print listMin
		print coinMin
	for i in range(10):
		sum += timeArr[i]
	avgTime = sum/len(timeArr)
	print "Times: " + str(timeArr)
	print "Avg Time: " + str(avgTime) + " secs\n"

if __name__ == "__main__": main()