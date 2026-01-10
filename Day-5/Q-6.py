from abc import ABC, abstractmethod

class Employee(ABC):
	@abstractmethod
	def cal_salary(self):
		pass

class intern(Employee):
	def __init__(self, salary):
		self.salary = salary

	def cal_salary(self):
		return self.salary
	
class FullTimeEmployee(Employee):
	def __init__(self, salary):
		self.salary = salary

	def cal_salary(self):
		return self.salary
	
class ContractEmployee(Employee):
	def __init__(self, Hour_worked, Hour_charged):
		self.Hour_charged = Hour_charged
		self.Hour_worked = Hour_worked

	def cal_salary(self):
		return self.Hour_charged * self.Hour_worked
	
it = intern(5000)
ft = FullTimeEmployee(37000)
ce = ContractEmployee(8,200)

print("Intern salary:",it.cal_salary())
print("FullTime Employee salary:",ft.cal_salary())
print("Contract employee salary:",ce.cal_salary())
		
		