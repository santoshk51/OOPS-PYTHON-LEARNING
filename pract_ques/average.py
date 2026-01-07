lists = [4, 5, 8, 9]

store = 0
count = 0

for i in lists:
	store += i
	count += 1

# print(store/count)

# optimized way

print(sum(lists) / len(lists))