#Project Euler - 21
#Keith Petro - 2016/10/20
#Problem Name: Amicable numbers
#Description: Evaluate the sum of all the amicable numbers under 10000.

def get_proper_divisor_sum(num):
	proper_divisor_sum = 0

	i = 1
	while(i <= int(num ** 0.5) + 1):
		if(num % i == 0):
			proper_divisor_sum += i
			if(i != 1):
				proper_divisor_sum += num // i
		i += 1

	return proper_divisor_sum

def get_amicable_number_sum(limit):
	amicable_number_sum = 0
	for i in range(1, limit):
		i_sum = get_proper_divisor_sum(i)
		j_sum = get_proper_divisor_sum(i_sum)
		if((i == j_sum)):
			if(i != i_sum):
				#print('D(' + str(i) + ') = ' + str(i_sum) + ' and D(' + str(i_sum) + ') = ' + str(j_sum))
				amicable_number_sum += i_sum + j_sum

	return amicable_number_sum // 2 #to account for duplicates

print(get_amicable_number_sum(10000))