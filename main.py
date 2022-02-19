#imports
import os, time

#settings
loadAnimation = True
slowMode = False
codes = ['ZENIT', 'LEET']

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

def convert() -> None:
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
            wait(1)

        #convert
        if code == "LEET":
            msg = LEET(f"{msg}")

        elif code == "ZENIT":
            msg = ZENIT(f"{msg}")
        
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

def menu() -> None:
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
def ZENIT(msg_input:str, slowMode:bool):  # sourcery skip: switch, use-assigned-variable
    encode = "ZENITzenit"
    decode = "POLARpolar"
    msg_output = ""

    for char in msg_input:
        if char in encode:
            msg_output += decode[encode.find(char)]
            if slowMode:
                print(f"char: {char} // output: {decode[encode.find(char)]}")
        elif char in decode:
            msg_output += encode[decode.find(char)]
            if slowMode:
                print(f"char: {char} // output: {encode[decode.find(char)]}")
        else:
            msg_output += char
            if slowMode:
                print(f"char: {char} // output: {char}")
    return msg_output


def LEET(msg_input:str, slowMode:bool):
    encode = "OIEASGT"
    decode = "0134567"
    msg_output = ""

    for char in msg_input:
        if char.upper() in encode:
            msg_output += decode[encode.find(char.upper())]
            if slowMode:
                print(f"char: {char} // output: {decode[encode.find(char.upper())]}")
        elif char.upper() in decode:
            msg_output += encode[decode.find(char.upper())]
            if slowMode:
                print(f"char: {char} // output: {encode[decode.find(char.upper())]}")
        else:
            msg_output += char
            if slowMode:
                print(f"char: {char} // output: {char}")
    return msg_output

## main
def main() -> None:
    #clearScreen()
    #menu()
    print(ZENIT('teste', True))
    print(LEET('teste', True))
    print(ZENIT('banana', False))
    print(LEET('banana', False))
    print(ZENIT('aBcDeFgHiJ', False))
    print(LEET('aBcDeFgHiJ', False))
    print(ZENIT('abcdef123', False))
    print(LEET('abcdef123', False))
    print(ZENIT('rosro', False))
    print(LEET('73573', False))

if __name__ == "__main__":
    main()