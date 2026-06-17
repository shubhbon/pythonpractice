#1 Program to the maximum in an array
arr= [10, 45, 28, 89, 12]
max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i
print("maximum element is:", max_val)



#2 Program to the minimum in an array
arr= [10, 45, 28, 89, 12]
min_val = arr[0]
for i in arr:
    if i < min_val:
        min_val = i
print("minimum element is:", min_val)



#3 Program to find the sum of array elements.
arr = [10,20,30,40]
total = 0
for i in arr:
    total += i
print("Sum of array element is :", total)



#4.Program to reverse the array elements.
arr = [10,20,30,40]
n = len(arr)
for i in range(n // 2):
    arr[i],arr[n-i-1] = arr[n - i - 1],arr[i]
print("Reversed array:", arr)


#5.Program to merge array elements
arr1 = [1,2,3]
arr2 = [4,5,6]
merged = []
for i in arr1:
    merged.append(i)
for j in arr2:
    merged.append(j)
print("Merged array:",merged)



#6.Program to remove duplicates from an array
arr = [1,3,4,2,1,3,2,4]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("Array after removing duplicates:",unique)



#7.Program to rotate array.

arr = [1,2,3,4,5]
k=2
n= len(arr)

k= k % n

for _ in range(k):
    first =arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n - 1] = first
print("Left roated array:", arr)



#8. Program to find the second largest array element.

arr = [10,43,34,89,12]

largest = second_largest = float('-inf')   # menas negative infinity . it helps handle all valuse safely

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element is:", second_largest)



