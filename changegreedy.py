#!/usr/bin/env python

'''

   Algorithm 2: Greedy Algorithm
  
	A greedy algorithm always makes the choice that looks best at
	the moment (locally optimal choice).
	
	So here, given an amount of change needed to make from a set of available coin denominations, the greedy alorithm will always take as many of the largest coin demonination that does not exceed the sum of change needed (or the remaining sum of change), before then taking the next largest and so on.  This will arrive at a minimum number of coins to make the amount of change, for this algorithm.  But may not be the globally optimal minimum amount of coins to make change, depending on the coin denominations.
	
	A = amount of change to make
	V = an array with the possible coin denominations (sorted)
	C = an array with the toatal coins for each denomination
	m = minimum coins used to make change
	
'''

def changegreedy(coinDenoms, changeToMake):
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
	
	return coinsUsed, coinsUsedSoFar

def main():
	V = [1, 3, 7, 12] 
	A = 29
	
	C, m = changegreedy(V, A)
	
	print C
	print m
	
if __name__ == "__main__":
	main()