def readCommand(userName):
    commandEmpty=True
    while commandEmpty:
        if userName == "":
            print(chr(27)+"[1;37m"+f"{userName}$ ", end="") 
        else:
            print(chr(27)+"[1;36m"+f"{userName}$ ", end="") 
        
        command = input().split()
        if len(command)==0:
            unknownCommand()
        else:
            commandEmpty=False

    return command

def numWordsEqualsTo(command,num, log):
    if(len(command) == num):
        return True
    else:
        if log:
            unknownCommandLog()
        else:
            unknownCommand()
        return False

def printHelp():
    print(chr(27)+"[1;35m"+"")
    print(''' 
    Available commands:

    ---- USERS MANAGEMENT ----
     -login <email>: Log in with user name 
     -add <userName> <email>: Add new user
     -ls: List all users
     -rm <email>: Remove user
     -update <email> <userName>: Update user name by email

     ---- OTHER COMMANDS ----
     -help: Show Available commands
     -exit: Exit
    ''')

def printHelpLog():
    print(chr(27)+"[1;36m"+"")
    print(''' 
    Available commands:

    ---- CONTACTS MANAGEMENT ----
     -add <email> <name>: Add new contact
     -ls: List all contacts
     -update <email> <name>: Update name by email contact
     -rm <email>: Remove contact

    ---- OTHER COMMANDS ----
     -help: Show Available commands
     -logout: Log out
    ''')

def unknownCommand():
    print(chr(27)+"[1;31m"+"UNKNOWN COMMAND")
    printHelp()

def unknownCommandLog():
    print(chr(27)+"[1;31m"+"UNKNOWN COMMAND")
    printHelpLog()

def loggedAs(name):
    print(chr(27)+"[1;32m"+f"Logged as {name}\n")

def loggedOut(name):
    print(chr(27)+"[1;32m"+f"{name} is logged out\n")

def userNotExist(name):
    print(chr(27)+"[1;31m"+f"User '{name}' does not exists in the database\n") 