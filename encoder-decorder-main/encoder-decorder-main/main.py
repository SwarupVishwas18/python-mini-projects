"""
    Name : Swarup Deepak Vishwas
    Project : Encrypter and Decrypter
"""

from colorama import Fore,Back
import normal
import funcs

# Encrypting Function

def main():

    while True:
        normal.printBrand("Encoder and Decoder")
        ch = normal.myMenu(["Encode Text","Decode Text","Encode txt File","Decode txt File","About Me","Quit"])
        
        if ch == 1:
            funcs.encrypter()
        elif ch == 2:
            funcs.decrypter()
        elif ch == 3:
            funcs.encodeFile()
        elif ch == 4:
            funcs.decodeFile()
        elif ch == 5:
            normal.aboutMe()
        elif ch == 6:
            normal.quitMe()
        print(Back.RESET)
        print(Fore.CYAN+"--------------------------------------------------")
        print(Fore.CYAN+"--------------------------------------------------")
        

try:
    main()
except KeyboardInterrupt:
    normal.quitMe()
except:
    print(Fore.RED)
    print("Error Occured..!!")