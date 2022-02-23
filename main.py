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

def printAllAvaliableCodes() -> None:
    print("\n= AVALIABLE CODES:")
    for code in codes:
        print(f"-- {code}")
    print("- - - - - - -")

def checkCode(codes: list, code: str):
    return code in codes

def wait(secs: int) -> None:
    if slowMode:
        time.sleep(secs)

def animLoad() -> None:
    load = "|/-\|"
    for i in load:
        clearScreen()
        print(f"{i}\n")
        time.sleep(.1)

def settings() -> None:
    global loadAnimation, slowMode

    while True:
        clearScreen()
        print(settingsMenu())
        match input(">>> "):
            case "1":
                loadAnimation = not loadAnimation
            case "2":
                slowMode = not slowMode
            case "3":
                return
            case _:
                invalidInput()

def convert() -> None:
    global loadAnimation, slowMode, codes

    while True:
        clearScreen()
        print("Please, enter data following the example:"+
                    "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"+
                    "\n|  Example:                          |"+
                    "\n|  MESSAGE: LEET_Hello World!        |"+
                    "\n- - - - - - - - - - - - - - - - - - - -")
        printAllAvaliableCodes()
        try:
            code, msg = input("\n>>> MESSAGE: ").split('_', 1)
        except Exception:
            invalidInput()
            continue
        if checkCode(codes, code):
            match code:
                case "ZENIT":
                    if loadAnimation:
                        animLoad()
                    clearScreen()
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
                    + f"\n| Message: [\t{ZENIT(msg, slowMode)}\t]"
                    + "\n| Run again?"
                    + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    match input(">>> (y/n): "):
                        case "y":
                            continue
                        case "n":
                            break
                case "LEET":
                    if loadAnimation:
                        animLoad()
                    clearScreen()
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
                    + f"\n| Message: [\t{LEET(msg, slowMode)}\t]"
                    + "\n| Run again?"
                    + "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    match input(">>> (y/n): "):
                        case "y":
                            continue
                        case "n":
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
                if input(">>> (y/n): ") == "y":
                    break
            case _:
                invalidInput()

## codes
def ZENIT(msg_input:str, slowMode:bool):
    encode = "ZENITzenit"
    decode = "POLARpolar"
    msg_output = ""

    for char in msg_input:
        if char in encode:
            msg_output += decode[encode.find(char)]
            if slowMode:
                print(f"[ZENIT | {msg_input}] char: {char} // output: {decode[encode.find(char)]}")
        elif char in decode:
            msg_output += encode[decode.find(char)]
            if slowMode:
                print(f"[ZENIT | {msg_input}] char: {char} // output: {encode[decode.find(char)]}")
        else:
            msg_output += char
            if slowMode:
                print(f"[ZENIT | {msg_input}] char: {char} // output: {char}")
    return msg_output


def LEET(msg_input:str, slowMode:bool):
    encode = "OIEASGT"
    decode = "0134567"
    msg_output = ""

    for char in msg_input:
        if char.upper() in encode:
            msg_output += decode[encode.find(char.upper())]
            if slowMode:
                print(f"[LEET | {msg_input}] char: {char} // output: {decode[encode.find(char.upper())]}")
        elif char.upper() in decode:
            msg_output += encode[decode.find(char.upper())]
            if slowMode:
                print(f"[LEET | {msg_input}] char: {char} // output: {encode[decode.find(char.upper())]}")
        else:
            msg_output += char
            if slowMode:
                print(f"[LEET | {msg_input}] char: {char} // output: {char}")
    return msg_output

## main
def main() -> None:
    menu()

if __name__ == "__main__":
    main()