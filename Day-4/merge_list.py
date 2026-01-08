n = int(input("How many data do u want: "))

list1 = []
list2 = []
for i in range(n):
	list1.append(float(input("Enter 1st list number: ")))
for i in range (n):
	list2.append(float(input("Enter 2nd list number: ")))

result = list1 + list2

result.sort()

print("Sorted Lists: ",result)


even = []
odd = []
for i in result:
	if (i % 2 == 0):
		even.append(i)
	else:
		odd.append(i)

print("Even: ",even)
print("\n")
print("Odd: ",odd)