print("----------------welcome to  the game---------------------")

print("choice any one number")
print("press 1 for easy ")
print("press 2 for medium")
print("press 3 for hard")

choice= int(input("choice any of the number amonge three stage :"))

# ready=input("ready for the text:yes/no")

class easy_level():
    def __init__(self,orange,watermelon,mango):
        self.orange=orange
        self.watermelon=watermelon
        self.mango=mango

    def easy(self):
        return("1",self.orange,"2",self.watermelon,"2",self.mango)
    
# obj=easy_level()
# print(obj.easy)

class medium_level(easy_level):
    def __init__(self,orange,watermelon,mango,banana,graps,apple):
        super().__init__(orange,watermelon,mango)
        self.banana=banana
        self.graps=graps
        self.apple=apple

    def medium(self):
        return("4",self.banana,"5",self.graps,"6",self.apple)  
# obj=medium_level()
# print(obj.medium)      

class hard_level(medium_level):
    def __init__(self,orange,watermelon,mango,banana,graps,apple,strawberry,blueberry,raseberry,pepaya):
        super(). __init__(orange,watermelon,mango,graps,banana,apple)
        self.strawberry=strawberry
        self.bluberry=blueberry
        self.raseberry=raseberry
        self.pepaya=pepaya

    def hard(self):
        return("7",self.strawberry,"8",self.bluberry,"9",self.raseberry,"10",self.pepaya)    
import os
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
# obj=hard_level()
# print(obj.hard)    
def func():
    clr()
    vv = int(input(' enter the number of orange'))
    if vv == 1:
        print(' correct answer ')
    elif int(input(' enter the number of watermelon ')) == 2:
        print(' corect answer ')
    elif int(input(' enter the number of mango ')) == 3:
        print(' corect answer ')
    else:
        print(' incorrect ')
    
if choice==1:
    obj=easy_level('orange','watermelon','mango')

    print(obj.easy())
    func()
elif choice==2:
    obj=medium_level('orange','watermelon','mango','banana','graps','apple')
    print(obj.medium())      
elif choice==3:
    obj=hard_level("orange","watermelon","mango","banana","graps","apple","strawberry","blueberry","raseberry","pepaya")
    print(obj.hard())


# class game():
#     def no (self):
#         a=(input("enter your number"))
#         while a==obj:
#             print("you earned 1 point")
#         if     
#         else:
#             print("do you wish to continue:")

#             print("press 1 for continue")
#             print("press 2 for the exit")    
# obj=game()
# obj.no()                        
    






    


       
