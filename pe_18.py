#Project Euler - 18
#Keith Petro - 2016/10/20
#Problem Name: Maximum path sum I
#Description: Find the maximum total from the top to bottom of the triangle below (see site)

import csv

with open('pe_18_content.txt') as f:
	reader = csv.reader(f, delimiter=' ')
	content = list(reader)

for i in range(0, len(content)):
	for j in range(0, len(content[i])):
		content[i][j] = int(content[i][j])

def get_max_path(content):
	for i in range(len(content) - 1, -1, -1):
		next_row_index = 0
		for j in range(0, len(content[i]) - 1, 1):
			if(content[i][j] > content[i][j + 1]):
				content[i - 1][next_row_index] += content[i][j]
			else:
				content[i - 1][next_row_index] += content[i][j + 1]
			
			next_row_index += 1
	return content[0][0]

print(get_max_path(content))