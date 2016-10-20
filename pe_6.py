#Project Euler - 6
#Keith Petro - 2016/10/20
#Problem Name: Sum square difference
#Description: Find the difference between the sum of the squares of
#the first one hundred natural numbers and the square of the sum.

def get_sum_of_squares(max):
	sum_of_squares = 0
	for i in range(1, max + 1):
		sum_of_squares += i * i

	return sum_of_squares

def get_square_of_sum(max):
	square_of_sum = sum(range(1, max + 1)) ** 2

	return square_of_sum

print(get_square_of_sum(100) - get_sum_of_squares(100))