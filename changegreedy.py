#!/usr/bin/env python

'''

   Algorithm 2: Greedy Algorithm
  
	A greedy algorithm always makes the choice that looks best at
	the moment (locally optimal choice).
	
	So here, given an amount of change needed to make from a set of available coin denominations, the greedy alorithm will always take as many of the largest coin demonination that does not exceed the sum of change needed (or the remaining sum of change), before then taking the next largest and so on.  This will arrive at a minimum number of coins to make the amount of change, for this algorithm.  But may not be the globally optimal minimum amount of coins to make change, depending on the coin denominations.
	
	A = amount of change to make
	V = an array with the possible coin denominations (sorted)
	listMin = an array with the toatal coins for each denomination
	coinMin = minimum coins used to make change
	
'''

import sys
import os

def changegreedy(coinDenoms, changeToMake):
	name = "changegreedy"
	coinsUsed = []
	coinsUsedHere = 0
	coinsUsedSoFar = 0
	
	for coinValue in reversed(coinDenoms):
		#print coinValue
		#print changeToMake
		coinsUsedHere = changeToMake/coinValue
		coinsUsed.insert(0, coinsUsedHere)
		changeToMake = changeToMake - (coinsUsedHere * coinValue)
		coinsUsedSoFar = coinsUsedSoFar + coinsUsedHere
	
	return coinsUsed, coinsUsedSoFar, name

def readFile(file):
	with open(file) as f:
		#remove list notation characters
		lines = f.readline().replace('[','').replace(']','').rstrip('\n').strip(',')
		lines2 = int(f.readline())
	#remove commas
	lines = map(int,lines.split(','))
	return lines, lines2

def writeFile(listMin,coinMin,file,name):
	#find file name and file extension
	base, ext = os.path.splitext(file)
	#keep just file name
	newFile = base + "change.txt"
	with open(newFile,"a") as f:
		f.write(name + ":")
		f.write('\n')
		f.write(str(listMin))
		f.write('\n')
		f.write(str(coinMin))
		f.write('\n\n')
	
def main():
	#V = [1, 3, 7, 12] 
	#A = 31
	
	file = raw_input("Enter a file name: ")
	V,A = readFile(file)
	listMin, coinMin, algoName = changegreedy(V, A)
	writeFile(listMin,coinMin,file,algoName)
	
	print listMin
	print coinMin
	
if __name__ == "__main__":
	main()