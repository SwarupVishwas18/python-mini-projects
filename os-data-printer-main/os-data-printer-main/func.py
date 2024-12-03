# Backend Functions
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
    

# TODO : Create For Battery
def displayBattery():
    battery = psutil.sensors_battery()
    perc = battery[0]
    secsLeft = battery[1]
    isPlugged = battery[2]

    if perc >= 75 or isPlugged:
        print(Fore.LIGHTGREEN_EX)
    elif perc >= 50:
        print(Fore.YELLOW)
    else:
        print(Fore.LIGHTRED_EX)
    print('-'*40)
    print(f"""
    Battery Percentage : {perc}
    Time Till Discharged : {secsLeft//3600} hr and {(secsLeft%3600)//60} min
    Is Charger Plugged : {isPlugged}
    """)
    print('-'*40)

# TODO : Create For Disk
def displayDisk():
    disk = psutil.disk_usage(str(Path.home()))
    total = disk[0]//(1000*1000*1000)
    used = disk[1]//(1000*1000*1000)
    free = disk[2]//(1000*1000*1000)
    per = disk[3]
    if free < used:
        print(Fore.LIGHTRED_EX)
    else:
        print(Fore.LIGHTGREEN_EX)
    print('-'*40)
    print(f"""
    Total Disk Storage : {total} Giga Bytes
    Used Disk Storage : {used} Giga Bytes
    Free Disk Storage : {free} Giga Bytes
    Disk Full Percent : {per} %
    """)
    print('-'*40)


# DONE : Create For Other Data
def displayOther():
    env = os.environ
    print(Fore.YELLOW)
    print('-'*40)
    print(f"\nName Of The Computer : {env['COMPUTERNAME']}")
    print(f"Name Of The User : {env['USERNAME']}")
    print(f"Your Home Path : {env['HOMEPATH']}")
    print(f"Operating System : {env['OS']}")
    print(f"Number of Processor : {env['NUMBER_OF_PROCESSORS']}")
    print(f"Level Of Processors : {env['PROCESSOR_LEVEL']}")
    print(f"Architecture Of Processor : {env['PROCESSOR_ARCHITECTURE']}\n")
    print('-'*40)

def displayLarge():
    partitions = psutil.disk_partitions()
    print(partitions)
    print(Fore.GREEN)
    for part in partitions:
        path = Path(part.mountpoint)

        for f, sub, files in os.walk(path):
            for file in files:
                print(Path(file).stat().st_size)
        