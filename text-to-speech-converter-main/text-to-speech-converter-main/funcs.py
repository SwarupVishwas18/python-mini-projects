# Functions Needed For This Application
from colorama import Fore
import os
from gtts import gTTS
import normal

# Convert whole text file
def convertFileToAudio():
    print(Fore.YELLOW)
    print()
    path = input("Enter the path of file : ")
    path = os.path.abspath(path)
    data = open(str(path),'r').read()
    if not checkText(data):
        return None
    try:
        aud = gTTS(text=data, lang='en', slow=False)
    except:
        print(Fore.RED)
        print("Make sure you are connected to internet")
    aud.save("auds\speech.mp3")
    os.system('auds\speech.mp3')
    print()
    print()
    normal.printBrand("Your File Data", symbol="-")
    print(data)

# Convert User Input into audio
def convertUserInput():
    print(Fore.YELLOW)
    print("Enter wqz in new line to quit")
    print("Enter the text : ")
    text = ''
    while True:
        i = input()
        if i == 'wqz':
            break
        text += (i+'\n')
    if not checkText(text):
        return None
    try:
        aud = gTTS(text=text, lang='en', slow=False)
    except:
        print(Fore.RED)
        print("Make sure you are connected to internet")
    aud.save("auds\speech.mp3")
    os.system("auds\speech.mp3")
    print()
    print()
    normal.printBrand("Your Text Data", symbol="-")
    print(text)

def checkText(text):
    texts = text.split()
    if len(texts) > 5:
        return True
    else:
        print(Fore.RED)
        print("Data must have atleast 5 words..!!")
        return False