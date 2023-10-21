from random import randrange
import time

# check if a list file exists, if not, create one. - Done
# check if new characters added are already in the list. - Done
# allow the user to save the password to a new file. - Done
# If the Length is a negative number, generate the password and then reverse it. - Done
# Fix the error where launching the Main Function within the Main function breaks it. - Done

# Functions
def changePassChars(passList, Chars):
    changeCharOption = input("""Would you like to append or replace the existing list?
    1) Append
    2) Replace
""")
    if changeCharOption not in ["1", "2"]: print("Incorrect option selected."); changePassChars(passList, Chars)
    
    try: # If the option is append, attempt to open the file in append mode, check if the character already exists, if not, append the character.
        if changeCharOption == "1":
            passListAppend = open("Characters.txt", "a")
            for char in Chars:
                if char in passList.read(): continue
                else: passListAppend.write(char)
        
        else: # If the option is write, attempt to open the file in write mode, and then write all of the characters to the file.
            passListWrite = open("Characters.txt", "w")
            passListWrite.write(Chars)
        
        print(f"Character list changed successfully.")

    except FileNotFoundError: # If the Password List is not found, create a new file with all of the current specified chars inside it.
        passList = open("Characters.txt", "w")
        passList.write(Chars)


def changePassLength():
    try: numLength = int(input("How long would you like your password? (e.g. '8') "))
    except ValueError:
        print("A ValueError has occured, returning to main menu.")
        Main(passList = open("Characters.txt", "r"), passLength = 0)

    if numLength != 0: passLength = numLength # if the length is not 0, the password length is assigned to the user's specified value.
    else: # The reason we are not banning negative numbers is because I have a funny idea in mind.
        print("Here's your password: ")
        print("Not so funny is it."); quit()
    return passLength


def Main(passList, passLength):
    menuChoice = input("""
--------------------------------------------------
 Python password creator, created by Logan Heath.
--------------------------------------------------
 Please select your option below:
    1) Create Password
    2) Change Character List
    3) Print Character List
    4) Quit
""")
        
    if menuChoice == "1":
        constructedPass = ""
        charList = []
        for char in passList.read():
            charList.append(char)

        passLength = changePassLength()

        processTimerStart = time.time()
        if passLength > 0:
            while passLength > 0:
                randomChar = charList[randrange(0, len(charList) - 1)]
                constructedPass += randomChar
                passLength -= 1
            finalOutput = constructedPass

        elif passLength < 0:
            while passLength < 0:
                randomChar = charList[randrange(0, len(charList) - 1)]
                constructedPass += randomChar
                passLength += 1
            finalOutput = constructedPass[::-1]

        processTimerStop = time.time()
        print(f"Your password is: {finalOutput}")
        print(f"Processing took {processTimerStop - processTimerStart} seconds.")

        toFile = str.upper(input("Do you wish to save this to a file? (Y / N): "))
        if toFile in ["Y", "YES"]:
            outPassFile = open("PasswordOutput.txt", "w")
            outPassFile.write(finalOutput)
        Main(passList = open("Characters.txt", "r"), passLength = 0)

    elif menuChoice == "2":
        Chars = input("Please enter all characters you wish to add: ")
        changePassChars(passList, Chars)
        Main(passList = open("Characters.txt", "r"), passLength = 0)

    elif menuChoice == "3":
        passList = open("Characters.txt", "r")
        print(passList.read())
        Main(passList = open("Characters.txt", "r"), passLength = 0)

    elif menuChoice == "4":
        quit()

    else:
        print(f"Incorrect option {menuChoice}, restarting..."); Main(passList = open("Characters.txt", "r"), passLength = 0)


# Code that starts the application by running the functions
defaultChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYX?!£$%&@"
try: passList = open("Characters.txt", "r")
except FileNotFoundError: 
    print("Your password characters file was not found, creating a default characters list...")
    passList = open("Characters.txt", "w")
    print(f"Creating file with default Characters: '{defaultChars}'...")
    passList.write(defaultChars)
    print("Success! proceeding with execution...")
    passList = open("Characters.txt", "r")

Main(passList, passLength = 0)
input("Press Enter to Quit")