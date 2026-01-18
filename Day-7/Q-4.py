import json

with open("cities.json", "r") as f:
	cities = json.load(f)

for city, population in cities.items():
	print(city,":",population)

new_city = input("Enter new city name: ")
new_population = int(input("Enter population: "))

cities[new_city] = population


with open("cities.json", "w") as file:
	json.dump(cities, file, indent=4)

print("JSON file updated successfully!")