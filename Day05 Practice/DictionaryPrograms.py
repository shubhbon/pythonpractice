#1.Program to extract Unique values dictionary values
from operator import itemgetter

data= {'a':10, 'b':20 ,'c':10, 'd':30, 'e':20}
unique_values = set(data.values())
print(unique_values)


#2.Program to find the sum of all items in a dictionary
data = {'a':10, 'b':20 ,'c':10, 'd':30, 'e':20}
total = sum(data.values())
print("Sum of all values:",total)


#3.Program to remove a key from a dictionary
data = {'a':10, 'b':20 ,'c':10, 'd':30, 'e':20}
del data['b']
print(data)



#4.Program to sort the list of dictionaries by values in Python using itemgetter.
students = [{'name':'jhon', 'age':23},{'name':'alice', 'age':21},{'name':'bob', 'age':25}]
sorted_list = sorted(students, key=itemgetter('age'))
print("sorted_list:")
for item in sorted_list:
    print(item)


#5.Program to sort the list of dictionaries by values in Python using lambda
students = [{'name':'jhon', 'age':23},
            {'name':'alice', 'age':21},
            {'name':'bob', 'age':25}]
sorted_list = sorted(students, key =lambda x: x['age'])
print("sorted_list:")
for item in sorted_list:
    print(item)