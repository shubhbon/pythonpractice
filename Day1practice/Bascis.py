# # 1.hello world program
# print("Hello world")
#
#
# #2. add two numbers
# a= 10
# b= 20
# print(a+b)
#
#
# # #3.check even or odd number
# # num = int(input("Enter a number"))
# # if num % 2 == 0:
# #     print("even number")
# # else:
# #     print("odd number")
#
#
# #4.Swap Two Variables
# a= 3
# b= 4
# a,b = b,a
#
# print("now a value is " + str(a))
# print("now b value is " + str(b))
#
# print(f"now a value is {a}")
# print(f"now b value is {b}")
#
# print("now a value is", a)
# print("now b value is", b)


#5. Find Factorial of a Number
# num = int(input("Enter a number"))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print(f"factorial of num is {fact}")


#6. Reverse a Number
# num = int(input("Enter a number"))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(f"Reverse number is {rev}")



#7. Program to check the prime number
# num = int(input("enter a number"))
# if num <= 1:
#     print("Not a primary number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a primary number")
#             break
#     else:
#         print("Primary number")


#8 Program to find the GCD of two numbers
# a= int(input("Enter a number: "))
# b= int(input("Enter another number: "))
#
# gcd =1
# for i in range(1,min(a,b)+1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print("gcd is", gcd)


#
# # 9 Program to find the sum of digits
# num = int(input("Enter a number: "))
# sum_digit = 0
# temp = num
#
# while temp > 0:
#      digit = temp % 10
#      sum_digit += digit
#      temp = temp // 10
# print(f"sum of digit of {num} is {sum_digit}")




#10 Program to check Armstrong number.

# easy way :
armstromg

num = int(input("Enter a number:"))
total = 0
n = len(str(num))

for i in str(num):
    total = total+ int(i)** n

if total == num:
    print("The number is armstrong")
else:
    print("The number is not armstrong")



#little complex
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
n_digits = len(str(num))  # number of digits

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** n_digits
    temp //= 10

if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
