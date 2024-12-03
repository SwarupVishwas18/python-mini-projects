"""

    TOPIC : Create The Project That Ca Perform Various Zip Files
    AUTHOR : Swarup Deepak Vishwas

"""

# Imports Here ⭐

from colorama import Fore  # For Colors

# Custom Imports 🧐
import menu
import abt
import extract
import readzip
import compress

while True:
    ch = menu.mainMenu()

    if(ch=='1'):
        extract.extractZip()
    elif(ch=='2'):
        readzip.readZip()
    elif(ch=='3'):
        com = menu.compressMenu()
        if(com=='1'):
            compress.compressViaFolder()
        elif(com=='2'):
            compress.compressViaExt()
        else:
            print(Fore.LIGHTRED_EX)
            print("Incorrect Option")
    elif(ch=='5'):
        print(Fore.LIGHTGREEN_EX)
        print("Thanks For Using Software..!!")
        print()
        break
    elif(ch=='4'):
        abt.info()
    else:
        print(Fore.LIGHTRED_EX)
        print("Sorry But Wrong Choice Mate..!!")