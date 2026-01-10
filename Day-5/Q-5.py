class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

class car(Vehicle):
	def __init__(self, brand, model, seat):
		super().__init__(brand, model)
		self.seat = seat

class Bike(Vehicle):
	def __init__(self, brand, model, engine):
		super().__init__(brand, model)
		self.engine = engine

c = car("TATA", "THAR", "A1")

b = Bike("Bullet", "n71", "bukati")

print("car seat : ",c.seat)
print("Bike engine: ",b.engine)
