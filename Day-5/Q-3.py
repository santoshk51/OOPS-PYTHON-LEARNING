class Student:
	def __init__(self, name, roll_no, marks):
		self._name = None
		self._roll_no = None
		self._marks = None

		self.name = name
		self.roll_no = roll_no
		self.marks = marks 

#Getter and Setter for Name
	@property  #Getter
	def name(self):
		return self._name 
	
	@name.setter  #Setter
	def name(self, value):
		if value.strip() != "":
			self._name = value
		else:
			print("Name cannot be empty")

	@property
	def rollNo(self):
		return self._roll_no
	
	@rollNo.setter
	def rolNo(self, value):
		if (1 <= value <= 100):
			self._roll_no = value
		else:
			print("Roll number must be btn 1 and 100")

	@property
	def Marks(self):
		return self._marks
	
	@Marks.setter
	def Marks(self, value):
		if value > 0:
			self._marks = value
		else:
			print("Marks cannot be negative")

s1 = Student("santosh", 98, 43.76)

print(s1.name)
print(s1.roll_no)
print(s1.marks)
