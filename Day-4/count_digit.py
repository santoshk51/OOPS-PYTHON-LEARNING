def count_digits(n):
	count = 0
	if n == 0:
		return 1
	while n > 0:
		count += 1
		n = n // 10
	return count


num = int(input("Enter any number: "))

count_digits(num)
result = count_digits(num)

print(result)



