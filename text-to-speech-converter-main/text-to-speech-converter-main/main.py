# Text To Speech Conveter

import normal, funcs


def main():
    while True:
        normal.printBrand("Convert To Speech")
        ch = normal.myMenu(["Convert Whole Text File","Convert Your Own Text","About Me","Exit"])

        if ch == 1:
            funcs.convertFileToAudio()
        elif ch == 2:
            funcs.convertUserInput()
        elif ch == 3:
            normal.aboutMe()
        elif ch == 4:
            normal.quitMe()

try:
    main()
except:
    normal.quitMe()