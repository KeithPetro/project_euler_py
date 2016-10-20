#Project Euler - 1
#Keith Petro - 2016/10/20
#Problem Name: Multiples of 3 and 5
#Description: Find the sum of all the multiples of 3 or 5 below 1000

#Go through multiples of num_1 and num_2 only, and then subtract the common multiples
def find_mults(num_1, num_2, limit):
	num_1_start = num_1
	num_2_start = num_2
	cross_mult_num = num_1 * num_2
	cross_mult_num_start = cross_mult_num
	sum_of_mults = 0

	while(num_1 < limit):
		sum_of_mults += num_1
		num_1 += num_1_start

	while(num_2 < limit):
		sum_of_mults += num_2
		num_2 += num_2_start

	while(cross_mult_num < limit):
		sum_of_mults -= cross_mult_num
		cross_mult_num += cross_mult_num_start

	return sum_of_mults

#Using S = n(n+1)/2 Gaussian summation
def find_mults_2(num_1, num_2, limit):
	cross_mult = num_1 * num_2
	max_num_1 = ((limit - 1) // num_1) * num_1
	max_num_2 = ((limit - 1) // num_2) * num_2
	max_cross_mult = ((limit - 1) // cross_mult) * cross_mult

	sum_of_mults =  max_num_1 * (max_num_1 + num_1) // (2 * num_1) + \
		  max_num_2 * (max_num_2 + num_2) // (2 * num_2) - \
		  max_cross_mult * (max_cross_mult + cross_mult) // (2 * cross_mult)

	return sum_of_mults

#Go through all numbers less than limit and check each for divisibility
def find_mults_3(num_1, num_2, limit):
	sum_of_mults = 0
	for i in range(1, limit):
		if(i % 3 == 0 or i % 5 == 0):
			sum_of_mults += i

	return sum_of_mults

print(find_mults_2(3, 5, 1000))