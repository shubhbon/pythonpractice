#1.Program to append elements to the list.  // append means add the value in list
arr = [10,20,30]
arr.append(40)
print("updated list:",arr) #[10,20,30,40]



#2.Program to extend the list.
arr = [10,20,30]
arr.extend([40,50,60])
print("Extended list:",arr)



#3.Program to insert an element at the specific position.
arr = [10,20,30]
pos= 2
value= 25
arr.insert(pos,value)
print("inserted list:", arr)



#4.Program to remove an element from the list.
arr = [10,20,30]
arr.remove(30)
print("Removed list:", arr)


#5.Program to pop list element.
arr = [10,20,30,40,50]
removed = arr.pop()  # removed last element
print("pop updated list:",removed)
print("after pop updated list:",arr)



#6.Program to count occurrences of list elements.
arr = [1,2,3,3,3,4,5,6,6,6]
count = {}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i] =1
print("Element occurrences as per below:")
for key, value in count.items():
     print(key, ": ", value)





