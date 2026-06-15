# 01. hello world perfoam
print("Hello World")

#02 add two number
a=10
b=20
print(a+b)

##3.check even or odd number
# num =int(input("enter the number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#04 swap the variable
a=3
b=5
a,b = b,a
print("a value is ",a)
print("b value is ",b)

print(f"value of a is {a}")
print(f"value of b is {b}")



# #05 find the factorial of number (it means if i enter 5 then it will calculate like this - 5*4*3*2*1 )
# num = int(input("Enter the number"))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print(fact)
#
# #6 rev number
# num = input("Enter a number: ")
# rev = ""
#
# for digit in num:
#     rev = digit + rev
#
# print("Reverse number is", rev)
#

#07. check program is prime number

# num= int(input("Enter a number: "))
# if num >= 1:
#     print("not a primary number")
# else :
#     for i in range (2, num):
#         if num % i == 0:
#             print("not a prime number")
#             break
#     else:
#         print("primary number")


#armstromg

num = int(input("Enter a number:"))
total = 0
n = len(str(num))

for i in str(num):
    total = total+ int(i)** n

if total == num:
    print("The number is armstrong")
else:
    print("The number is not armstrong")




