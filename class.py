# # class is a blueprint or a template 
# class student:
#     def __init__(self,name ,marks):
#         self.name=name
#         self.marks=marks
        
# #waht is object : instace of a class 
# s1=student("neeraj", 90)
# print(s1.name,s1.marks)


# # constructor:
# #__init__




# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def circum(self):
#         return 2*3.14*self.radius
# cir=circle(int(input("enter the radious: ")))
# print(f"circumferce of circle is {cir.circum()}")
    



# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def y_salary(self):
#         return self.salary*12
# e1=employee("Parth",150)
# e2=employee("mehak",150000)
# print(e1.name,"yearly salary is:",e1.y_salary)
# print(e2.name,"yearly salary is",e2.y_salary)    

# class car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model

# c1=car("thar","maruti")
# print(c1.name , c1.model)


# class product:
#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self.discount = discount

#     def last_price(self):
#         return self.price - (self.price * self.discount / 100)


# p1 = product("chai", 100, 10)   
# print(p1.name, p1.price, p1.last_price())  



# class Student:
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def calculate_result(self):
#         total = self.mark1 + self.mark2 + self.mark3
#         percentage = total / 3
        
#         if percentage >= 40:
#             end_result = "Pass"
#         else:
#             end_result = "Fail"
        
#         return total, percentage, end_result



# name = input("Enter student name: ")
# m1 = float(input("Enter marks of Subject 1: "))
# m2 = float(input("Enter marks of Subject 2: "))
# m3 = float(input("Enter marks of Subject 3: "))

# s = Student(name, m1, m2, m3)
# total, percentage, status = s.calculate_result()

# print("Name:", s.name)
# print("Total Marks:", total)
# print("Percentage:", round(percentage, 2))
# print("Status:", status)





#  class BankAccount:
#     def _init_(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#     def withdraw(self, amount):
#         if self.balance-amount < 500:
#             print("Minimum balance of ₹500 must be maintained")
#         else:
#             self.balance -= amount
#         return self.balance
# b1 = BankAccount("Prabhjot", 50000)
# print(b1.name, b1.deposit(1000), b1.withdraw(500))
            





# class Distance:
#     def __init__(self , kilometer):
#         self.kilometer=kilometer
    

#     def meter(self):
#         return self.kilometer*1000
    
#     def centimeter(self):
#         return self.kilometer*100000
    
#     def milimeter(self):
#         return self.kilometer*1000000
    

# d=Distance(5)
# print("meter",d.meter() , "centimeter" , d.centimeter() , "milimeter",d.milimeter())




# class ticket:
#     def __init__(self , name , dis):
#         self.name=name
#         self.dis=dis
#     def fare(self):
#         if self.dis<=5:
#             return self.dis*20
#         firstfive=5*20
#         afterfive=(self.dis-5)*15
#         return firstfive + afterfive
# name=input("enter the name os passenger: ")
# dist=float(input("enter the distance and plz take in kilometer only: "))

# tic=ticket(name,dist)
# fare=tic.fare()
# print("the passenger name is ", tic.name)
# print("the distance is ", tic.dis ,"km")
# print("the total fare is ", fare)

        
        

        
    
