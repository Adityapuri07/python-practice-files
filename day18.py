# # exceptionn handling
# try:
#     a = int(input(' enter first number '))
#     b = int(input(' enter second number '))
#     print(a+b)
# except:
#     print(' some error please enter valid input ')



# try:
#     ls=[2,4,6,8,10,12,14]
#     for a in ls:
#         print(a,"hello india")

# except Exception as e:
#     print(e)


# try:
#     for a in range(10):
#         print(b)
# except Exception as e :
#     print(e)       

# try:
#     amt=1000
#     if amt<500:
#         print("mercy")
# # except:
# try:
#   marks = 10000
#   a = marks / 0
#   print(a)
# except Exception as e:
#   print(e)

# practice
# try:
#     x=1000
#     y="hello"
#     print(x+y)
# except Exception as e:
#     print(e)              


# try:
#     for i in range(10):
#         print(i,(10-i)*"*")
# except Exception as e:
#     print(e
#           )        

# try:
      
#       n=int(input("ennter your no"))
#       while n !=1234:
#        print(n)
#        n=int(input("enter ur number again"))
# except Exception as e:
#     print(e)

try:
    vv=int(input("enter your name"))
    if vv=="aditya":
        print("login accepts")
    else:
        print("not loggined")  
except Exception as f:
    print(f)          
