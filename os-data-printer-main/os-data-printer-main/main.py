# Create the System Data Displayer
import normal, func
import sys
try:
    import psutil, os
    from colorama import Fore
    from pathlib import Path
    import requests
except:
    print("Sorry, it seems you haven't install the required packeges")
    print("Run : ")
    print("\t pip install psutil")
    print("\t pip install colorama")
    sys.exit()
    

while True:
    normal.printBrand("System Data Displayer")
    ch = normal.myMenu(["Show Battery Status","Show Disk Status","Show Other Data","Display The File","About Me","Exit"])

    if ch == 1:
        func.displayBattery()
    elif ch == 2:
        func.displayDisk()
    elif ch == 3:
        func.displayOther()
    elif ch == 4:
        func.displayLarge()
    elif ch == 5:
        normal.aboutMe()
    elif ch == 6:
        normal.quitMe()