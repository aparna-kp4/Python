
#<<<<<<<<<<<<<<<<<<<<<<<<OOPS CONCEPT>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<<<<<<<<<CLASS>>>>>>>>>>>>>>>>>>>>>>

# class Employee:
#     id=10
#     name="Aparna"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))           # %d it display integer  and  %s it display string 
# emp=Employee()             #it can be call the function
# emp.display()             #it can be print the function




#..............DELETE THEOBJECT

# class Employee:
#     id=10
#     name="Aparna"
#     def display(self):
#          print("ID:%d\nName:%s"%(self.id,self.name))  
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()      #it will through the attribute error beacuse we have deleted the object emp


#<<<<<<<<<<<<<<<<<<<<<<<<<....OBJECT....>>>>>>>>>>>>>>>>>>>>>>>>>>

#...........parameterised constructor  the value can pass class through


# class Car:
#     def __init__(self,modelname,year):             #after def keyword must be space
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)               #parameterised constructor
# c1=Car("Toyota",2016)
# c1.display()    


#...............NON PARAMETERISED CONSTRUCTOR......

# class Student:
#     def __init__(self):
#         print("This is non paramettized constructor")
#     def show(self,name):
#         print("Hello",name) 
# Student=Student()
# Student.show("Aparna")   

#..............DEFAULT CONSTRUCTOR............

# class Student:
#     roll_num=101
#     name="Aparna"
#     def display(self):
#         print(self.roll_num,self.name)
# st=Student()
# st.display()



#..........................getattr prints the attribue name of the object s


# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("Aparna",101,20)
# print(getattr(s,'name'))

# #..........set attribute can be used to update the self (reset the value)

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("Aparna",101,22)
# setattr(s,"age",23)
# print(getattr(s,'age'))


#.............print true if the student contains the attribute with name id

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("Aparna",101,20)
# print(hasattr(s,'id'))

#...............this will given an error since the attribute age has been deleted

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("Aparna",101,20)
# print(delattr(s,'name'))