class Client:

    def __init__(self, name, agency, account, phone, balance):
        self.name = name
        self.agency = agency
        self.account = account
        self.phone = phone
        self.balance = balance

    def deposit(self, value):

        self.balance += value

        if self.balance > 0:
            print("=====================")
            print("Efetuado com Sucesso!", "\nSaldo Positivo!")
            print("=====================")
        else:
            print("=====================")
            print("Efetuado com Sucesso!", "\n\033[31mSaldo Negativo!\033[0;m")
            print("=====================")

    def sake(self, value):
        self.balance -= value

        if self.balance > 0:
            print("=====================")
            print("Efetuado com Sucesso!", "\nSaldo Positivo!")
            print("=====================")
        else:
            print("=====================")
            print("Efetuado com Sucesso!", "\n\033[31mSaldo Negativo!\033[0;m")
            print("=====================")

    def statement(self):
        pass
