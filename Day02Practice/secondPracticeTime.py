#1 Program to the maximum in an array
from heapq import merge

from Day02Practice.ArrayPrograms import second_largest

arr = [10,20,30,40,50]
max_value = arr[0]
for i in arr:
    if i > max_value:
        max_value = i
print(max_value)

#2 program to the minimun in a array
arr = [10,20,30,40,50]
min_value = arr[0]
for i in arr:
    if i < min_value:
        min_value = i
print(min_value)

#3 Program to find the sum of array elements.
arr = [10,20,30,40,50]
total = 0
for i in arr:
    total += i
print(total)

#4.Program to reverse the array elements.
arr = [10,20,30,40,50]
n = len(arr)
for i in range(n // 2):
    arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
    print(arr)

#5.Program to merge array elements
arr1= [1,2,3]
arr2= [4,5,6]
merge = []
for i in arr1:
    merge.append(i)
for j in arr2:
    merge.append(j)

print(merge)


#6.Program to remove duplicates from an array
arr = [1,2,3,4,5,1,2,3,4]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)

#8. Program to find the second largest array element.
arr = [10,43,34,89,12]
largest = second_largest = float('-inf')
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)