# -*- coding: utf-8 -*-

import cliente, os

list = [(123, 456, "Gustavo")]

def main():
    print("\033[32m================")
    print("Welcome to bank!")
    print("================\033[0;m")

    print("1 - Login")
    print("2 - Exit")

    clear = lambda: os.system('clear')

    enter = input("Enter The Option Number: ")

    if enter == 1:

        clear()
        agency = input("Enter The Agency Number: ")
        account = input("Enter The Account Number: ")

        if agency == list[0][0] and account == list[0][1]:
            clear()
            print("Welcome " + list[0][2])

            print("\n1 - Deposit")
            print("2 - Sake")

            enter = input("Enter The Option Number: ")

            if enter == 1:
                pass

            elif enter == 2:
                pass
            else:
                print("Error!")

    elif enter == 2:
        pass

    else:
        print("Error!")

c1 = cliente.Client("gustavo", "123", "456", "87798564", 0.00)

# print("Nome:", c1.name)
# print("Agencia:", c1.agency)

# c1.sake(100)

main()


# c1.deposit(50)
