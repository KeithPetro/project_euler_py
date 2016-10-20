#Project Euler - 12
#Keith Petro - 2016/10/20
#Problem Name: Highly divisible triangular number
#Description: What is the value of the first triangle number to have over
#five hundred divisors?

def get_factor_count(num):
	factor_count = 0

	i = 1
	while(i <= int(num ** 0.5) + 1):
		if(num % i == 0):
			factor_count += 2
		i += 1

	return factor_count

def get_first_tri_num_with_n_factors(n): #I know, what a function name
	num_factors = 0
	tri_num_index = 1
	current_tri_num = 0
	while(num_factors < n):
		current_tri_num += tri_num_index
		num_factors = get_factor_count(current_tri_num)
		tri_num_index += 1

	return current_tri_num

print(get_first_tri_num_with_n_factors(500))