'''(a) Write a Python script to check whether a given key already exists in a dictionary.'''
print("Program - (a)")

dict = {'k1':'value1' , 'k2':'value2' ,'k6':'value2', 'k3':'value3' , 'k4':'value4' }
k_searched = input("Enter the key you want to search for: ")      # User enters the key to be searched
print(dict)                         # prints the whole dictionary.
for key in dict:
    if key==k_searched:             # if condition to check of the key
        print("Yes, the given key-",k_searched," already exists in a dictionary.")



''' (b)  Write a Python script to merge two Python dictionaryies. '''
print("\nProgram - (b)")

student1 = {'DSA': 98 , 'PYTHON':78 , 'DBMS':90}
student2 = {'HS':100 , 'MCO':99 , 'PYTHON':99}
total_marks = {**student1,**student2}           # This will merge both the dictionaries
print("student1 : ",student1,'\nstudent2 : ',student2)
print("Merged dictionary : ",total_marks)



''' (c) Write a Python program to sum all the items in a dictionary. '''
print("\nProgram - (c)")

student1 = {'DSA': 98 , 'PYTHON':78 , 'DBMS':90 , 'HS':100 ,'MCO':96}
add=0
print(student1)
for i in student1.values():
    add += i
print("Summation of all the marks(values) : ",add)



''' (d) Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} '''
print("\nProgram - (d)")

dict = {'eng':78 , 'phy':90 , 'maths':100}
print("Initial dictionary : ",dict)
dict['comp']=100                # Add key to the dictionary
print("Final dictionary : ",dict)



''' (e)  Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} '''
print("\nProgram - (e)")

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4= {**dic1, **dic2, **dic3}      # Concatenates all three dictionaries
print("Dic1=", dic1)
print("Dict2=", dic2)
print("Dict3=", dic3)
print("Dict4=", dic4)
