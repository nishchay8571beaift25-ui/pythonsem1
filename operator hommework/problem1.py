num1=float(input("enter the number : "))
num2=float(input("enter the number : "))
calculation=input("enter sign :")

sum=(num1+num2)

diff=(num1-num2)

product=(num1*num2)

divide=(num1/num2)

if calculation == "+":
    print("sum of numbers is ",sum)
elif(calculation=="-"):
    print("diff of number is ",diff)
elif(calculation=="*"):
    print("product of number is ", product)
elif(calculation=="/"):
    print("diffrence if number is ",divide)
else:
    print("enter a calculation sign")
