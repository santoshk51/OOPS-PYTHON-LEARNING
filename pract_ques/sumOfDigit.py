def sumOfDigits(n):
	n = abs(n)
	sum1 = 0
	while n > 0:
		digit = n % 10
		sum1 += digit
		n //= 10
	return sum1

num = int(input("Enter any digits: "))

result = sumOfDigits(num)

print("the sum of Digit is: ", result)
