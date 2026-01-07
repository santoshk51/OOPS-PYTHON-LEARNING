def studentDictonary(student):
	while (True):
		print("\nMenu...")
		print("A - Add a student: ")
		print("B - Update marks: ")
		print("C - Search for a student: ")
		print("D - Display all students and marks: ")

		choice = input("Enter your Requirement: ").upper()

		match choice:
			case 'A':
				name = input("Enter student Name: ")
				marks = float(input("Enter Student marks: "))
				student[name] = marks
				print("Student details added Successfully!")
			
			case 'B':
				name = input("Enter Student name: ")
				if name in student:
					marks = float(input("Enter student updated marks: "))
					student[name] = marks
					print("Student marks updated successfulyy!")
				else:
					print("Student not found.")
			
			case 'C':
				name = input("Enter student name: ")
				if name in student:
					print("Student found!")
					print(name,":",student[name])
					
				else:
					print("Student not exist.")
			
			case 'D':
				for name, marks in student.items():
					print(name,":", marks)

			case _:
				print("Error")

					
			



student = {}

studentDictonary(student)

