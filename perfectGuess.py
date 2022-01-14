#It is a game in which first the computer chooses a random no. from 1 to 10
#now you have to guess this no.
#it will finally display how many chances you took to guess the no.
import random

def compareGuess(n,c):
    g=int(input("Enter your guess(1,10): ") )
    if g>n: 
        print("Please enter a smaller no.")
        return 0
    elif g<n: 
        print("Please enter a greater no.")
        return 0
    else: 
        print("\nCongo! You guessed it right!")
        c+=1
        return c

generatedNo=random.randint(1,10) #this will store any random no. from [ 1 to 10]
c=0 #used for count
r=0
while r==0:
    r=compareGuess(generatedNo,c)
    c+=1
print("Total no, of chances taken:",r)
