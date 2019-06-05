from random import *
import sys
x=randint(1,100)
while True:
    n=int(input("enter your guess between 1 to 100 = "))
    if n<x:
        print(f"this is smaller number please try another greater number than this.....number>{n}")
    elif n>x:
        print(f"this is bigger number please try another smaller number than this......number<{n}")
    else:
        print("GOOD JOB! you got that number......")
        e=input("wanna play again if yes than hit any button except N or n = ")
        x=randint(1,100)
        if e=='N' or e=='n':
            print("Have a good day sir")
            sys.exit()
