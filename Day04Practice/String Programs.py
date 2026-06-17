# #1. Python program to check if a string is palindrome or not
# s = input("enter a string:")
#
# rev = ""
# for char in s:
#     rev = char + rev
# if s == rev:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
#
# #2.Python program to check whether the string is Symmetrical or Palindrome
#
# s= input("enter a string:")
#
# if s == s[::-1]:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
#
# n= len(s)
# mid = n //2
#
# if n%2 == 0:
#     first = s[:mid]
#     second = s[mid:]
# else:
#     first = s[:mid]
#     second = s[mid+1:]
#
# if first == second:
#     print("String is symmetrical")
# else:
#     print("String is not symmetrical")


#3.Reverse words in a given String in Python
#Hello world from Python
#"Python from world Hello"

# s =input("enter a string:")
# word = s.split()
# word.reverse()
# reversed_string = ' '.join(word)
# print(reversed_string)


#
# #4.Program to remove Kth character from string in Python
# s = input("enter a string:")
# k = int(input("Enter the position of charactor to remove(1-based index): "))
# new_s = s[:k-1] + s[k:]
# print("String after removing",new_s)


#5 .Program to check if a Substring is Present in a Given String

s   = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

if sub in s:
    print(f"'{sub}' is present in the string.")
else:
    print(f"'{sub}' is NOT present in the string.")
