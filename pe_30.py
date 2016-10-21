#Project Euler - 30
#Keith Petro - 2016/10/21
#Problem Name: Digit fifth powers
#Description: Find the sum of all the numbers that can be written as the sum
#of fifth powers of their digits.

#9^5 = 59049
#59049 * n <= 10^n - 1 for n <= 6
#59059 * 6 = 354294

sum_of_numbers = 0
for i in range(2, 354294):
	i_str = str(i)
	sum_of_fifth_powers = 0
	for digit in i_str:
		sum_of_fifth_powers += int(digit) ** 5

	if(sum_of_fifth_powers == i):
		sum_of_numbers += i
		print(i_str + ' can be written as a sum of its fifth powers')

print(sum_of_numbers)