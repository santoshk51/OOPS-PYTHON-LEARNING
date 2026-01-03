x = int("10")
# print(type(x))

y = str(25)
# print(type(y))

txt = "python"


txt.lower()
# print(txt.upper())
# print(text[1:5])
l = "ot"
print(txt.replace("pyth", "jio"))
print(txt.startswith(l))

t = "hello world with chai"
print(t.split())
print(t.find("ai"))

## operation in python

a = 10
b = 21
print(b ** a)


# comparison operations

y = 20
z = 33

f = x == y
f1 = x != y
f2 = x > y
f3 = x < y
f4 = x >= y
f5 = x <= y

# print(f)
# print(f1)
# print(f2)
# print(f3)
# print(f4)
# print(f5)


# Membership & Identity operators

# lst = [1,2,3,4,5]
# lst1 = [1,2,3,4,5]
# x =5

# print(lst is not lst1)

# name  = input("Enter your name: ")
# print("Hello", name)

#Type conversion

# age = int(input("Enter your age: "))
# price = float(input("Enter the price: "))
# print(age,"", price)

# result = 10 + 2 * 3 # Multiplication happens first: 10 + (2 * 3) = 16
# print(result)
# result = (10 + 2) * 3 # Parentheses first: (10 + 2) * 3 = 36
# print(result)
# result = 2 ** 3 ** 2 # Right-to-left exponentiation: 2 ** (3 ** 2) = 2 ** 9 = 512
# print(result)

## sets


## defining an empty set

# set_var = set()
# If else statements
# t2 = 10
# if x <= 5:
# 	print("T1 is greater than 5")
# else:
# 	print("x is not greatr=er than 5")

u1 = 5
if u1 > 10:
	print("x is greater than 10")
elif u1 > 5:
	print("x is greater than 5 but not more than 10")
elif u1 == 5:
	print("x is exactally 5")
else:
	print("x is less than 5")


# Using if else in data science

age = 33
if age < 18:
	category = "Minor"
elif age >= 18 and age < 65:
	category = "Adult"
else:
	category = "senior citizen"

print("category:", category)

# tuple

tup = (2,3,4,1)

print(type(tup))
print(tup[0])
print(tup.count(4))
# tup[0] = 5 # error

tupl = [1,2,3,2,1]


tup11 = (1.0)
print(tup11)
print(type(tup11))

# tup[0] = 43

# tup1 = ()

# tup2 = (1,)
# tup3 = (1,2,3)

my_list = []
# user1 = input("Enter your fav movie: ")
# user2 = input("Enter your fav movie: ")
# user3 = input("Enter your fav movie: ")

# my_list.append(user1)
# my_list.append(user2)
# my_list.append(user3)
# print(my_list)

# another way

movies = []

# movies.append(input("Enter your 1st Movie: "))
# movies.append(input("Enter your 2st Movie: "))
# movies.append(input("Enter your 3st Movie: "))

print(movies)

#palidrome or not

palid = [1,2,3,2,1]

plad1 = palid.copy()

plad1.reverse()
# if plad1 == palid:
# 	print("yes")
# else:
# 	print("not")

# agecheck = int(input("Enter the Age: "))


# if (agecheck < 13):
# 	print("Minor")
# elif (agecheck >=13 and agecheck < 18):
# 	print("Teneger")
# elif (agecheck < 65 and agecheck >= 18):
# 	print("Adult")
# else:
# 	print("Senior Citizen")

userName = input("Enter Username: ")
userPass = input("Enter pass: ")

if (userName ==  "admin" and userPass == "pass"):
	print("Login succeed!")
else:
	if (userName != "admin"):
		print("Wrong userName")
	else:
		print("password is wrong")


phrase = "artificial intelligence"
count = 0
for ch in phrase:
	
	if (ch == "i"):
		count += 1
print("count is ", count)
