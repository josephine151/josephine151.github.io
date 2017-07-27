from random import *

# list of first and last names
names = ["faith", "kathy", "sara", "aleef", "jesus", "lenny"]
last_names = ["smith", "johnson", "duggan", "doe", "riley", "brown"]

# list of names already used
names_used = []
last_names_used = []

#generate all names
for x in range(len(names)):
	# get 2 random numbers
	random_num1 = randint(0, len(names) - 1)
	random_num2 = randint(0, len(last_names) - 1)

	# get the name @randomnum index
	random_first = names[random_num1]
	random_last = last_names[random_num2]

	# if random first name was used, pick another
	while random_first in names_used:
		random_first = names[randint(0, len(names) - 1)]

	#if random last name was used, pick another
	while random_last in last_names_used:
		random_last = last_names[randint(0, len(last_names) - 1)]

	# add the names used to their lists
	names_used.append(random_first)
	last_names_used.append(random_last)

	# print the name
	print(random_first + " " + random_last)

	











