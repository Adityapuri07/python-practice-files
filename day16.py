# multilevel inheritance 
# multiple inheritance
# class A:
#     def helo(self):
#         print(' ok good ')
# class B():
#     def second_class(self):
#         print(' this is my second class')
# class C(B,A):
#     def third_class(self):
#         print(' this is my third class ')
# obj = C()
# obj.helo()
# obj.second_class()
# obj.third_class()


# multi level inheritance
# example

# class hello_name():
#     def first_name(self):
#         print("aditya")

# class hello_middle(hello_name):
#     def midle_name(self):
#         print("@")

# class hello_surname(hello_middle):
#     def surname(self):
#         print("puri")


# obj=hello_surname()
# obj.first_name()
# obj.midle_name()
# obj.surname()

# example of multiple inheritance/

# class team_1():
#     def football(self):
#         print("no1")

# class team_2():
#     def tennis(self):
#         print("no2")

# class team_3(team_2,team_1):
#     def table_tennis(self):
#         print("no3")

# hello=team_3()
# hello.football()
# hello.table_tennis()
# hello.tennis()



# class calcultor():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("add both value:",self.a+self.b)

# class sum(calcultor):
#     def summ(self):
#         print("subtract :",self.a-self.b) 
# class multi(calcultor):
#     def multiply(Self):

#         print("multiply:",Self.a*Self.b)

# v=int(input("enter number"))
# a=int(input("enter another number"))

# obj=multi(v,a)
# obj.add()
# obj.multiply()
# obj.summ()


# print("press 1 for add")
# print("press 2 for subject")
# print("press 3 for subtract")
# print("press 4 for div")

# # vv=int(input("enter your first required number:"))
# # xx=int(input("enter your second required number:"))

# choice=int(input("enter your choice number"))

# class calculator():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         print("sum of both digit:",self.a+self.b)

# class operator():
#     def sub (self):
#         print("subtract off both number :",self.a-self.b)

# class multi_inheritance(calculator,operator):

#     def multi(self):
#         print("multiply both number",self.a*self.b)

# class divident(multi_inheritance):
#     def div(self):
#         print("get me divident of both number:",self.a/self.b)

# vv=int(input("enter your first required number:"))
# xx=int(input("enter your second required number:"))

# obj=divident(xx,vv)

# # obj.multi()
# # obj.div()  
# # obj.sub()


# if choice==1:
#     obj.add()
# elif choice==2:
#     obj.sub()
# elif choice==3:
#     obj.multi()
# elif choice==4:
#     obj.div()

class balance_enquiry:
    def __init__(self,bal):
        self.balance = bal 
    def my_balance(self):
        print(' your current Balance is : ',self.balance)
class deposit(balance_enquiry):
    # def __init__(self,depo):
    def deposit_amount(self,depo):

        print(' you deposit the money :',depo)
        print(' the updated amount is :',self.balance+depo)


class withdrow(deposit):
    def withdraw_amount(self,withdraw):
        print("how much you want to  withdrawn",withdraw)
        print("current amount after withdrawn:",self.bal-withdraw)    



obj = balance_enquiry(100000)




print(' -------------- welcome to hdfc bank ------------')
print(' press 1 for balance enquiry ')
print(' press 2 for Deposit ')
print(' press 3 for Withdraw ')
choice = int(input(' enter your choice '))
if choice == 1:
    obj.my_balance()
elif choice == 2:
    amnt = int(input(' how much amount you want to deposit '))
    dep = deposit(amnt)
    dep.deposit_amount(amnt)
elif choice == 3:
    amnt = int(input(' how much amount you want to withdraw '))
    wit = withdrow(amnt)
    wit.withdraw_amount(amnt)





print("________________welcome to state bank of india________________")

print("press 1 for balan_enquiry")
print("press 2 for deposit")
print("press 3 for withdraw")

choice=int(input("enter your choice option"))

class bank_enquiry():
    def __init__(self,balance):
        self.bal=balance
        print("check your curreny balance:",self.bal)

class deposit_amount(bank_enquiry):
    def __init__(self,deposite,bal):
        self.depo=deposite
        self.bal = bal

        print("enter your deposit amount",self.depo)
        print("current balancce after deposited amount:",self.bal+self.depo)


class withdraw_amount(deposit_amount):
    def __init__(self,withdraw):
        self.takeout=withdraw

        print("how much amount to be withdraw:",self.takeout)
        print("available_balance after withdrawn :",self.bal-self.takeout)  
if choice==1:
    obj=bank_enquiry(5000000000)

elif choice==2:
    ob = bank_enquiry()
    amount=int(input("enter amount hoe much you want to deposite "))
    obj =deposit_amount(amount,ob.bal)
elif choice==3: 
    amt=int(input("how much ou want to deposite:"))
    obj = withdraw_amount(amt)



    

    


    




# # practice multilevel


 
















