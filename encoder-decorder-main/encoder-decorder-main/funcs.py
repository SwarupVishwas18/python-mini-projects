
from colorama import Fore
from pyperclip import copy
from pathlib import Path
import os
# All functions needed for Encoding and Decoding

def encrypter():
    print(Fore.YELLOW)
    data = input("Enter the Data : ")
    str = []
    for i in data:
        str.append(chr(ord(i)+5))
    s = ''.join(str)
    print("Encrypted Data is : ")
    print(Fore.LIGHTBLUE_EX)
    print(s)
    copy(s)
    print(Fore.LIGHTGREEN_EX)
    print("Encrypted Data has been copied to clipboard..!!")

def decrypter():
    print(Fore.YELLOW)
    data = input("Enter the Data : ")
    str = []
    for i in data:
        str.append(chr(ord(i)-5))
    s = ''.join(str)
    print("Decrypted Data is : ")
    print(Fore.LIGHTBLUE_EX)
    print(s)
    copy(s)
    print(Fore.LIGHTGREEN_EX)
    print("Decrypted Data has been copied to clipboard..!!")


# Encode file data
def encodeFile():
    print(Fore.YELLOW)
    path = os.path.abspath(input("Enter the Path of text file : "))
    if not Path(path).exists():
        print(Fore.RED)
        print("File Not Found..!!")
        return None
    file = open(path)
    data = file.read()
    str = []
    for i in data:
        str.append(chr(ord(i)+5))
    s = ''.join(str)
    print("Encrypted Data is : ")
    print(Fore.LIGHTBLUE_EX)
    print(s)
    copy(s)
    print(Fore.LIGHTGREEN_EX)
    print("Encrypted Data has been copied to clipboard..!!")

# decode file data
def decodeFile():
    print(Fore.YELLOW)
    path = os.path.abspath(input("Enter the Path of text file : "))
    if not Path(path).exists():
        print(Fore.RED)
        print("File Not Found..!!")
        return None
    file = open(path)
    data = file.read()
    str = []
    for i in data:
        str.append(chr(ord(i)-5))
    s = ''.join(str)
    print("Decrypted Data is : ")
    print(Fore.LIGHTBLUE_EX)
    print(s)
    copy(s)
    print(Fore.LIGHTGREEN_EX)
    print("Decrypted Data has been copied to clipboard..!!")