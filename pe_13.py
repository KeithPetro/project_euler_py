#Project Euler - 12
#Keith Petro - 2016/10/20
#Problem Name: Large sum
#Description: Work out the first ten digits of the sum of the following
#one-hundred 50-digit numbers.

#open file to get numbers
f = open('pe_13_content.txt', 'r')
content = f.read().split('\n')
f.close()

def get_sum(num_list):
	large_sum = 0
	for i in range(0, len(content)):
		large_sum += int(content[i])

	return str(large_sum)[0:10]

print(get_sum(content))