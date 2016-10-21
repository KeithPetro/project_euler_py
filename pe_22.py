#Project Euler - 22
#Keith Petro - 2016/10/20
#Problem Name: Names scores
#Description: what is the total of all the name scores in the file pe_22_content.txt?

f = open('pe_22_content.txt', 'r')
content = f.read().replace('"', '').split(',')
content.sort()
f.close()

def char_to_value(char):
	return ord(char) - ord('A') + 1

def get_name_worth(name):
	name_worth = 0
	for letter in name:
		name_worth += char_to_value(letter)

	return name_worth

overall_name_score = 0
for name in content:
	name_score = get_name_worth(name)
	name_score *= content.index(name) + 1

	#print(name + ': ' + str(name_score))
	overall_name_score += name_score

print(overall_name_score)