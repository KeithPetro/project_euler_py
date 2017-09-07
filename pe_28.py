#Project Euler - 28
#Keith Petro - 2016/10/21
#Problem Name: Number spiral diagonals
#Description: What is the sum of the numbers on the diagonals in a 1001*1001
#spiral formed in the same way? (see site)

#diff = 0|size = 1
#       2|       3
#       4|       5
#       6|       7
#     ...|     ...
#As can be seen from this pattern, diff = size - 1
#For each layer we go out, we add 4 new values, each diff apart

def get_diagonal_sum_of_spiral(size):
	sum_of_diagonal = 0
	previous_num = 0
	for i in range(1, size + 1, 2):
		diff = i - 1
		if(diff == 0):
			sum_of_diagonal += 1
			previous_num = 1
		else:
			for j in range(1, 4 + 1):
				sum_of_diagonal += previous_num + diff
				previous_num += diff

	return sum_of_diagonal

print(get_diagonal_sum_of_spiral(1001))
