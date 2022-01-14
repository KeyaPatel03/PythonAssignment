''' (a)  Write a Python program to create a tuple with different data types. '''
print("Program - (a)")

tuple = (True,'Keya',88,20.22)     # Tuple with different datatype
print(tuple)



''' (b) Write a Python program to create a tuple with numbers and print one item. '''
print("\nProgram - (b)")

tuple1 = (-1 ,0 ,3 , -10, 33 , 107)
print(tuple[2])         # Printing element at 2md index of tuple



''' (c) Write a Python program to add an item in a tuple. '''
print("\nProgram - (c)")

tuple1 = ( -1, 0, 3, -10, 33, 107)
sum = 0
for i in range(len(tuple1)):  # Loop iterates from i=0 to i=length of tuple1
    sum = sum + tuple1[i]       # Performs the summations
print("Addition of items of tuple is ",sum)



''' (d) Write a Python program to convert a tuple to a string. '''
print("\nProgram - (d)")

tuple2 = ('g','i','t','h','u','b')
str = ''
for i in range(len(tuple2)):
    str += tuple2[i]            # Storing each element of tuple in str one by one
print("Tuple: ",tuple2)
print("It's string form: ",str)



''' (e) Write a Python program to find the length of a tuple. '''
print("\nProgram - (e)")
print(tuple)
print("Length of tuple : ",len(tuple))

