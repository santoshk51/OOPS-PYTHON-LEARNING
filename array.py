# import array as arr
from array import *

val = array('b',[1,2,3,4,5,6,7,8,9,10])

for i in range(0,len(val)):
	print(val[i], end = " ")

print("\n")

for x in val:
	print(x, end = " ")

print('\n')

print(val.typecode)
print(val.reverse())

for i in range(0, len(val)):
	print(val[i], end = " ")

print('\n')

val.insert(2,50)

for i in range(0, len(val)):
	print(val[i], end = " ")


copyArr = array(val.typecode , (x*2 for x in val))



copyArr.pop()


# for i in range(0, len(copyArr)):
# 	print(copyArr[i], end = " ")

newArr = val[::-1]

# for i in range(0, len(newArr)):
# 	print(newArr[i], end = " ")

arrCreate = array('i' , [])

n = int(input("Enter any number: "))

for i in range(0, n):
	arrCreate.append(int(input("Enter the Data: ")))

for x in arrCreate:
	print(x, end=" ")