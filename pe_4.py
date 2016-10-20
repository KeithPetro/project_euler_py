#Project Euler - 4
#Keith Petro - 2016/10/20
#Problem Name: Largest palindrome product
#Description: Find the largest palindrome nade from the product
#of two 3-digit numbers.

#A palindrome can be written as ABCCBA
#This can be written as 100000A + 10000B + 1000C + 100C + 10B + A
#This can then be written as 100001A + 10010B + 1100C
#Factoring out 11, we see that the palindrome must be a multiple of 11
#This means that at least one of the two multipliers must be divisible by 11

def get_max_palindrome():
	for i in range(9, -1, -1):
		a = i * 100001
		for j in range(9, -1, -1):
			b = a + j * 10010
			for k in range(9, -1, -1):
				c = b + k * 1100
				for x in range(990, 98, -11):
					if(c % x == 0):
						y = c / x
						if(y < 1000):
							return c

print(get_max_palindrome())