# def print_digits(n):
# 	while n > 0:
# 		print(n%10)



# def print_digits(n):
#     while n > 0:
#         print(n % 10)

# num = 312
# print_digits(num)


def print_digits(n):
    if (n == 0):
        return
    print_digits(n // 10)
    print(n % 10, end=" ")



num = int(input("Enter any number: "))
print_digits(num)
