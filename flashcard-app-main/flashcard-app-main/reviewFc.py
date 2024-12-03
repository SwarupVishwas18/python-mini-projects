# Review All Set

import csv
from random import shuffle
from colorama import Fore
import time
import pyinputplus as pyip
from pathlib import Path
import os, sys

def reviewSet(filename):
    file = open(f'./fcs/{filename}.csv')

    fileReader = csv.DictReader(file, ['srno', 'title', 'defn'])
    fcList = list(fileReader)
    shuffle(fcList)
    print(Fore.YELLOW)
    print('#'*40)
    print(f"Review From {filename}".center(40))
    print('#'*40)
    print()
    i = 1
    for row in fcList:
        if row['title'] == 'title':
            continue
        print('-'*100)
        print()
        print(f"Flashcard No : {i}")
        print(f"Q. {row['title']}")
        time.sleep(3)
        print(f"Answer -> {row['defn']}")
        print()
        time.sleep(1)
        i+=1

    try:
        score = pyip.inputNum("Enter Your Correct Answers : ", min=1, max=i-1)
    except:
        print(Fore.RED)
        print("There Are No FlashCards Here..!!")
        sys.exit()
    checkScore(score, filename)
    file.close()

def checkScore(score, setname):
    file = open(f'./code-support-files/scores.csv', 'r')
    fileReader = csv.DictReader(file, ['set', 'score'])
    lines = list(fileReader)
    label = 1
    i=0
    for line in lines:
        if not (line['set'] == 'set' and line['score'] == 'score'):
            if line['set'] == setname:
                if int(line['score'])<score:
                    print(Fore.LIGHTGREEN_EX)
                    print("New High Score Achieved..!!\n Well Done Mate...!!")
                    lines[i].update({'score':score})
                label = 0
        i+=1
    if label == 1:
        print(Fore.LIGHTGREEN_EX)
        print("New High Score Achieved..!!\n Well Done Mate...!!")
        lines.append({'set':setname, 'score':score})

    file.close()
    
    file = open(f'./code-support-files/scores.csv', 'w')
    file.flush()
    fileWriter = csv.DictWriter(file, ['set', 'score'])
    
    for line in lines:
        # print(line)
        fileWriter.writerow({'set':line.get('set'), 'score':line.get('score')})
    

def reviewRemix():
    path = Path('./fcs')

    for f, s, files in os.walk(path):
        for file in files:
            filePath = Path(f)/file
            reviewSet(filePath.stem)
            
def viewAllFlashCards(fc):
    file = open('./fcs/{fc}.csv')
    fileReader = csv.DictReader(file, ['srno','title','defn'])
    srs = []
    print(Fore.CYAN)
    for line in fileReader:
        sr = line['srno']
        srs.append(sr)
        title = line['title']
        defn = line['defn']
        print(f'{sr}. {title} --> {defn}')
    ch = pyip.inputNum("Enter the number of line you want to apply changes to : ", min=min(srs), max=max(srs))
    return ch