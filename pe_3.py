#Project Euler - 3
#Keith Petro - 2016/10/20
#Problem Name: Largest prime factor
#Description: What is the largest prime factor of the number 600851475143?

def get_max_prime_factor(num):
	i = 2
	while(i * i < num):
		while(num % i == 0):
			num = num // i
		i += 1

	return num

print(get_max_prime_factor(600851475143))