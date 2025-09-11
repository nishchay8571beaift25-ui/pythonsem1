
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


if a >= b:
    if a >= c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b >= c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)
