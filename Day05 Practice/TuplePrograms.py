#.1.Program to find the size of a Tuple
t= (10,20,30,40,50)
size = len(t)
print(size)


#.2.Program to find the maximum and minimum K elements in Tuple
t= (10,3,4,5,6,20,2)
k=3
#convert tuple to list and sort
sorted_list = sorted(t)

min_k = sorted_list[:k]
max_k = sorted_list[-k:]

print("minimum",k, "element:", min_k)
print("maximum",k, "element:", max_k)


#3.Program to create a list of tuples from a given list having a number and its cube in each tuple
nums = [1, 2, 3, 4, 5]
result = []
for n in nums:
    result.append((n,n**3))
print("list of tuples:", result)



#4.Program to add a Tuple to the List
my_list = [(1,2),(3,4)]
new_tuple = (5,6)
my_list.append(new_tuple)
print(my_list)


