user = str(input("Enter any string: "))

seen = set()
duplicates = set()
count = 0
for ch in user:
	if ch in seen:
		duplicates.add(ch)
	else:
		seen.add(ch)
		count += 1
print(seen)
print(count)