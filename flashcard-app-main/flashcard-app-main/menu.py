# Menu Code Here


import os
from colorama import Fore
import pyinputplus as pyip
from pathlib import Path
import reviewFc, deleteFc
import csv, sys

def printLabel():
    print(Fore.CYAN)
    print('#'*30)
    print("FlashCard".center(30))
    print('#'*30)
    print()

def mainMenu():
    print(Fore.CYAN)
    print("""
    1. Create Flashcard
    2. Review Flashcard
    3. Update Flashcard
    4. Delete Flashcard
    5. About Us
    6. Quit
    """.center(30))

    ch = pyip.inputNum("Enter your choice : ", min=1, max=6)

    return ch

def createMenu():
    print(Fore.CYAN)
    print("""
        1. Create New Set
        2. Add Card To Existing Set
        3. Back To Main Menu
    """)

    ch = pyip.inputNum("Enter your choice : ", min=1, max=3)

    return ch

def showAllSets():
    path = Path('./fcs')
    sets = []

    for f, s, files in os.walk(path):
        for file in files:
            filepath = Path(f)/file
            # print(filepath)    NOTHING JUST TESTING PURPOSE
            # print("File Path Suffix : "+filepath.suffix)
            # print("File Path Stem : "+filepath.stem)
            if filepath.suffix == '.csv':
                sets.append(filepath.stem)
    if len(sets) == 0:
        print(Fore.LIGHTRED_EX)
        print("There is No Set Present..!!")
        sys.exit()    
    ch = pyip.inputMenu(sets, "Enter the set value : \n", blank=True)

    return ch

def reviewMenu():
    print(Fore.CYAN)
    print("""
        1. Review A Set
        2. Remix and Review All Set
        3. Back
    """)
    ch = int(input("Enter your choice : "))

    if ch == 1:
        file = showAllSets()
        reviewFc.reviewSet(file)
    elif ch == 2:
        reviewFc.reviewRemix()
    else:
        return None

def deleteMenu():
    print(Fore.CYAN)
    print("""
        1. Delete Flashcard
        2. Delete Complete Set
        3. Back
    """)

    ch = int(input("Enter the choice : "))

    if ch == 1:
        fc, setname, allFcs = showAllFc()
        deleteFc.delFlashcard(setname, fc, allFcs)
    elif ch == 2:
        setname = showAllSets()
        deleteFc.delSet(setname)
    else:
        return None

def showAllFc():
    setname = showAllSets()
    file = open(f'./fcs/{setname}.csv')
    fileReader = csv.DictReader(file, ['srno', 'title', 'defn'])
    print(Fore.YELLOW)
    i=1
    fcList = []
    for line in fileReader:
        if not (line['srno'] == 'srno'):
            srno = line['srno']
            title = line['title']
            defn = line['defn']
            fcList.append({'srno':srno, 'title':title, 'defn':defn})
            print(f'{srno}. {title} --> {defn}')
    print()
    print()
    fc = pyip.inputNum("Enter your choice : ", max=int(srno),min=1)
    return fc,setname, fcList