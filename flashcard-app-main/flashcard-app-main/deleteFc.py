# Delete the flashcards

from colorama import Fore
import os
import csv

def delSet(setname):
    file = f'./fcs/{setname}.csv'
    os.unlink(file)
    print(Fore.LIGHTGREEN_EX)
    print(f"Set {setname} deleted successfully..!!")

def delFlashcard(setname, fc, allFcs):
    file = open(f'./fcs/{setname}.csv', 'w')
    fileWriter = csv.DictWriter(file, ['srno','title', 'defn'])
    fileWriter.writeheader()
    i=1
    # print(type(fc))
    for flash in allFcs:
        if int(flash.get('srno')) != fc:
            # print(type(flash.get('srno')))
            # print(fc == flash.get('srno'))
            sr = i
            title = flash.get('title')
            defn = flash.get('defn')
            fileWriter.writerow({'srno':sr, 'title':title, 'defn':defn})
            i+=1           
    
    print(Fore.LIGHTGREEN_EX)
    print("Given Flashcard Deleted Successfully..!!")
    file.close()