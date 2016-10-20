#Project Euler - 5
#Keith Petro - 2016/10/20
#Problem Name: Smallest multiple
#Description: What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?

def get_smallest_multiple(max_divisor):
	product = 1
	for i in range(1, max_divisor + 1):
		if(product % i != 0):
			for j in range(1, max_divisor + 1):
				if(product * j % i == 0):
					product *= j
					break

	return product

print(get_smallest_multiple(20))