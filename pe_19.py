#Project Euler - 19
#Keith Petro - 2016/10/20
#Problem Name: Counting Sundays
#Description: How many Sundays fell on the first of the month during the
#twentieth century (1 Jan 1901 to 31 Dec 2000)

import datetime

def get_sunday_count():
	sunday_count = 0
	for year in range(1901, 2000 + 1):
		for month in range(1, 12 + 1):
			if(datetime.date(year, month, 1).weekday() == 6):
				sunday_count += 1

	return sunday_count

print(get_sunday_count())