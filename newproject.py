class balance_enquiry():
    def __init__(self):
        self.balance = 100000
    def my_balance(self):
        print(' your current balance is : ',self.balance)
# obj=balance_enquiry()
# obj.balance()        

class deposit(balance_enquiry):
    def deposit_amount(self,amount,clr_balance):
        print(' your deposited amount is : ',amount)
        print(' your available balance is :',clr_balance+amount)


class withdraw(balance_enquiry):
    def withdraw_amount(self,amnt,clr_balance):
        print('your withdraw amount is : ',amnt)
        print(' your balance after withdrawn is : ',clr_balance-amnt)

print("________________welcome to state bank of india________________")

print("press 1 for balan_enquiry")
print("press 2 for deposit")
print("press 3 for withdraw")

choice=int(input("enter your choice option"))
if choice==1:
    obj = balance_enquiry()
    obj.my_balance()

elif choice==2:
    obj = deposit()
    dep = int(input(' enter amount you want to deposit : '))
    obj.deposit_amount(dep,obj.balance)
elif choice==3: 
    amt=int(input(' enter amount you want to withdraw : '))
    obj = withdraw()
    obj.withdraw_amount(amt,obj.balance)
    



# bank system   

# class bal_enquiry():
#     def __init__(self):
#         self.balance=100000




