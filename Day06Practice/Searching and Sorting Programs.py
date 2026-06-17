#1.Program for Binary Search
from operator import truediv

# arr = [10,20,30,40,50]
# key = int(input("enter element to search: "))
#
# low = 0
# high = len(arr)-1
#
# found = False
#
# while low <=high:
#     mid = (low+high)//2
#
#     if arr[mid] == key:
#         print("Element found at index",mid)
#         found = True
#         break
#     elif key < arr[mid]:
#         high = mid-1
#     else:
#         low = mid+1
#
# if not found:
#     print("Element not found")



#2.Program for Linear Search
# arr= [10,20,30,40,50]
# key = int(input("enter element to search: "))
# found = False
#
# for i in range(len(arr)):
#     if arr[i] == key:
#         print("Element found at index",i)
#         found = True
#         break
# if not found:
#     print("Element not found")


#3.Program for Insertion Sort

def insertion_sort(arr):
    n=len(arr)
    for i in range (1,n):
        key = arr[i]
        j = i-1
        # move elementts greater than key one position ahead

        while j>0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j +1] = key

arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("sorted array:",arr)


#4. Program for QuickSort

def quick_sort(arr):
    if len(arr) <=1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

arr =[5,3,8,4,2]
sorted_arr = quick_sort(arr)
print("sorted array:",arr)



#5.Program for Selection Sort

arr = [64,25,12,22,11]
n =len(arr)
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j]< arr[min_index]:
            min_index =j
# swap the found minimum element with the first element
arr[i], arr[min_index] = arr[min_index], arr[i]

print("sorted array:",arr)


#6.Program for Bubble Sort

arr = [62,34,25,12,22,11,90]
n = len(arr)

for i in range(n):
    for j in range(0, n- i - 1):
        if arr[j] > arr [j +1 ]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("sorted array:",arr)


#.7 Program for Merge Sort

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]


    left = merge_sort(left)
    right = merge_sort(right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
    else:
        result.append(right[j])
        j+=1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

arr = [38,27,43,3,9,82,10]
sorted_arr = merge_sort(arr)
print("sorted array:",arr)