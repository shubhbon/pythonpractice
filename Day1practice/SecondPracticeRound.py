# 1.hello world program
print("hello world")

# 2. add two numbers
a=10
b=20
print("two number added:" ,a+b)



#3.check even or odd number
num = int(input("Enter a number:"))
if num % 2 ==0:
    print("given number is even")
else:
    print("given number is odd")



#4.Swap Two Variables
a=10
b=20
a,b = b,a
print("now value of a is:" ,a)
print("now value of b is:" ,b)



#5.Find Factorial of a Number
num = int(input("Enter a number"))
fact = 1
for i in range(1,num+1):
    fact *= i
print(fact)


#6. Reverse a Number
num = int(input("Enter a number"))
rev = 0
while num > 0:
    digit = rev % 10
    rev = rev * 10 + digit
    num//=10
print(rev)


#7. Program to check the prime number
num = int(input("Enter a number"))
if num >=1:
    print("not a primary number")
else:
    for i in range (2, num):
        if num % i ==0:
            print("not a primary number")
            break
    else:
        print("primary number")


#10 Program to check Armstrong number.
num = int(input("Enter a number"))
sum_digits = 0
temp = num
n_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_digits = digit ** n_digits
    temp //= 10
if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
#------------------------------------------------------------------

num = int(input("enter a number"))
sum_digits = 0
temp = num
n_digits = len(str(num))

while temp > 0:
    digit = temp %10
    sum_digits = digit ** 10
    temp //=10
if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")