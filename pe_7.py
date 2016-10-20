#Project Euler - 7
#Keith Petro - 2016/10/20
#Problem Name: 10001st prime
#Description: What is the 10001st prime number?

primes = [2, 3, 5, 7, 11, 13] #cache of primes

def is_prime(num): #this function only works providing all previous primes are populated in the primes list
	isprime = num >= 2 and 1 or 0

	for prime in primes:
		if prime * prime > num:
			break
		if(num % prime == 0):
			isprime = 0
			break

	return isprime

def get_nth_prime(n):
	i = primes[-1] #start at the last cached prime

	while(len(primes) < n):
		i += 1
		if(is_prime(i)):
			primes.append(i)

	return primes[n - 1]

print(get_nth_prime(10001))