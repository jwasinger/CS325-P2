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

	for i in range(0, len(V)):
		if (V[i] <= A):
			listTemp, coinsTemp = divideConquer(V, A - V[i])
			coinsTemp += 1
			listTemp[i] += 1				

			if coinMin > coinsTemp:
				coinMin = coinsTemp
				listMin = listTemp

	return listMin, coinMin

def readFile(file):
	arr = []
	with open(file, 'r') as f:
		line = f.readline().split()
		for x in line:
			line = line.replace(']','').replace('[','').split(',')
	return line

def writeFile(arr):
	x = []

def main():
    A = 75
    V = [1, 5, 10, 25, 50]
    listMin,coinMin = divideConquer(V,A)
	print listMin
	print coinMin

if __name__ == "__main__": main()
