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


class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")
class sparrow(Bird):
    def flight(self):
        print("sparrows can fly")
class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")
d=Bird()
d.intro()
d.flight()

c=sparrow()
c.intro()
c.flight()

a=ostrich()
a.intro()
a.flight()


