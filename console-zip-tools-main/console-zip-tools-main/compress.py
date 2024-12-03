"""
    COMPRESS ZIPS HERE
"""

import pyinputplus as pyip
import shutil
from pathlib import Path
import os
import zipfile
from colorama import Fore

def compressViaExt():

    opts = ["jpg","png","pdf","other"]

    print(Fore.CYAN)

    ch = pyip.inputMenu(opts, prompt="Choose The File Extension : ")

    if(ch=="other"):
        ch = input("Enter The Extension : ")


    #  Paths Needed..!!
    home = Path.home()
    if(not os.path.exists(Path.cwd()/'zips')):
        os.mkdir(Path('./zips'))
    folder = Path.cwd()/'docs'


    os.mkdir('docs')

    zip = zipfile.ZipFile(Path('./zips')/(ch+'.zip'), 'w')

    for f, sub, files in os.walk(home):
        for file in Path(f).glob(f'*.{ch}'):
            if(not (Path(f)/file).is_dir()):
                print(f"Copied : {file}" )
                try:
                    shutil.copy(Path(f)/file, folder)
                except shutil.SameFileError:
                    continue

    print(Fore.YELLOW)

    for f, sub, files in os.walk(folder):
        for file in files:
            try:
                zip.write(Path('./docs/')/file)
            except shutil.SameFileError:
                continue
            print(f"Compressing : {file}...")

    shutil.rmtree(folder)
    zip.close()
    print(Fore.LIGHTGREEN_EX)
    print("Done..!!")



def compressViaFolder():
    
    print(Fore.CYAN)
    path = pyip.inputFilepath("Enter the Path of Folder : ")
    path = Path(os.path.abspath(path))
    # print(path)
    if(not os.path.exists(path)):
        print(Fore.LIGHTRED_EX)
        print("Given Path Do Not Exist...!!")
        return None
    
    if(not os.path.isdir(path)):
        print(Fore.LIGHTRED_EX)
        print("You Have Not Given Folder Mate..!!")
        return None
    
    
    
    

    shutil.make_archive(Path('zips')/path.stem, 'zip', path)
    print(f"Compressing : {path.stem}...")
    print(Fore.LIGHTGREEN_EX)
    print("Done..!!")

