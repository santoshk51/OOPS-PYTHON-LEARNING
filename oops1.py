class employee:
	def __init__(self):
		 # special method/ magic method/dunder method
		print("Started executing attributes/data")
		self.id = 123
		self.salary = 50000
		self.degination = "SDE"
		print("finished executing attributes/data")

	def travel(self, destination):
		print("manually called travel method")
		print(f"Employee is travelling to {destination}")

# create an object/instance of employee class
sk = employee()

sk.travel("karela")
		