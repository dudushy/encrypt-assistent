#imports
import os
import math
import time

#settings
loadAnimation = True
slowMode = False
codes = ['ZENITPOLAR', 'LEET']

#menus
mainMenu = """
-=- -=- -=- -=- -=- -=- -=-
|   Choose a number:    |
|                       |
|   1 > Convert         |
|                       |
|   2 > Settings        |
|                       |
|   3 > EXIT            |
-=- -=- -=- -=- -=- -=- -=-
"""

invalidMenu = """
-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-
|      Invalid input, try again.       |
-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-
"""

#functions
def settingsMenu() -> str:
    return f"""
-=- -=- -=- -=- -=- -=- -=- -=-
=======<Enter the number>=======

===> (1) Load Animation [{loadAnimation}]

===> (2) Slow Mode [{slowMode}]

=======> (3) BACK
-=- -=- -=- -=- -=- -=- -=- -=-
"""

def clearScreen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def waitKeyPress() -> None:
    print(": OK")
    os.system('pause >NUL' if os.name == 'nt' else 'read -s -n 1')

def invalidInput() -> None:
    clearScreen()
    print(invalidMenu)
    waitKeyPress()

def printAllCodesAvaliable() -> None:
    print("\n= AVALIABLE CODES:")
    for code in codes:
        print(f"-- {code}")
    print("- - - - - - -")

def settings() -> None:
    global loadAnimation
    global slowMode

    while True:
        clearScreen()
        print(settingsMenu())
        match input("=> "):
            case "1":
                loadAnimation = not loadAnimation
            case "2":
                slowMode = not slowMode
            case "3":
                return
            case _:
                invalidInput()

def wait(secs: int) -> None:
    if slowMode:
        time.sleep(secs)

def animLoad() -> None:
    load = "|/-\|"
    for i in load:
        clearScreen()
        print(f"{i}\n")
        time.sleep(.1)

def convert():
    #loop //how it works
    while True:
        #request //raw data
        code_msg = ""
        while not code_msg:
            clearScreen()
            print("Please, enter data following the example:"+
                    "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"+
                    "\n|  Example:                          |"+
                    "\n|  MESSAGE: LEET_Hello World!        |"+
                    "\n- - - - - - - - - - - - - - - - - - - -")
            printAllCodesAvaliable()
            code_msg = input("\n-> MESSAGE: ")
        clearScreen()

        #filter
        code = ""
        msg = ""
        print(code_msg)
        for j in code_msg:
            if j == "_":
                break
            code += j
            if slowMode == True:
                print(f"\n{j}\t===\t{code}")
                wait(.1)
        for k in range(((len(code)) + 1), len(code_msg)):
            msg += code_msg[k]
            if slowMode == True:
                print(f"\n{k}\t===\t{msg}")
                wait(.1)
        if slowMode == True:
            print(f"\nCODE: {code}\nMESSAGE: {msg}")
            wait(.4)

        #convert
        if code == "LEET":
            msg = LEET(f"{msg}")

        elif code == "ZENITPOLAR":
            msg = ZENITPOLAR(f"{msg}")
        
        #loading animation
        if loadAnimation:
            animLoad()

        #results
        check = ""
        while check != "y" or "n":
            clearScreen()
            print("%= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =%"+
                    f"\n\t\tMessage: [  {msg}  ]\n"+
                    "\n\t\tRun again?"+
                    "\n%= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =%")
            check = input("\n (y/n): ")
            if check == "y":
                break
            if check == "n":
                break
        if check == "n":
            break

def menu():
    while True:
        clearScreen()
        print(mainMenu)
        match input(" : "):
            case "1":
                convert()
            case "2":
                settings()
            case "3":
                clearScreen()
                print("-=- -=- -=- -=- -=- -=-"+
                    "\n|   Are you sure?   |"+
                    "\n-=- -=- -=- -=- -=- -=-")
                if input(" (y/n): ") == "y":
                    break
            case _:
                invalidInput()

## codes
def ZENITPOLAR(msg_input):  # sourcery skip: switch, use-assigned-variable
    msg_output = ""         #ZENIT
                            #POLAR
    for i in msg_input:
        c = i
        #change to char //lower case
        if i == "z":
            msg_output += "p"
        elif i == "e":
            msg_output += "o"
        elif i == "n":
            msg_output += "l"
        elif i == "i":
            msg_output += "a"
        elif i == "t":
            msg_output += "r"
        elif i == "p":
            msg_output += "z"
        elif i == "o":
            msg_output += "e"
        elif i == "l":
            msg_output += "n"
        elif i == "a":
            msg_output += "i"
        elif i == "r":
            msg_output += "t"
        #upper case
        elif i == "Z":
            msg_output += "P"
        elif i == "E":
            msg_output += "O"
        elif i == "N":
            msg_output += "L"
        elif i == "I":
            msg_output += "A"
        elif i == "T":
            msg_output += "R"
        elif i == "P":
            msg_output += "Z"
        elif i == "O":
            msg_output += "E"
        elif i == "L":
            msg_output += "N"
        elif i == "A":
            msg_output += "I"
        elif i == "R":
            msg_output += "T"
        else:
            msg_output += c
    return msg_output

def LEET(msg_input):  # sourcery skip: use-assigned-variable
    msg_output = ""         #0134567
                            #OIEASGT
    for i in msg_input:
        c = i
        if i == "0":
            msg_output += "O"
        elif i == "1":
            msg_output += "L"
        elif i == "3":
            msg_output += "E"
        elif i == "4":
            msg_output += "A"
        elif i == "7":
            msg_output += "T"
        elif i == "o":
            msg_output += "0"
        elif i == "l":
            msg_output += "1"
        elif i == "e":
            msg_output += "3"
        elif i == "a":
            msg_output += "4"
        elif i == "t":
            msg_output += "7"
        elif i == "O":
            msg_output += "0"
        elif i == "L":
            msg_output += "1"
        elif i == "E":
            msg_output += "3"
        elif i == "A":
            msg_output += "4"
        elif i == "T":
            msg_output += "7"
        else:
            msg_output += c.upper()
    return msg_output

## main
def main():
    clearScreen()
    menu()

if __name__ == "__main__":
    main()