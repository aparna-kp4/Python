#<<<<<<<<<<<<<<<<INHERITANCE>>>>>>>>>>>>>>>>>>

# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# class Dog(Animal):
#         def bark(self):
#          print("dog barking")
# d=Dog()
# d.bark()
# d.speak()


#<<<<<<<<<<<<<<<MULTILEVEL INHERITANCE>>>>>>>>>>>>>>>>>

# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#     #the child class dog inheritance the base class animal
# class Dog(Animal):
# #     def bark(self):
# #         print("dog barking")
# #     #the child dogclass inheritance another child class dog
# # class DogChild(Dog):
# #     def eat(self):
# #         print("Eating bread")
# # d=DogChild()
# # d.bark()
# # d.speak()
# # d.eat()


# #<<<<<<<<<<<<<<<<<<<MULTIPLE INHERITANCE>>>>>>>>>>>>>

# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def multiplication(self,a,b):   #it is not connection of Calculation1and Calculation2 it can be combine in the 3 rd class
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.summation(10,20))
# print(d.multiplication(10,20))
# print(d.Divide(10,20))


#<<<<<<<<<<<<<<<<<<HIERARCHICAL INHERITANCE>>>>>>>>>>>>>>  it contain only one parent and one more child

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#     #derived class
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child1.")
#     #derived class2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child2.")
# d=Child1()
# d.func1()
# d.func2()
# c=Child1()
# c.func2()
# c.func1()



#<<<<<<<<<<<<HYBRID INHERITANCE>>>>>>>>>>>>>>>


# class Animal:
#      def speak(self):
#          print("Animal Speaking")
# class Dog(Animal):
#          def bark(self):
#           print("dog barking")
# class Animal:
#      def speak(self):
#           print("Animal Speaking")
# #     #the child class dog inheritance the base class animal
# class Dog(Animal):
#       def bark(self):
#           print("dog barking")
# #      #the child dogclass inheritance another child class dog
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread")


