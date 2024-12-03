# Create Flashcards Here

import csv, os
from pathlib import Path
from colorama import Fore

# Creating Flash-Card With New Set

def fcViaNewSet(setname):

    file = open(f'./fcs/{setname}.csv', 'w')
    
    writer = csv.DictWriter(file, ['srno',"title", 'defn'])
    writer.writeheader()

    print("Please Enter The Flashcard Details Here")
    print("Enter (wqz) as a Title for Save and Exit the adding terminal..!!")

    i=1
    while True:
        print(Fore.CYAN)
        title = input("Enter The Title : ")
        if(title == "wqz"):
            break
        defn = input("Enter the Definition : ")
        writer.writerow({'srno':i, 'title':title, 'defn':defn})

        print(Fore.LIGHTGREEN_EX)
        print("Flash Card Added Succesfully..!!")

        i+=1

# Creating Flash-Card Via Existing Set

def fcViaExistingSet(setname):
    file = open(f'./fcs/{setname}.csv', 'a')
    fileToRead = open(f'./fcs/{setname}.csv', 'r', newline='')
    
    writer = csv.DictWriter(file, ['srno',"title", 'defn'])

    reader = csv.DictReader(fileToRead, ['srno',"title", 'defn'])
    i = 1
    for line in reader:
        # print(type(line['srno']))
        if not reader.line_num == 1:
            i = int(line['srno'].strip())
            i+=1    
    fileToRead.close()
    print("Please Enter The Flashcard Details Here")
    print("Enter (wqz) as a Title for Save and Exit the adding terminal..!!")

    while True:
        print(Fore.CYAN)
        title = input("Enter The Title : ")
        if(title == "wqz"):
            break
        defn = input("Enter the Definition : ")
        writer.writerow({'srno':i, 'title':title, 'defn':defn})

        print(Fore.LIGHTGREEN_EX)
        print("Flash Card Added Succesfully..!!")
        i+=1