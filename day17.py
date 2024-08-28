# bank system 


class bal_enquiry():
    def __init__(self):
        self.balance=100000
    def my_balance(self):
        print("my balance enquiry:",self.balance)

class my_deposit(bal_enquiry):
    def deposite(self,amount,balance):
      print("amount you want to deposite",amount)    
      print("balance after deposite money:",amount+balance)

class my_withdraw(bal_enquiry):
    def withdraw(self,amount,bal):
        print("amount you want to withdraw:",amount)
        print("balance shown after withdrawing:",bal-amount)
print("press 1 for balance enquiry")
print("press 2 for deposite")
print("press 3 for withdraw")

choice=int(input("enter your choice number:"))

if choice==1:
    obj=bal_enquiry()
    obj.my_balance()
elif choice==2:
    obj=my_deposit()
    amount=int(input("enter amount you want to deposite:"))
    obj.deposite(amount,obj.balance)    

elif choice==3:
    obj=my_withdraw()
    amount=int(input("enter amount you want to withraw"))
    obj.withdraw(amount,obj.balance)    


# https://www.w3schools.com/python/python_inheritance.asp
# que practice

# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("welcome to the college")

# hello=person("john",36)
# print(hello.name)
# print(hello.age)


# class person():
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def hello(self):
#         print("welcome to the group:",self.fname,self.lname)    

        
# obj=person("john","winston")
# # obj.fname()
# # obj.lname()   
# obj.hello()

# anoher method of doing this
# class person():
#     def __init__(self,fname,lname):
#         self.a=fname
#         self.b=lname
# obj=person("john","winston")

# print(obj.a,obj.b)

# bank system practice


class bal_enquiry():
    def __init__(self):
        self.balance=100000
    def my_balance(self):
        print("my balance:",self.balance)
# obj=bal_enquiry()
# obj.my_balance()  

# class my_deposite(bal_enquiry):
#     def deposite(self,amount,balance):
#         print("how much amount to deposite:",amount)
#         print("balance shown after deposite:",amount+balance)

# # obj=my_deposite()
# # obj.deposite(50000,obj.balance)  

# class my_withdraw(bal_enquiry):
#     def withdraw (self,amount,balance):
#         print("how much you want to withdraw:",amount)
#         print("how much balance left after withdrawn:",balance-amount)

# # obj=my_withdraw()
# # obj.withdraw(50000,obj.balance)            
  

# print("press1 for balance enquiry:")
# print("press2 for deposite:")  
# print("press3 for withdrawn:")  

# choice=int(input("enter your choice number:"))

# if choice==1:
#     obj=bal_enquiry()
#     obj.my_balance()  

# elif choice==2:
    
#      obj=my_deposite()
#      amt=int(input("enter your amount you want to deposite"))
#      obj.deposite(amt,obj.balance)  
# elif choice==3:
#     obj=my_withdraw()
#     amount=int(input("enter money you with to withdraw"))
#     obj.withdraw(amount,obj.balance)            
  













          





