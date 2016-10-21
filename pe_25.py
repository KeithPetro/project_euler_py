#Project Euler - 25
#Keith Petro - 2016/10/20
#Problem Name: 1000-digit Fibonacci number
#Description: What is the index of the first term in the Fibonacci sequence to contain
#1000 digits?

def get_next_fib(prev_fib, current_fib):
	current_fib = prev_fib + current_fib

	return current_fib

def get_first_fib_index_with_n_digits(n):
	fibs = [1, 1]
	while(len(str(fibs[-1])) < n):
		fibs.append(get_next_fib(fibs[-2], fibs[-1]))

	return fibs.index(fibs[-1]) + 1

print(get_first_fib_index_with_n_digits(1000))