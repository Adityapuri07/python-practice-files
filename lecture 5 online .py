# loops
# loops are used to repeat functions

# while and for 

# for example

# a=1
# while  a<=10:
#     print(a,"hello")
#     a=a+1

# v=1
# while v<=100:
#     print(v,"puri")
#     v=v+1

# if we want to use a decending order counting 

# a=10
# while a>=1:
#  print(a)
#  a=a-1

# a=100
# while a>=1:
#  print(a)
#  a=a-1


# practice ques
# ques 1

# a=1
# while a<=100:
#     print(a)
#     a=a+1


# ques2
# i=100
# while i>=1:
#     print(i)
#     i-=1


# ques 3

# n=1
# while n<=10:
#     print(5*n)
#     n=n+1

# v=1
# while v<=20:
#     print(10*v)
#     v=v+1

# v=int(input("enter your number:"))
# while v<=10:
#     print(4*v)
#     v=v+1

# v=int(input("enter number:"))
# n=1
# while n<=10:
#     print (v*n)

#     n=n+1

# how to make password
# v=(input("enter your password:"))
# while v!="adi":
#       print(v)
#       v=(input("enter your password:"))

# one more example
# v=int(input("enter your number:"))
# n=1
# while n<=10:
#     print(v,"x",n,"=",n*v)
#     n=n+1



# ques4

# list=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<=len(list):
#     print(list[idx])
    # idx=idx+1


# ques5
# num=(1,4,9,16,25,36,49,64,81,100)
# x=25
# i=0
# while i<=len(num):
#     if(num[i]==x):
#      print("found",i)
#     i=i+1


# break condition 

# i=10
# while i<=20:
#     print(i)
#     if i==15:
#         print("found")
#         break
#     # else:
#     #     print("finding")
    # i=i+1

# num=(20,25,26,28,30,36,40)
# x=28
# i=0

# while i<len(num):
#     if(num[i]==x):
#         print("found",i)
#         break
#     else:
#         print("finding")
#     #     # break
#     i=i+1        

# print("end of loop")

# for continue

# i=1
# while i<=5:
#     if (i==3):
#         i=i+1
#         continue #work as skp
#     # i=i+1
#     print(i)
#     i=i+1


# i=1
# while i<=10:
#     if(i%2==0):
#         i=i+1
#         continue
#     print(i)
#     i=i+1

# for condition
# it is used for sequential traversal intuple.string,list


# hello=["patato","onion","green finger" ,"mushroom"]
# for val in hello:
#     print(val)

# name="apnacollege"
# for char in name:
#     print(char)

# use of else in loop 

# str="helloindia"
# for val in str:
    
#     print(val)
# else:
#     print("end")    


# str="helloindia"
# for val in str:
#     if val=="o":
#         print("found")
#         break
    
#     print(val)
# else:
#     print("end")    


# practice question for loop
# 1 ques

# ls=[1,4,9,16,25,36,49,64,81,100]
# for num in ls:
#     print(num)

# # ques 2

# these process of serarching is linear search called 

# num=[2,5,6,8,10,25,35,10]
# x=10
# i=0
# for val in num:
#     if (val==x):
#      print("number found at index:",i)
#     #  break
     
#     i=i+1       
# else:
#    print("end of command")



# make atable
# with Loop
# ls=(1,2,3,4,5,6,7,8,9,10)
# no=int(input("enter your table number:"))
# for a in ls:
#     print(a*no)


# for range function    return the sequence of number
# (start,sstop,step )

# for i in range(2,50,2):#(start,stop,step)
#     print(i)
# and we need odd number in these form 

# for i in range(1,50,2):
#     print(i)


# for i in range(10):
#     print(i)


# practice ques 
# ques1

# for i in range(1,101):
#     print(i)

# ques 2
# for i in range(100,0,-1):
#     print(i)

# ques 3

# n=int(input("enter any number"))
# for i in range(1,11):
#     print(i*n)



# pass statement


# practce ques
# ques1

# n=5
# sum=0
# for i in range(n):
#     sum=sum+i
#     print("total sum of:",sum)

# n=10
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i=i+1
# print(sum)
    
          
# n=5
# fact=1
# i=1
# while i<=n:
#     fact *=i
#     i=i+1
# print(fact)    


# n=10
# fac=1
# for i in range(1,n):
#     fac*=i
# print("factors:",fac)    
    
# n=5
# fac=1
# for i in range(1,n):
#     fac*=i
# print(fac)        

# n=10
# sum=0
# for i in range(1,n):
#     sum+=i
# print(sum)    

# n=10
# sum=0
# i=1

# while i<=n:
#     sum+=i
#     i=i+1
# print(sum)    





    
    



