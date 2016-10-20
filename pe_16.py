#Project Euler - 16
#Keith Petro - 2016/10/20
#Problem Name: Power digit sum
#Description: What is the sum of the digits of the number 2^1000?

def get_sum_of_digits(num):
	num_str = str(num)
	digit_sum = sum([int(i) for i in num_str])

	return digit_sum

print(get_sum_of_digits(2 ** 1000))