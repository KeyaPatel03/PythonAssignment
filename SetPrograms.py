''' (a) Write a Python program to add member(s) in a set and clear a set '''
from itertools import count
from statistics import mode     # This file is imported because we are using mode mtd here in program - (e)

print("Program - (a)")

set = {1,2,3,4,5,'a'}
print("Set (before add) : ",set)
set.add('b')        # 'b; is added in set
set.add('c')        # 'c' is added in set
print("Set (after add) : ",set)
set.clear()         # the whole set is getting clear using clear function
print("Set (after clear) : ",set)


''' (b) Write a Python program to remove an item from a set if it is present in the set. '''
print("\nProgram - (b)")

set1 = {'a','b','c','d','e','f','u'}
print(set1)
rm = str(input("Enter an element to be deleted from set: "))
set1.remove(rm)         # The element is removed from set using remove function
print("Set (after remove) : ",set1)


''' (c) Write a Python program to create an intersection, Union, difference of sets. '''
print("\nProgram - (c)")

a = {1 , 'a' , 'py' , 50}
b = {80 , 'a' , '50' , 50}
print("Union : ",a.union(b))    # set union using union function
print("Intersection : ",a.intersection(b))  # set intersection using intersection function
print("Difference : ",b.difference(a))  # set difference using difference function


''' (d) Write a Python program to find maximum and the minimum value in a set. '''
print("\nProgram - (d)")

set2 = {1,2,3,30,40,50}
l = list(set2)
print(l)
max = min = l[0]
for i in range(len(l)):
    if max < l[i]:      # condition to find max element
        max = l[i]
    elif min > l[i]:    # condition to find min element
        min = l[i]
print("Max value : ",max)
print("Min value : ",min)


''' (e) Write a Python program to find the most common elements and their counts from list, tuple, dictionary. '''
print("\nProgram - (e)")

#For list
List = [82, 10, 82, 82, 100, 33]
a=mode(List)
print(List)
print("In the given list the most common element is ",a)
print("count= ",List.count(a))

#FOR tuple
Tuple = (1,2,2,3)
a=mode(Tuple)
print(Tuple)
print("Tn the given tuple the most common element is ",a)
print("count= ",Tuple.count(a))

#For dictionary
dict={1:11,2:22,3:33,4:11,5:11}
list = [(k, v) for k, v in dict.items()]    # Converting into list of tuple
a = mode(list)
print(dict)
print("In the given dictionary the most common element is ",a)
print("count= ",list.count(a))