#Project Euler - 14
#Keith Petro - 2016/10/20
#Problem Name: Longest Collatz sequence
#Description: Which starting number, under one million, produces the
#longest chain?

calculated_lens = []
calculated_starters = []
def get_collatz_len(num):
	i = 1
	while(num != 1):
		if num in calculated_starters:
			i += calculated_lens[calculated_starters.index(num)]
			return i
		elif(num % 2 == 0):
			num //= 2
			i += 1
		else:
			num = int(3 * num + 1)
			i += 1
	return i

def get_longest_collatz(limit):
	max_starter = 0
	max_len = 0
	for i in range(1, limit + 1):
		i_collatz_len = get_collatz_len(i)
		if(max_len <= i_collatz_len):
			max_len = i_collatz_len
			max_starter = i

	return max_starter

print(get_longest_collatz(1000000))
