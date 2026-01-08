nums = [1, 2, 3, 2, 4, 1, 5, 3]

duplicates = []

for i in nums:
	if ( nums.count(i) > 1 and i not in duplicates):
		duplicates.append(i)
print(duplicates)

# another way
seen = set()
duplicates = set()

for i in nums:
	if i in seen:
		duplicates.add(i)
	else:
		seen.add(i)
		