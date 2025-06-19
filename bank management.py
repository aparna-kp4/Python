# d={}
# acc_no=10001
# a=1

# while True:
#     print("1.Create a account")
#     print("2.Deposit money")
#     print("3.Withdraw money")
#     print("4.Display account details")
#     print("5.Exit")

#     choice=int(input("Enter your choice"))
#     if choice== 1:
#             name=input("Enter your name")
#             initial_balance=int(input("Enter your initial_balance"))
#             data={}
#             data['name']=name
#             data['initaial_balance']=initial_balance
#             data['acc_no']=acc_no
#             d[a]=data
            
#             # d.append({"acc_no":acc_no,"name":name,"initial_balance":initial_balance,})
#             print(d)
#             acc_no+=1
#             print(acc_no)
#             a+=1
            
            

#     elif choice== 2:
#           account_number=int(input("Enter your acc number"))
#           a=0
#           for i in d:
#             for j in d[i]:
               
#                if d[i]["acc_no"] == account_number:
#                     a=1
#                     amount=int(input("Enter your deposit amount"))
#                     if amount>0:
#                         d[i]["initaial_balance"]=amount+d[i]["initaial_balance"]
#                         print(f"{amount} amount deposit to the account number {account_number} and your balance is {d[i]["initaial_balance"]}")
#                         break
#                     else:
#                         print("deposit amount is less than zero")
#                         break  
#           if a==0:
#                     print("there is no account is matching ")
                    


#     elif choice== 3:
#           account_number=int(input("Enter your account number"))
#           amount=int(input("Enter your withdraw money"))
#           for i in d:
#             for j in d[i]:
#                if d[i]["acc_no"] == account_number:
#                   if amount>0 and amount<=initial_balance:
#                         initial_balance=initial_balance-amount
#                         print(f"{amount} amount is withdraw to the account number {account_number} and your balance is {initial_balance}")
#                         break
#                   else:
#                         print("enter a valid amount")
#                         break


#     elif choice== 4:
#           account_number=int(input("Enter your acc_no"))
#           for i in d:
#             print(d[i]["acc_no"])
#             if d[i]["acc_no"] == account_number:
#                   print("account_number",account_number)
#                   print("name",name)
#                   print("initial balance",initial_balance)
#                   break
#             else:
#                   print("there is no account")
#     elif choice== 5:
#         print("Exit")
#         break
#     else:
#         print("invalid choice")




    
          
          
            

    

