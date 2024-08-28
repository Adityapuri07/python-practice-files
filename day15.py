
# # inheritance

# # class A:
# #     def demo(self):
# #         print(' my demo file')
# #     def welcome(self):
# #         print('-------------------')
# # class B(A):
# #     def subject(self):
# #         print(' my second class')
# # # vv=A()

# # a=B()
# # a.subject()
# # a.demo()


# # class hello():
# #     def student(self):
# #         print("enter your name:")
# #     def medium(self):
# #         print("medium course:")
# # class subject(hello):
# #      def choice(self):
# #        print("subject  selection")

# # vv=subject()
# # vv.choice()
# # vv.student:

# # class balance_enquiry:
# #     def my_balance(self):
# #         print('your current balance  is : 8000000')
# # class withdraw(balance_enquiry):
# #     def withdraw_balance(self):
# #         print(' the money you withhdraw is 89898')
# # obj = withdraw()
# # obj.withdraw_balance()
# # obj.my_balance()



# class bank_enquiry():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def bank_enquiry(self):     
#         print("money enquiry",self.a+self.b)
# class balance_withdraw(bank_enquiry):
#     def withdraw(self):
#         print("money withdrown ",self.a-self.b)
# aa=int(input("enter number to withdraw"))
# vv=balance_withdraw(100000,aa)
# vv.bank_enquiry()
# vv.withdraw()



# class bank_enquiry():
#     def __int__(self,a,b):
#         self.a=a
#         self.b=b
#     def deposit(self):
#         print("deposited amount:",self.a+self.b)

#     def enquiry(self):
#         print("available amount:",self.a)

# class bank_wthdraw(bank_enquiry):

#     def withdraw(self):
#         print("money withrown from available balance:",self.b)
#     def available_balance(self):
#         print("available balance left in the account:",self.a+self.b)

# vv=bank_wthdraw(bank_enquiry)










    


