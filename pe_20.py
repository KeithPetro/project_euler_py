#Project Euler - 20
#Keith Petro - 2016/10/20
#Problem Name: Factorial digit sum
#Description: Find the sum of the digits in the number 100!

def factorial(n):
	factorial = 1
	for i in range(1, n + 1):
		factorial *= i

	return factorial

def get_sum_of_digits(num):
	return sum([int(i) for i in str(num)])

print(get_sum_of_digits(factorial(100)))