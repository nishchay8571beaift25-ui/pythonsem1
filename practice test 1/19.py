
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter the number to search: "))

for num in numbers:
    if num == search:
        print(f"{search} found in the list!")
        break
else:
    print(f"{search} not found in the list.")