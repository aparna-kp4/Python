

                                                      #2right half pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

                                                      #3inverted right half pyramid

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*",end=" ")
#     print()



                                                     #5left half

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(i):
#         print("* ",end=" ")
#     print()

                                                #6full pyramid

# n=5
# for i in range(0,n):
#     for k in range(0,n-i):
#            print("  ",end=" ")
#     for j in range(0,i+1):
#           print("* ",end="    ")
#     print()


                                                 #7rhombus pattern

# n=5
# for i in range(1,n+1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(n):
#         print("*",end=" ")
#     print() 

                                                     #8full pyramid
# n=5
# for i in range(0,n):
#     for k in range(0,n-i):
#            print(" ",end=" ")
#     for j in range(0,i+1):
#           print("* ",end="  ")
#     print()

                                                    #8hollow square pattern

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("* ",end=" ")
#         else:
#             print(" ",end="  ")
#     print()


                                                     #8inveerted pyramid


# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()




                                                  #9  diamond


# n=5
# for i in range(0,n):
#     for k in range(0,n-i):
#            print(" ",end=" ")
#     for j in range(0,i+1):
#           print("* ",end="   ")
#     print()
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(2*i-1):
#         print("*",end="  ")
#     print()





                                        #10hourglass pattern


# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="   ")
#     for k in range(2*i-1):
#         print("* ",end="  ")
#     print()


# n=5
# for i in range(0,n):
#     for k in range(0,n-i):
#            print("  ",end=" ")
#     for j in range(0,i+1):
#           print("* ",end="  ")
#     print()


#hollow inverted full daigram
# n=5
# for i in range(n,n-1):
    # for j in range()