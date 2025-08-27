num = int(input("Enter a number: "))

if num > 100 and num % 5 == 0:
    print(f"{num} is greater than 100 and divisible by 5.")
else:
    print(f"{num} does not satisfy the condition.")
