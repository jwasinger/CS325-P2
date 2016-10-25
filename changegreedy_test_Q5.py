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
import time

def changegreedy(coinDenoms, changeToMake):
	#name = "changegreedy"
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
	
	return coinsUsed, coinsUsedSoFar#, name

def readFile(file):
	with open(file) as f:
		#remove list notation characters
		lines = f.readline().replace('[','').replace(']','').rstrip('\n').strip(',')
		#lines2 = int(f.readline())
	#remove commas
	lines = map(int,lines.split(','))
	return lines#, lines2

def writeFile(listMin, coinMin, file, runTime):
	#find file name and file extension
	base, ext = os.path.splitext(file)
	#keep just file name
	newFile = base + "change.txt"
	with open(newFile,"a") as f:
		#f.write(name + ":")
		#f.write('\n')
		#f.write(str(listMin))
		#f.write('\n')
		#f.write(str(coinMin))
		#f.write('\n')
		f.write(str(runTime) + '\n')
		
def main():
	#V = [1, 5, 10, 5, 50] 
	timeArr = []
	sum = 0
	file = "test_for_Q5.txt"
	V = readFile(file)
	#print V
	for i in range(2000, 2201):
		A = i
			#file = raw_input("Enter a file name: ")
			#V = readFile(file)
		
		start = time.time()
		listMin, coinMin = changegreedy(V, A)
		finish = time.time()
		
		runTime = finish - start
		timeArr.append(runTime)
		
		writeFile(listMin, coinMin, file, runTime)
	
	for i in range(200):
		sum += timeArr[i]
		avgTime = sum/len(timeArr)
		print "Times: " + str(timeArr)
		print "Avg Time: " + str(avgTime) + " secs\n"
	
		#print listMin
		#print coinMin
		
	timeArr = []
	sum = 0
	file = "Coin1.txt"
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
	
if __name__ == "__main__":
	main()