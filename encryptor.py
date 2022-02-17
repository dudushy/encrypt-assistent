import os
import math
import time

#default
loadAnimation = True
slowMode = False

def clearScreen():
    import os
    os.system('cls')

def printAllCodesAvaliable():
    print("\n= CÓDIGOS DISPONÍVEIS:"+
            "\n-- ZENITPOLAR"+
            "\n-- 1337"+
            "\n- - - - - - -")
            
#how they incode
def ZENITPOLAR(msg_input):
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

def LEET(msg_input):
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

def settings():
    clearScreen()
    #loop = True
    while True:
        clearScreen()
        global loadAnimation
        global slowMode
        print("-=- -=- -=- -=- -=- -=- -=- -=-"+
                "\n=======<Escolha uma operação>======="+
                "\n"+
                f"\n===> 1 Load Animation [{loadAnimation}]"+
                "\n"+
                f"\n===> 2 Slow Mode [{slowMode}]"+
                "\n"+
                "\n=======> 3 VOLTAR"+
                "\n-=- -=- -=- -=- -=- -=- -=- -=-")
        op = input("\t=> ")
        if op == "1":
            if loadAnimation == True:
                loadAnimation = False
            else:
                loadAnimation = True
        elif op == "2":
            if slowMode == True:
                slowMode = False
            else:
                slowMode = True
        elif op == "3":
            break
        else:
            clearScreen()
            print("-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-"+
                    "\n|   Valor inválido, tente novamente.   |"+
                    "\n-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-")
            input("\n : 'Ok'")

def wait(secs):
    import time
    if slowMode == True:
        time.sleep(secs)
    else:
        pass

def animLoad():
    import os, time
    if loadAnimation == True:
        load="|/-\|"
        for i in load:
            clearScreen()
            print(f"{i}\n")
            time.sleep(.1)
            clearScreen()
    else:
        pass

def convert():
    #loop //how it works
    while True:
        #request //raw data
        while True:
            clearScreen()
            print("Por favor insira os dados conforme o exemplo:"+
                    "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"+
                    "\n|  Exemplo:                          |"+
                    "\n|  CODE_MESSAGE: 1337_Hello World!   |"+
                    "\n- - - - - - - - - - - - - - - - - - - -")
            printAllCodesAvaliable()
            code_msg = input("\n-> CODE_MESSAGE: ")
            if code_msg != "":
                break
                clearScreen()
        #filter
        code = ""
        msg = ""
        print(code_msg)
        for j in code_msg:
            if j != "_":
                code += j
                if slowMode == True:
                    print(f"\n{j}\t===\t{code}")
                    wait(.1)
            else:
                break
        for k in range(((len(code)) + 1), len(code_msg)):
            msg += code_msg[k]
            if slowMode == True:
                print(f"\n{k}\t===\t{msg}")
                wait(.1)
        if slowMode == True:
            print(f"\nCODE: {code}\nMESSAGE: {msg}")
            wait(.4)

        #convert
        if code == "BINARIO":
            msg = BINARIO(f"{msg}")
        elif code == "ZENITPOLAR":
            msg = ZENITPOLAR(f"{msg}")
        elif code == "1337":
            msg = LEET(f"{msg}")

        #loading animation
        animLoad()

        #results
        check = ""
        while check != "s" or "n":
            clearScreen()
            print("%= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =%"+
                    f"\n\t\tMensagem: [  {msg}  ]\n"+
                    "\n\t\tDeseja executar novamente?"+
                    "\n%= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =%")
            check = input("\n (s/n): ")
            if check == "s":
                break
            if check == "n":
                break
        if check == "n":
            break

def menu():
    #menu
    clearScreen()
    #loop = True
    while True:
        clearScreen()
        print("-=- -=- -=- -=- -=- -=- -=- -=- -=- -=-"+
                "\n|   Escolha uma operação:    |"+
                "\n|                            |"+
                "\n|   1 > Converter            |"+
                "\n|                            |"+
                "\n|   2 > Configurações        |"+
                "\n|                            |"+
                "\n|   3 > SAIR                 |"+
                "\n-=- -=- -=- -=- -=- -=- -=- -=- -=- -=-")
        op = input("\n : ")
        if op == "1":
            convert()
        elif op == "2":
            settings()
        elif op == "3":
            clearScreen()
            check = ""
            while check != "s" or "n":
                clearScreen()
                print("-=- -=- -=- -=- -=- -=- -=- -=- -=- -=-"+
                    "\n|   Tem certeza de que deseja sair?   |"+
                    "\n-=- -=- -=- -=- -=- -=- -=- -=- -=- -=-")
                check = input("\n (s/n): ")
                if check == "s" or "n":
                    break
            if check == "s":
                break
        else:
            clearScreen()
            print("-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-"+
                    "\n|   Valor inválido, tente novamente.   |"+
                    "\n-=- -=- -=- -=- -=- -=- -=- -=- -=- -=- -=-")
            input("\n : 'Ok'")

clearScreen()
menu()
