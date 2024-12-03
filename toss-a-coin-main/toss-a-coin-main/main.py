# Create Toss Game
import sys
try:
    from colorama import Fore
except:
    print("Sorry, it seems you haven't install the required packeges")
    print("Run : ")
    print("\t pip install colorama")
    sys.exit()
from random import shuffle
import normal
from time import sleep

# Functions For Toss
def spinACoin():
    choices = ['heads', 'tails']
    shuffle(choices)
    toss = choices[0].title()
    return toss

while True:
    normal.printBrand("Toss A Coin")
    ch = normal.myMenu(["Just Spin A Coin","Contest With A Friend","About Me","Quit"])
    if ch == 1:
        print(Fore.WHITE)
        print("Spinning A Coin . ", end='')
        for i in range(0, 5):
            print('. ',end='')
        print(Fore.LIGHTGREEN_EX)
        sleep(3)
        print("It is ",spinACoin(),"..!!")
    elif ch == 2:
        person1 = input("Name of who needs Heads : ").title()
        person2 = input("Name of who needs Tails : ").title()
        chances = int(input("Enter the number of chances : "))
        pt1 = 0
        pt2 = 0
        for i in range(chances):
            print(Fore.WHITE)
            print("Spinning A Coin ... ", end='')
            sleep(3)
            toss = spinACoin()

            if toss == "Heads":
                print(Fore.LIGHTGREEN_EX)
                print(f"{person1} has won the round, it was {toss}..!!")
                pt1+=1
            elif toss == "Tails":
                print(Fore.LIGHTMAGENTA_EX)
                print(f"{person2} has won the round, it was {toss}..!!")
                pt2+=1
            sleep(1)
            normal.printBrand("Score-Board", color=Fore.YELLOW)
            print(f"{person1} - {pt1}")
            print(f"{person2} - {pt2}")
        if pt1>pt2:
            print(Fore.LIGHTGREEN_EX)
            res = f"{person1} has won the game by {pt1}-{pt2}"
            print('*'*(len(res)+20))

            print('='*(len(res)+20))
            print(res.center(len(res)+20))
        elif pt2>pt1:
            print(Fore.LIGHTMAGENTA_EX)
            res = f"{person2} has won the game by {pt2}-{pt1}"
            print('*'*(len(res)+20))
            print('='*(len(res)+20))
            print(res.center(len(res)+20))
        else:
            print(Fore.CYAN)
            res = f"Match has been Tied by {pt1}-{pt2}"
            print('*'*(len(res)+20))
            print('='*(len(res)+20))
            print(res.center(len(res)+20))
        
        print('='*(len(res)+20))
        print('*'*(len(res)+20))
    elif ch == 4:
        normal.quitMe()
    elif ch == 3:
        normal.aboutMe()