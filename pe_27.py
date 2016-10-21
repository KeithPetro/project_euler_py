#Project Euler - 27
#Keith Petro - 2016/10/21
#Problem Name: Quadratic primes
#Description: Find the product of the coefficients, a and b, for the quadratic
#expression that produces the maximum number of primes for consecutive
#values of n, starting with n = 0.

#n^2 + an + b, |a| < 1000, |b| <= 1000
#b must be prime and a must be odd

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31] #cache of primes

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

def get_quadratic_prime_product(a_limit, b_limit):
	get_nth_prime(1000) #initialize primes list
	max_length = 0
	max_length_product = 0
	for a in range(a_limit - 1, -a_limit + 1, -2):
		for b in [i for i in primes if i <= 1000]:
			n = 0
			length = 0
			result = 2
			while(is_prime(result)):
				result = n ** 2 + a * n + b
				length += 1
				n += 1

			if(length - 1 > max_length):
				max_length = length - 1
				max_length_product = a * b

	return max_length_product

print(get_quadratic_prime_product(1000, 1000))