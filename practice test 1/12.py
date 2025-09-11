fruits = ["apple", "banana", "mango", "grapes", "orange"]


item = input("Enter an element to check: ")


if item in fruits:
    print(f" {item} is present in the list.")
else:
    print(f" {item} is not present in the list.")


if item not in fruits:
    print(f"{item} is NOT in the list.")
else:
    print(f"{item} IS in the list.")
