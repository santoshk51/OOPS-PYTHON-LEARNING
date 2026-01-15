# 1) Open file in write mode and write 5 names
with open("names.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")

        file.write(name + "\n")

with open("names.txt", "r") as file:
    print("\nName in file:")
    print(file.read())

