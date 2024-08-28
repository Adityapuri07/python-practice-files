# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def display_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary:.2f}"


# class Manager(Employee):
#     def __init__(self, name, age, salary, department):
#         super().__init__(name, age, salary)
#         self.department = department

#     def display_info(self):
#         return f"{super().display_info()}, Department: {self.department}"


# class Developer(Employee):
#     def __init__(self, name, age, salary, programming_language):
#         super().__init__(name, age, salary)
#         self.programming_language = programming_language

#     def display_info(self):
#         return f"{super().display_info()}, Programming Language: {self.programming_language}"


# manager = Manager("Alice", 35, 80000, "Engineering")
# print(manager.display_info())

# emp = Employee('kk',77,80000)
# print(emp.display_info())





# class employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def display_info(self):
#      return ("name",self.name,"age",self.age,"salary",self.salary)

# obj=employee("john",55,50000)
# print(obj.display_info)

# class emp_dep(employee):
#     def __init__(self,name,age,salary,department):
#         super().__init__(name,age,salary)
#         self.depart=department
#     def hello(self):
#         return  (super().display_info(),"department",self.depart)
# # obj=emp_dep("john",35,50000,"engenering")
# # print(obj.hello)


# class developer(emp_dep):
#     def __init__(self,name,age,salary,department,programeer):
#         super().__init__(name,age,salary,department)
#         self.programeer=programeer
#     def mnc(self):
#         return (super().hello(),"developer:",self.programeer)    
    
# obj=developer("john",55,50000,"engeneering","coumputer application")
# print(obj.mnc()) 


# using of super 

class employee():
    def __init__ (self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):
     return("name:",self.name,"age:",self.age,"salary:",self.salary)

obj=employee("john",55,50000)
print(obj.display())     