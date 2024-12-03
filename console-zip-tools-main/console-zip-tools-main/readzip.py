"""
    Read Zip Files Here 
"""

# Imports
from colorama import Fore
import zipfile
from pathlib import Path
import os
from pyinputplus import inputFilepath


def readZip():
    print(Fore.CYAN)
    path = inputFilepath("Enter the Path of Zip File : ", allowRegexes=r"""
        ^(.*)
        (\.zip)$
    """)
    path = Path(os.path.abspath(path))
    # print(path)
    if(not os.path.exists(path)):
        print(Fore.LIGHTRED_EX)
        print("Given Path Do Not Exist...!!")
        return None
    
    if(os.path.isdir(path)):
        print(Fore.LIGHTRED_EX)
        print("You Have Given Folder Mate..!!")
        return None
    
    print("Type".center(7), end="")
    print("Name".center(40), end="")
    print("File Size".center(15), end="")
    print("Com. Size".center(15), end="")


    try:
        zip = zipfile.ZipFile(path)
        files = zip.namelist()
        for file in files:
            print(Fore.YELLOW)
            name=file
            info = zip.getinfo(name)
            file_size = info.file_size
            compress_size = info.compress_size
            if Path(file).suffix == "" and file_size==0 and compress_size==0:
                print(Fore.BLUE)
                type = "Dir"
            else:
                type=Path(file).suffix
            print(type.center(7), end="")
            print(name.center(40), end="")
            print(str(file_size).center(15), end="")
            print(str(compress_size).center(15), end="")
        zip.close()
    except zipfile.BadZipFile:
        print(Fore.LIGHTRED_EX)
        print("You Not Given Zip File Or Bad Zip File")