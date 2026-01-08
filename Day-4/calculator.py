def calulator(a, b, operations):
	match operations:
		case '+':
			print("Sum: ",a+b)
		case '-':
			print("Neg: ",a-b)
		case '*':
			print("mul: ",a*b)
		case '/':
			print("Div: ",a/b)
		case '%':
			print("mod: ",a%b)
		case _ :
			return "Invalid Operator"
		

a = float(input("Enter 1st Number: "))
operations = input("Enter operation: ")
b = float(input("Enter 2nd Number: "))


result = calulator(a,b,operations)

	 