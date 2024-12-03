"""
    Extract Zip File Here
"""

import shutil
from colorama import Fore
import zipfile
import os
from pyinputplus import inputFilepath
from pathlib import Path

def extractZip():
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
    
    if(not os.path.exists(Path.cwd()/'extracts')):
        os.mkdir(Path('./extracts'))
        os.mkdir(Path('./extracts')/path.stem)
    try:
        zip = zipfile.ZipFile(path)
        zip.extractall(path=Path.cwd()/'extracts'/path.stem)
        zip.close()
    except zipfile.BadZipFile:
        print(Fore.LIGHTRED_EX)
        print("You Not Given Zip File Or Bad Zip File")
    else:
        print(Fore.LIGHTGREEN_EX)
        zipname = Path(path).stem
        print(f"Extracted {zipname} Successfully..!!")


