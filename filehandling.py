#<<<<<<<<<<<<<<<<<<<<<<<<<<<CREATE FILE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# f=open('file.txt','x')                     #to create a new file in right side of files (file.txt)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<READ OPERATIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# file=open('file.txt','r')                    #it can print the file.txt details
# for each in file:
#     print(each)


#..............example 1  #read line by line
# f=open("file.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()

#............. example2  same function of example 1 without for loop

# f=open("file.txt","r")
# print(f.read())

#..................example3

# with open("file.txt")as file:
#     data=file.read()
# print(data)


#...................example4 <<can be find limit of letters to find the first two lettres like that>>

# file=open("file.txt","r")
# print(file.read(10))


# #..................example5 <<also split the lines while reading files like word by word (hey,how,are,you)>>

# with open("file.txt","r")as file:
#     data=file.readlines()
# for line in data:
#     word=line.split()
#     print(word)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WRITE OPERATIONS>>>>>>>>>>>>>>>>

#................this can be write the file file.txt  and the code can be change the new sentance and replace the sentance

# file=open('file.txt','w')
# file.write("heyy where are youu")
# file.write("iam here")
# file.close()

#................it can add new line do not replace first sentance

# file=open('file.txt','a')
# file.write("this is will add this line")
# file.close()
