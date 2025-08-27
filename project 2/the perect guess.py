import random
n=random.randint (1, 100)
a =-1
guesses= 0
while (a != n):
    guesses+=1
    a =  int(input("guess a number: "))
    if(a >= n):
       print("lower no. please")
    else:
       (a <=n)
       print("higher no. please")

print(f" you have guessed the number in {guesses} attempt")
