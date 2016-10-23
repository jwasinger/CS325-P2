#!/usr/bin/env python

'''
Divide and Conquer Coin Change Algorithm

To make change for A cents, start by letting K = A.
If there is a K-cent coin, then that one coin is the minimum.
Otherwise, for each value i < k,
     1. Find the minimum number of coins needed to make i cents
	 2. Find the minimum number of coins needed to make K - i cents
Choose the i that minimizes the sum of 1 and 2

A = amount to make
V = list of denominations
'''

'''
Work in progress
'''
def divideConquer(V,A):
	coinMin = A
	listMin = [0] * len(V)
	
	loop = range(0,len(V))

	for i in loop:
		if (V[i] <= A):
			listTemp, coinsTemp = divideConquer(V, A - V[i])
			coinsTemp += 1
			listTemp[i] += 1				

			if coinMin > coinsTemp:
				coinMin = coinsTemp
				listMin = listTemp

	return listMin, coinMin

def readFile(file):
	with open(file) as f:
		lines = f.readline().replace('[','').replace(']','').rstrip('\n').strip(',')
		lines2 = int(f.readline())
	lines = map(int,lines.split(','))
	return lines, lines2

def writeFile(listMin,coinMin,file):
	newFile = file + "change.txt"
	with open(newFile,"w") as f:
		f.write(str(listMin))
		f.write('\n')
		f.write(str(coinMin))

def main():
	file = raw_input("Enter a file name: ")
	V,A = readFile(file)
	listMin,coinMin = divideConquer(V,A)
	writeFile(listMin,coinMin,file)
	print listMin
	print coinMin

if __name__ == "__main__": main()
