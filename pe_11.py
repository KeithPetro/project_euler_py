#Project Euler - 11
#Keith Petro - 2016/10/20
#Problem Name: Largest product in a grid
#Description: What is the greatest product of four adjacent numbers
#in the same direction (up, down, left, right or diagonally) in the 20*20 grid?

import csv

#content is stored in pe_11_content.txt
with open('pe_11_content.txt') as f:
	reader = csv.reader(f, delimiter=' ')
	content = list(reader)

def get_largest_product(adj_nums):
	largest_product = 0

	for i in range(0, len(content) - 3):
		for j in range(0, len(content) - 3):
			test_product = int(content[i][j]) * int(content[i + 1][j + 1]) * int(content[i + 2][j + 2]) * int(content[i + 3][j + 3])
			if(test_product > largest_product):
				largest_product = test_product

		for j in range(3, len(content)):
			test_product = int(content[i][j]) * int(content[i + 1][j - 1]) * int(content[i + 2][j - 2]) * int(content[i + 3][j - 3])
			if(test_product > largest_product):
				largest_product = test_product

		for j in range(0, len(content)):
			test_product = int(content[i][j]) * int(content[i + 1][j]) * int(content[i + 2][j]) * int(content[i + 3][j])
			if(test_product > largest_product):
				largest_product = test_product

	for i in range(3, len(content)):
		for j in range(3, len(content)):
			test_product = int(content[i][j]) * int(content[i - 1][j - 1]) * int(content[i - 2][j - 2]) * int(content[i - 3][j - 3])
			if(test_product > largest_product):
				largest_product = test_product

		for j in range(0, len(content) - 3):
			test_product = int(content[i][j]) * int(content[i - 1][j + 1]) * int(content[i - 2][j + 2]) * int(content[i - 3][j + 3])
			if(test_product > largest_product):
				largest_product = test_product
				
		for j in range(0, len(content) - 3):
			test_product = int(content[i][j]) * int(content[i][j + 1]) * int(content[i][j + 2]) * int(content[i][j + 3])
			if(test_product > largest_product):
				largest_product = test_product

	return largest_product
	
print(get_largest_product(4))