#Project Euler - 17
#Keith Petro - 2016/10/20
#Problem Name: Number letter counts
#Description: If all the numbers from 1 to 1000 (one thousand) inclusive
#were written out in words, how many letters would be used?
#Do not count spaces or hyphens. The use of "and" is in compliance
#with British usage.

len_dict = {0: 0, \
			1: 3, \
			2: 3, \
			3: 5, \
			4: 4, \
			5: 4, \
			6: 3, \
			7: 5, \
			8: 5, \
			9: 4, \
			10: 3, \
			11: 6, \
			12: 6, \
			13: 8, \
			14: 8, \
			15: 7, \
			16: 7, \
			17: 9, \
			18: 8, \
			19: 8, \
			20: 6, \
			30: 6, \
			40: 5, \
			50: 5, \
			60: 5, \
			70: 7, \
			80: 6, \
			90: 6, \
			100: 7, \
			1000: 8, \
			'and': 3}

def get_sum_of_letters(limit):
	sum_of_letters = 0
	for i in range(1, limit + 1):
		ones = i % 10
		tens = ((i % 100) - ones) // 10
		hundreds = ((i % 1000) - tens * 10 - ones) // 100

		if(i == 1000):
			sum_of_letters += len_dict[1000] + len_dict[1]

		if(hundreds != 0):
			sum_of_letters += len_dict[hundreds] + len_dict[100]
			if(tens | ones != 0):
				sum_of_letters += len_dict['and']

		if(tens == 0 | 1):
			sum_of_letters += len_dict[tens * 10 + ones]
		else:
			sum_of_letters += len_dict[tens * 10] + len_dict[ones]
	return sum_of_letters

print(get_sum_of_letters(1000))