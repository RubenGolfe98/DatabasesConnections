import Querys.Contacts as Contacts
import Querys.Users as Users
import Database
import Console



def main():
    userLog = ""
    Database.existsDB()
    Console.printHelp()
    command = Console.readCommand(userLog)

    while command[0] != 'exit':

        if command[0] == 'create':
            if Console.numWordsEqualsTo(command, 1, False):
                Database.create()

        elif command[0] == 'destroy':
            if Console.numWordsEqualsTo(command, 1, False):
                Database.destroyDB()

        elif command[0] == 'help':
            if Console.numWordsEqualsTo(command, 1, False):
                Console.printHelp()

        elif command[0] == 'ls':
            if Console.numWordsEqualsTo(command, 1, False):
                if Database.existsDB():
                    Users.listUsers()
                else:
                    Console.DBnotExists()

        elif command[0] == 'add':
            if Console.numWordsEqualsTo(command, 3, False):
                if Database.existsDB():
                    Users.addUser(command[1], command[2])
                else:
                    Console.DBnotExists()

        elif command[0] == 'rm':
            if Console.numWordsEqualsTo(command, 2, False):
                if Database.existsDB():
                    Users.removeUser(command[1])
                else:
                    Console.DBnotExists()

        elif command[0] == 'update':
            if Console.numWordsEqualsTo(command, 3, False):
                if Database.existsDB():
                    Users.updateUser(command[1], command[2])
                else:
                    Console.DBnotExists()

        elif command[0] == 'login':
            if Console.numWordsEqualsTo(command, 2, False):
                if Database.existsDB():
                    if Users.userInDB(command[1]):
                        userLog = command[1]
                        Console.loggedAs(userLog)
                        Console.printHelpLog()
                        command = Console.readCommand(userLog)

                        while command[0] != 'logout':
                            if command[0] == 'ls':
                                if Console.numWordsEqualsTo(command, 1, True):
                                    Contacts.listContacts(userLog)

                            elif command[0] == 'add':
                                if Console.numWordsEqualsTo(command, 3, True):
                                    Contacts.addContact(userLog, command[1], command[2])

                            elif command[0] == 'help':
                                if Console.numWordsEqualsTo(command, 1, True):
                                    Console.printHelpLog()

                            elif command[0] == 'rm':
                                if Console.numWordsEqualsTo(command, 2, True):
                                    Contacts.removeContact(userLog, command[1])

                            elif command[0] == 'update':
                                if Console.numWordsEqualsTo(command, 3, True):
                                    Contacts.updateContact(userLog, command[1], command[2])

                            else: Console.unknownCommandLog()

                            command = Console.readCommand(userLog)

                        Console.loggedOut(userLog)
                        userLog = ""

                else:
                    Console.DBnotExists()

        else: Console.unknownCommand()
        command = Console.readCommand(userLog)


if __name__ == "__main__":
    main()
