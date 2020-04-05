import time

def evenGen(lower, upper):
	return [x for x in range(lower, upper) if x % 2 == 0]

def printList(list):
	for i in list:
		print(i)

def checkPrime(x):
	if(x <= 1):
		return False
	for i in range(2, x//2+1):
		if(x % i == 0):
			return False
	return True

def genPrimeList(lower, upper):
	oldNums = [x for x in range(lower, upper)]
	return filter(checkPrime, oldNums)

def findGoldbach(entry):
	for i in genPrimeList(0, entry):
		test = entry - i
		if(checkPrime(test)):
			print('{} + {} = {}'.format(i, test, entry))
			break

def sieve(size):
	primes = [True]*(size+1)
	outputPrimes = []

	primes[0] = False
	primes[1] = False

	for i in range(2, size):		#start at "number 2"
		for p in range(i**2, (size+1)):
			if p % i == 0:
				primes[p] = False

	for x in range(0, size):
		if primes[x] == True:
			outputPrimes.append(x)

	return outputPrimes

def findGoldbachSieve(entry):
	primes = sieve(entry)
	for i in primes:
		test = entry - i
		if(test in primes):
			print('{} + {} = {}'.format(i, test, entry))
			break


if __name__ == '__main__':
	start_time = time.time()
	for i in evenGen(2, 2000):
		findGoldbach(i)
	print("--- %s seconds ---" % (time.time() - start_time))

	start_time = time.time()
	for i in evenGen(2, 2000):
		findGoldbachSieve(i)
	print("--- %s seconds ---" % (time.time() - start_time))

