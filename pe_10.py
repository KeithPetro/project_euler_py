#Project Euler - 10
#Keith Petro - 2016/10/20
#Problem Name: Summation of primes
#Description: Find the sum of all the primes below two milliion.

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

def get_prime_sum_less_than_n(n):
	i = primes[-1] #start at the last cached prime

	while(primes[-1] < n):
		i += 1
		if(is_prime(i)):
			primes.append(i)

	return sum(primes[0:-1])

print(get_prime_sum_less_than_n(2000000))