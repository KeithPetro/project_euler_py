#Project Euler - 9
#Keith Petro - 2016/10/20
#Problem Name: Special Pythagorean triplet
#Description: There exists exactly one Pythagorean triplet for which
#a + b + c = 1000. Find the product abc.

#Using Euclid's formula: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
#This is a naive solution that assumes the result is a primitive triple

from math import sqrt

def get_abc():
	for m in range(2, int(sqrt(500))): #m(m+n) == 1000. If m == n, max m needed is sqrt(m)
		for n in range(1, m):
			a = m ** 2 - n ** 2
			b = 2 * m * n
			c = m ** 2 + n ** 2
			if(a + b + c == 1000):
				return a * b * c

print(get_abc())