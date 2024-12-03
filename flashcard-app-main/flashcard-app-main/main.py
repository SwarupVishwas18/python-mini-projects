"""
    Flashcard App Using Python : Swarup Deepak Vishwas
"""

# Built In Imports
from colorama import Fore

# Custom Imports
import menu
from abtus import printAbout
import createFc, updateFc

while True:
    # Print Label

    menu.printLabel()

    ch = menu.mainMenu()

    if ch==1:
        ch_2 = menu.createMenu()

        if ch_2==1:
            setname = input("Enter The Name of Set : ")
            createFc.fcViaNewSet(setname)
        elif ch_2==2:
            ch = menu.showAllSets()
            createFc.fcViaExistingSet(ch)
        else:
            continue
    elif ch==2:
        menu.reviewMenu()
    elif ch==3:
        fc, setname, allFcs = menu.showAllFc()
        updateFc.updateFlashcards(fc, setname, allFcs)
    elif ch==4:
        menu.deleteMenu()

    elif ch==5:
        printAbout()
    else:
        print(Fore.LIGHTGREEN_EX)
        print("Thanks For Using FlashCard App")
        print()
        break
