#Project Euler - 2
#Keith Petro - 2016/10/20
#Problem Name: Even Fibonacci numbers
#Description: By considering the terms in the Fibonacci sequence
#whose values do not exceed four million, find the sum of the
#even-valued terms.

def get_fib_sequence_even_sum(limit):
	previous_fib = 1
	current_fib = 2
	fib_sum = 0
	while(current_fib <= 4000000):
		if(current_fib % 2 == 0):
			fib_sum += current_fib

		current_fib = previous_fib + current_fib
		previous_fib = current_fib - previous_fib

	return fib_sum
	
print(get_fib_sequence_even_sum(4000000))