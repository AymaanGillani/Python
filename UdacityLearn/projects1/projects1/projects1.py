import random

word_file = "words.txt"
word_list = []

with open(word_file,'r') as words:
	for line in words:
		word = line.strip().lower()
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
	return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())