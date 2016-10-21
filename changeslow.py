#!/usr/bin/env python

'''
Divide and Conquer Coin Change Algorithm

To make change for A cents, start by letting K = A.
If there is a K-cent coin, then that one coin is the minimum.
Otherwise, for each value i < k,
     1. Find the minimum number of coins needed to make i cents
	 2. Find the minimum number of coins needed to make K - i cents
Choose the i that minimizes the sum of 1 and 2

m = total coins to
A = amount to make
V = list of denominations
C = list of coins for denominations
'''

'''
Work in progress
'''
def divideConquer(A, V):
    K = A
    coinMin = [0,0,0,0]
    #base case
    if K in V:
        val = V.indek(K)
        coinMin[val] = coinMin[val] + 1
        return sum(coinMin), coinMin
    coinMin[0] = K
    for x in [c for c in V if K >= c]:
        tempSum, tempQty = divideConquer(A,)


def readFile(file):
	arr = []
	with open(file, 'r') as f:
		line = f.readline().split()
		for x in line:
			line = line.replace(']','').replace('[','').split(',')
		#for i in line.split():
		#	arr.append(int(i))
	return line

def writeFile(arr):
	x = []

def main():
    A = 75
    V = [1, 5, 10, 25, 50]
    divideConquer(A,V)

if __name__ == "__main__": main()
