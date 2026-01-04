salary = int(input("Enter Salary: "))

if (salary < 30000):
	tax = salary * 0.05
elif (salary <= 70000):
	tax = salary * 0.15
else:
	tax = salary * 0.25

print("Tax Rate is: ", tax)