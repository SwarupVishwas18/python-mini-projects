"""
    This File Contains all code related to menu..
"""

import pyinputplus
from colorama import Fore


# Nothing Just Printing Our Brand..!! 😉

def printLogo():
    print(Fore.CYAN)
    print()
    print('#'*30)
    print("Zip Extractor".center(30))
    print('#'*30)
    print()

def mainMenu():
    printLogo()
    print("Our Choices are : ")
    print()
    print("1. Extract Zip")
    print("2. Read Data From Zip File")
    print("3. Compress File")
    print("4. About us")
    print("5. EXIT..!!")

    print()
    ch = input("Choose Your Option : ")
    return ch

def compressMenu():
    print(Fore.CYAN)
    print("COMPRESS DATA")
    print("1. Compress Folder")
    print("2. Compress All Files Of Extensions")
    print()
    ch = input("Choose Your Option : ")
    return ch
