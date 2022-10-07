import Querys.Contacts as Contacts
import Querys.Users as Users
import Console



def main():
    userLog = ""
    Console.printHelp()
    command = Console.readCommand(userLog)

    while command[0] != 'exit':

        if command[0] == 'help':
            if Console.numWordsEqualsTo(command, 1, False):
                Console.printHelp()

        elif command[0] == 'ls':
            if Console.numWordsEqualsTo(command, 1, False):
                Users.listUsers()

        elif command[0] == 'add':
            if Console.numWordsEqualsTo(command, 3, False):
                Users.addUser(command[1], command[2])

        elif command[0] == 'rm':
            if Console.numWordsEqualsTo(command, 2, False):
                Users.removeUser(command[1])

        elif command[0] == 'update':
            if Console.numWordsEqualsTo(command, 3, False):
                    Users.updateUser(command[1], command[2])

        elif command[0] == 'login':
            if Console.numWordsEqualsTo(command, 2, False):
                if Users.existUser(command[1]):
                    userLog = Users.getNameByEmail(command[1])
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

        else: Console.unknownCommand()
        command = Console.readCommand(userLog)


if __name__ == "__main__":
    main()
