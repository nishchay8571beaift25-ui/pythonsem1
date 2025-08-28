
# n = int(input("Enter number of star rows"))

# for i in range(1, n+1):
#     print("*" * i,)


rows=int(input(" enter a number"))
for i in range(1 , rows+1):
    for j in range(i):
        print("*", end=" ")
    print()
 

