import cliente

def main():
    print("\033[32m================")
    print("Welcome to bank!")
    print("================\033[0;m")

c1 = cliente.Client("gustavo", "123", "456", "87798564", 0.00)

# print("Nome:", c1.name)
# print("Agencia:", c1.agency)

# c1.deposit(50)
# c1.sake(100)

main()