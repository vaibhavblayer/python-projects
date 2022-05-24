# generating random Names
# random-names.py


import string
import random
import os
import sys

n = int(sys.argv[1])

def rnames(n):
	names = []
	for i in range(n):
		fletter = random.choice(string.ascii_uppercase)
		name = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(2, 8))) 
		names.append(fletter + name)

	return names


# print(rnames(100))


with open('names.txt', 'w') as names:
	nameList = rnames(n)
	for i in range(n):
		names.write('insert into tableone(name, address) values(\'{0}\', {1});\n'.format(nameList[i], random.randint(1, 600)))
