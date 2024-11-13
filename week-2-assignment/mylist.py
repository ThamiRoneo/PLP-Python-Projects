# declaring an empty list
my_list = []

# printing an empty list
print("my_list: ", my_list)

# appending elements to the list
my_list = [10, 20, 30, 40]

# printing the appended list
print("Appended my_list: ", my_list)

# insert the value 15 at the second position in the list
my_list.insert(1, 15)

# printing the list with the new element on the second position
print("my_list after inserting 15: ", my_list)

# extending my_list with another list
my_list.extend([50, 60, 70])

# printing the extended list
print("The extended my_list: ", my_list)

# removing the last element from the list
my_list.remove(my_list[-1])

# printing the list with the last element removed
print("List with the last element removed: ", my_list)

# sorting my_list in ascending order
my_list.sort()

# printing the sorted list
print("Sorted list: ", my_list)

# declaring the variable index
index = my_list.index(30)

# finding and printing the index for the value 30
print("The index of the value 30 in my_list is: ", index)
