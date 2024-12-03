# Update FlashCard

from colorama import Fore
import csv

def updateFlashcards(fc, setname, allFcs):
    print(Fore.CYAN)
    new_title = input("Enter new title : ")
    new_defn = input("Enter the New Definition : ")

    file = open(f'./fcs/{setname}.csv', 'w')
    fileWriter = csv.DictWriter(file, ['srno', 'title', 'defn'])
    fileWriter.writeheader()

    i=1

    for line in allFcs:
        if int(line.get('srno')) == fc:
            fileWriter.writerow({'srno':i, 'title':new_title, 'defn':new_defn})
        else:
            sr = i
            title = line.get('title')
            defn = line.get('defn')
            fileWriter.writerow({'srno':sr, 'title':title, 'defn':defn})
        i+=1
    
    print(Fore.LIGHTGREEN_EX)
    print("Flashcard Updated Successfully..!!")
