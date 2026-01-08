words = ["apple", "banana", "kiwi", "cherry", "mango"]

count_length = {word : len(word) for word in words}

print(count_length)


#another way
# count_length = {}

for word in words:
	count_length[word] = len(word)

# print(count_length)
	