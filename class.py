#factorial

# a=int(input("enter your number"))
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)

#1sum of even numbers

# a=int(input("enter your number"))
# sum=0
# for i in range(2,a+1,2):
#     sum+=i
# print(sum)

#2calculate product

# num=[3,3]
# mul=1
# for num in num:
#     mul*=num
# print(mul)


#3reverse string


# str=input("enter a string:")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)

#4maximum number in list

# a=[10,30,0,1]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# print("the maximum list is:",max)



#5print characters at even indices input a string and use a for loop to print characters at even position index[0,2,4,6]

# a=str(input("enter your string"))
# b=len(a)
# for i in range(0,b,2):
#     print(a[i])

#6to print common elements in a list


# a=[1,3,5,7,2,5,3]
# b=[1,3,2,6,8,9]
# c=[]
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

#count vowels in a string

# string=(input("enter your string"))
# count=0
# vowels="aeiouAEIOU"
# for char in string:
#     if char in vowels:
#         count+=1
# print(count)




#sum of two digits

# a=int(input("enter your number"))
# b=str(a)
# for i in range(a):
#       str=a
#       a=int
      
# print(b)


#while loop


# a=int(input("enter your number:"))
# b=0
# while a!=-1:      #we can denote a not equal to -1
#     b+=a
#     a=int(input("enter your number:"))
# print(b)


#nested loop

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()

#to print 1 to 25

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(a,end=" ")
#         a+=1
#     print()




#to print triangle stars

# n=5
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("* ",end=" ") 
#     print()




# #reverse of an star traingle

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#             print("* ",end=" ")
#     print()




# n=5
# for i in range(0,n):
#       for j in range(0,n-i):
#           print(" ",end=" ")
#       for k in range(0,i):
#           print("*",end=" ")
#       print()
      


#list comprehensions

#matrix comprehension

# matrix=[[j for j in range(3)]for i in range(3)]
# print(matrix)
        

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#              print("* ",end=" ")
#         else:
#              print(" ",end="  ")
#     print()



# n=5
# for i in range(0,n-1):
#       for j in range(0,n-i):
#           print(" ",end=" ")
      