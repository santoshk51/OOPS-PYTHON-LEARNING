a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# print("Even data...")
# for i in range(a+1,b):
# 	# print(i, end=" ")
	
# 	if(i%2 == 0):
# 		print( i, end=" ")
	
# print("\nOdd data...")

# for i in range(a+1,b):
# 	# print(i, end=" ")
	
# 	if(i%2 != 0):
# 		print( i, end=" ")


# second method

even = []
odd = []

for i in range(a+1,b):
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)

print(even)
print(odd)

	