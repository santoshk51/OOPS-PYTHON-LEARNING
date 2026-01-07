list1 = [1, 2, 3, 4]
list2 = [5, 4, 7, 8]

# Check for common elements
if set(list1) & set(list2):
    print("Lists share common elements")
else:
    print("Lists share NO common elements")
