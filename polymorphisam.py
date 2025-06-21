#example1

# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
# d=Dog()
# d.speak()

#example 2

# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 6
# class ICICI(Bank):
#     def getroi(self):
#         return 8
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank Rate of interest:",b1.getroi())
# print("SBI Rate of interest:",b2.getroi())
# print("ICICI Rate of interest:",b3.getroi())


#exmple3


# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#     def flight(self):
#         print("Most of the birds can fly but some cannot")
# class sparrow(Bird):
#     def flight(self):
#         print("sparrows can fly")
# class ostrich(Bird):
#     def flight(self):
#         print("Ostrich cannot fly")
# d=Bird()
# d.intro()
# d.flight()

# c=sparrow()
# c.intro()
# c.flight()

# a=ostrich()
# a.intro()
# a.flight()


#                                         example 4

# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 
# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
#print("Accessing protected member of obj2: ", obj2._a) 


#                                               4example

# class Base:
#     def __init__(self):
#         self.a ="Hello"
#         self.__c="World"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
# obj1 = Base()
# print(obj1.a) 
# obj2=Derived()


#                                   data abstraction







