class Laptop:
	storage_type = "ssd"

	def __init__(self, RAM, storage):
		self.RAM = RAM
		self.storage = storage

	def get_info(self):
		print(f"Laptop has {self.RAM} RAM & {self.storage} storage {self.storage_type} type")

l1 = Laptop("16GB", "512GB")
l2 = Laptop("8GB", "256GB")
l1.get_info()
