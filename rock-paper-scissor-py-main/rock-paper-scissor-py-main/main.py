from random import *
from colorama import Fore
from time import sleep
# Project Name : ROCK PAPER SCISSOR
# Name of Developer : Swarup Deepak Vishwas
# Date : 21-Jan-2022

# ########################## GLOBAL VARIABLES #########################

print(Fore.MAGENTA)

gap_denoter = "----------------------------------------------------"

story_text = """
    So, you are Member of Dumbledore's Army and ROCK PAPER SCISSOR's CHAMPION 😉\n
    And You need to win over Voldermort\n
    So for that you are playing ROCK PAPER SCISSOR with BELLATRIX\n
    All of humainty's fate is decide in this ONE MATCH..!!\n
    There will be five rounds!
"""

user_won = 0
bella_won = 0
round = 1
tie_num = 0

# ########################## NECESSARY FUNCTIONS #########################

# Function Returning User Choice


def randChoice():
    choice = randint(1, 3)
    sleep(1)
    if choice == 1:
        print(Fore.GREEN)
        print("Bella's choice is Rock  ")
        return 'R'
    elif choice == 2:
        print(Fore.WHITE)
        print("Bella's choice is Paper ")
        return 'P'
    elif choice == 3:
        print(Fore.LIGHTBLUE_EX)
        print("Bella's choice is Scissor ")
        return 'S'
    else:
        pass

# Function Containing all the logic


def code_logic(user, bella):
    sleep(1)
    if bella == 'R':
        if user == 'R':
            return 'Tie'
        elif user == 'P':
            return 'Win'
        else:
            return 'Lose'
    elif bella == 'P':
        if user == 'P':
            return 'Tie'
        elif user == 'S':
            return 'Win'
        else:
            return 'Lose'
    elif bella == 'S':
        if user == 'S':
            return 'Tie'
        elif user == 'R':
            return 'Win'
        else:
            return 'Lose'


# ########################## PRINT STORY #########################

def main():
    print(gap_denoter)
    print(story_text)
    print(gap_denoter)

    # ########################## TAKE USER NAME #########################

    print(Fore.CYAN)
    user_name = input("But what is your name : ").title()
    print(gap_denoter)
    print("\nHi, ", user_name, " I am HBP, organizer of ROCK PAPER SCISSOR game")
    print(gap_denoter)

# ########################## TAKE USER CHOICE #########################

    while round <= 5:
        print(Fore.YELLOW)
        print(gap_denoter)
        print("ROUND ", round)
        print(gap_denoter)

        user_choice = input('What is Your Choice(r/p/s) : ')
        user_choice = user_choice.upper()  # convert choice to upper case
        if not (user_choice == 'R' or user_choice == 'P' or user_choice == 'S'):
            print(Fore.RED)
            print("You Gave Wrong Option Mate..!!")
            continue
        bella_choice = randChoice()

        result = code_logic(user=user_choice, bella=bella_choice)
        sleep(3)
        if result == 'Win':
            user_won = user_won + 1
            print(Fore.LIGHTGREEN_EX)
            print("You have Won..!!")
            print("World still has Hope..!!")
        elif result == 'Lose':
            bella_won = bella_won + 1
            print(Fore.LIGHTRED_EX)
            print("Alas, you lose..!!")
            print("Please do something ", user_name)
        else:
            tie_num = tie_num + 1
            print(Fore.LIGHTBLUE_EX)
            print("It is Tie")

        print(gap_denoter)
        print(gap_denoter)

        print(Fore.YELLOW)
        sleep(2)
        print("SCORE BOARD")
        print("Total Round : ", round)
        print("%s points : %d" % (user_name, user_won))
        print("Bella points %d: " % bella_won)
        print("Tie Matches : ", tie_num)
        if round == 5:
            print("OK SO TOTAL SCORE IS UP")
            sleep(4)
            print("Your score : %d\tBella's score : %d" % (user_won, bella_won))
            print(gap_denoter)
            if bella_won < user_won:
                print(Fore.LIGHTGREEN_EX)
                print("WE WON THE WIZARDING WAR")
            elif bella_won > user_won:
                print(Fore.LIGHTRED_EX)
                print("WE LOSE THE WIZARDING WAR")
            else:
                print(Fore.CYAN)
                print("SCORE UNDECIDED AS IT IS TIED")
        round = round+1
        print(Fore.YELLOW)
        print(gap_denoter)

    print(Fore.MAGENTA)
    print("="*40)
    print("Name : Swarup Deepak Vishwas".center(40))
    print("Github : @SwarupVishwas18".center(40))
    print("Instagram : @swarup.vishwas".center(40))
    print("Built With Peace 💝".center(40))
    print("="*40)

    print(Fore.WHITE)

    quitMe()


def quitMe():
    print(Fore.GREEN)
    print("#"*50)
    print("Thanks For Using Our Software".center(50))
    print("#"*50)
    print()
    print(Fore.WHITE)
    exit()

try:
    main()
except:
    quitMe()