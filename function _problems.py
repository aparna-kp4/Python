#................2Write a recursive function to calculate the sum of first n natural numbers
# def sum_no(n):
#     if n !=0:
#         return n +sum_no(n - 1)
#     else:
#         return 0
# no = int(input("Enter your number"))
# print("sum=", sum_no(no))

#................1write a recursive function to print numbers from n to 1

# def numbers(n):
#     if n <= 0:
#         return
#     print(n)
#     numbers(n - 1)

# #................write a recursive function to find the sum of digits of a numbers
# def sum_digit(n):
#     if n==0:
#         return 0
#     else:
#         return (n % 10) + sum_digit(n // 10)
# a=int(input("Enter a number: "))
# print("Sum of the digits:", sum_digit(a))
   
# 
# 
# 1 ....................................... Write a function that takes a list of numbers and returns the maximum               

# def max():
#     list=[2,10,6,8,3]
#     a=0
#     for i in list:
#         if i>a:
#             a=i
#     print(a)        
# max() 


# 2 ...................................... Define a function that returns the reverse of a given string.

# def reverse():
#     str=input("enter the string:")
#     rev=""
#     for i in str:
#         rev=i+rev
#     print(rev)
# reverse()        


# 3 ........................................ Write a function that takes a string and counts the number of vowels.
# def VOWELS():
#     str=input("Enter a string:")
#     count=0
#     for i in str:
#         if i in['a','i','o','e','u','A','E','I','O','U']:
#             count=count+1
#     print(count)
# VOWELS()

#4.........................................factorial

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 3
# print("The factorial of", num, "is", factorial(num))


# 5 ................................. Define a function that accepts a list and returns a new list with only even numbers.

# def Even():
#     list1=[1,2,3,4,6,7,8,9] 
#     Even_list=[]
#     for i in list1:
#         if(i%2==0):
#             Even_list.append(i)
#     print(Even_list)    
# Even()



# 6 .................................. Write a function that calculates the power of a number (without using ** or pow).

# def power(x,y):
#     result = 1
#     for i in range(y):
#         result *= x
#     print("power:", result)
# a=int(input("Enter number:"))
# b=int(input("Enter power:"))
# power(a,b)


# 7 ............................... Create a menu-driven program using functions:
# #  a) Add two numbers
# #  b) Subtract two numbers
# #  c) Multiply two numbers
# #  d) Divide two numbers
# #  e) Exit
# #      (Use functions for each operation.)

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     if b!=0:
#         return a/b
#     else:
#         print("Cannot divide by zero")

# def menu():
#     while True:
#         print("\nMENU:")
#         print("1.ADD")
#         print("2.SUBTRACT")
#         print("3.MULTIPLY")
#         print("4.DIVIDE")
#         optn=int(input("Enter your choice :"))

#         a=int(input("Enter 1st number:"))
#         b=int(input("Enter 2nd number:"))

#         if  optn==1:
#             print("Result:",add(a,b))
#         elif  optn==2:
#             print("Result:",sub(a,b))
#         elif  optn==3:
#             print("Result:",mul(a,b))
#         elif  optn==4:
#             print("Result:",div(a,b))
#         else:
#             print("Enter a valid choice!")

# menu()     

                         #   ANONYMOUS Fn
                     # .......................

# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the fn is :",lambda_(20,30))
# print("Value of the fn is :",lambda_(40,50))



                         #   ANONYMOUS Fn
                     # .......................

# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the fn is :",lambda_(20,30))
# print("Value of the fn is :",lambda_(40,50))



#<<<<<<<<<<<<<<<   ANONYMOUS FUNCTION  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                     

# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the fn is :",lambda_(20,30))
# print("Value of the fn is :",lambda_(40,50))


#1 ..................................... Write a lambda function to find the square of a number.

# lambda_=lambda n1: n1**2
# a=int(input("Enter a number:"))
# print("The square is :",lambda_(a))

#2 ..................................... Write a lambda function to check if a number is even or odd.

# even_no= lambda n: "Even" if n % 2 == 0  else "Odd"
# a= int(input("Enter a number: "))
# print("The number is:",(even_no))

#3......................................maximum numbers


max_num = lambda a, b: a if a > b else b
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print("The greater number is:", max_num(n1,2))







