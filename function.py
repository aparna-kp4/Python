                                   # USER DEFINED FUNCTION
# # a=int(input("Enter your number"))
# def square(num):
#     return num**2
# a=int(input("Enter your number"))                             #it can use any place
# b=square(a)
# print("The square of the given number is:",b)





#                                  #CALLING A FUNCTION

# def a_function(string):
#     "This prints the value of length of string"    #this can be only used to understanding the function
#     a=len(string)              #   or  it can be use this method(return len(string))
#     return a
# #calling the function we defined
# print(a_function("Functions"))
# print(a_function("Python"))



                                #WITH ARGUMENT WITH RETURN TYPE

#function to calculate square of a number

# def square(num):
#     return num*num
# result=square(5)
# print("Square:",result)



                              #WITH ARGUMENT WITHOUT RETURN TYPE

#function to print greeting message

# def greet(name):
#     print("Hello",name + "!")
# greet("Ammu")                         #it can call function


                              #WITHOUT ARGUMENT WITH RETURN TYPE

#function that returns a welcome message

# def get_message():
#     return "Welcome to Python programming"
# msg=get_message()
# print(msg)

                                 #WITHOUT ARGUMENT WITHOUT RETURN TYPE

#function to print numbers from 1-5

# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers()



#..............................................Default arguments

# def function(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Passing only one argument")
# function(30)


#............................................Keyword arguments

# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Without using keyword")
# function(n2=50,n1=20)


#...........................................Anonymous function

# lambda_=lambda argument1,argument2:argument1+argument2
# print("Value of the function is:",lambda_(20,30))
# print("Value of the function is:",lambda_(40,50))



#...............................................Python function within another function

# def word():
#     string='Python functions tutorial'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()


#.................................................RECURSIVE FUNCTION



#FACTORIAL of a number is the product of all the integers from 1 to that number.For example,the factorial of 6(denoted as 6)



# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=3
# print("The factorial of",num,"is",factorial(num))                  




# #*****************************************************WORKING  OF FACTORIAL

# factorial(3)        1st call with3
# 3*factorial(2)      2nd  call  with 2
# 3*2*factorial(1)     3rd call with  1
# 3*2*1                return from 3rd call as number=1
# 3*2                 return from 2nd call
# 6                    return from 1st call





#Write a function that takes a list of numbers and returns the maximum

# def maximum(num):
    



#define a function that returns the reverse of an string
# def reverse():
#     a=""
#     for i in str:
#         a=i+a
#     return a
# str=input("Enter the string")
# b=reverse()
# print("reverse of the string:",b)



#*****************IMPORT STATEMENT***************(it can be call constant values)

# import math
# print("The value of eulers number is",math.e)

#**********************************IMPORTING AND ALSO RENAMING    (it can be used to renam9ing the key word as can be used and to renaming)

# import math as mt
# print("the value of  eulers number is",mt.e)


#******************GETTING FORMATTED TIME**************

#the time can be formatted by using the asctime()function

# import time
# print(time.asctime(time.localtime(time.time())))

#*************PYTHON SLEEPING TIME****************

# import time
# for i in range(0,5):
#     print(i)
#     time.sleep(5)             #the 5 can be used to calculate seconds

# #*************DATE TIME MODULE

# import datetime                       #returns current datetime object
# print(datetime.datetime.now())


#CALENDER MODULe

# import calendar
# cal=calendar.month(2020,3)
# print(cal)

#print the calendar of whole year


# import calendar
# cal=calendar.calendar(2005)
# print(cal)


#oops nokkanam