#................................................type error
# x=5
# y="hello"
# z=x+y#raises type error

#.................................................try catch block to resolve it
# x=5
# y="hello"
# try:
#     z=x+y
# except TypeError:
#     print("Error:cannot add an int and a str")


# ................................................try and except statement -catching statement

# a=[1,2,3]
# try:
#     print("second element=",a[1])
#     print("Fourth element=",a[3])
# except:
#     print("An error occured")

#(the print statemnt can add try or catch statement)
# #..................................................the error can print
# a=[1,2,3]
# try:
#     print("second element=",a[1])
#     print("Fourth element=",a[3])
# except Exception as e:
#     print(e)

#raise error can used to force fully detected an error

#................................................raising exception
#program to depict raising exceprtion
# try:
#     raise NameError("hey")                  #raise error
# except NameError:
#     print("An exception")
# raise     #to determine whether the exception
