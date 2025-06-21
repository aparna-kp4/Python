#In Python, *args and **kwargs are used in function definitions to allow the function to accept a variable number of arguments


#...............*args and **kwargs...............

#__________________________*args______________________________

#🔹 *args (Non-keyword arguments)

#Used to pass a variable number of positional arguments

#Inside the function, args is a tuple.

#example

# def function(*args):
#     for arg in args:
#         print(arg)
# function(1,2,3)


#🔹 **kwargs (Keyword arguments)

#Used to pass a variable number of keyword arguments.
#Inside the function, kwargs is a dictionary.

#example

# def function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# function(name="Alice", age=30)

0
#🔹 Using Both Together
#You can combine both in a function, but *args must come before **kwargs.

#Example:

# def function(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# function(10, 20, name="Bob", job="Developer")

#non keyword argument

#it is an positional arguments

#it is passed to a function  based on their position in the function call

#keyword arguments

#passed to a function using the parameter name 





