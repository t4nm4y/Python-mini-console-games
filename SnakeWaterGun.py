# its a snake water gun game
# its similar to stone paper and scissors.
import random
def game( c,p):
        if(c==p): 
            print("comp chose",c)
            return None

        elif(c=='s' and p=='w'): 
            print("comp chose",c) 
            return False
        elif(c=='w' and p=='g'): 
            print("comp chose",c)
            return False
        elif(c=='g' and p=='s'):
            print("comp chose",c)         
            return False

        else: 
            print("comp chose",c)
            return True
    
print("Comp turn started.")
RandComp=random.randint(1,3)  #this will chose any random int from 1 to 3 ie.(1,2 or 3)
if RandComp==1: comp='s'
elif RandComp==2: comp='w'
else: comp='g'
print("Comp turn finished.")

p=input("Player's turn. Choose: Snake(s), Water(w) or Gun(g) ")
a=game(comp,p)
if a==None: print("Its a draw.")
elif a==True: print("You won!:)")
else: print("You Loose :(")