
class Atm:

    global balance
    balance = 100

    @staticmethod
    def reg():
        global newLogin
        global newPassword
        print('Create your login: ')
        newLogin = input()
        print('Create your password: ')
        newPassword = input()
        print("Great, now you must enter in your account")
        Atm.auth()

    @staticmethod
    def auth():
        print('Write your login: ')
        login = input()
        print('Write your password: ')
        password = input()
        if newLogin == login and newPassword == password:
            print("You are logged into your account")
            Atm.deposit()
        else:
            print("Wrong login or password")
            Atm.auth()

    @staticmethod
    def enterDeposit():
        global balance
        print("Specify the amount you want to deposit: ")
        countOfMoney = input()
        if int(countOfMoney) >= 10000:
            print("Mne kajetsa ti naebchik")
            Atm.auth()
        else:
            balance += int(countOfMoney)
            print("Money has been deposited")
            Atm.deposit()

    @staticmethod
    def withdraw():
        global balance
        print("Specify the amount you want to withdraw: ")
        withdraw = input()
        if balance < int(withdraw):
            print("There are not enough funds in your account")
        else:
            balance -= int(withdraw)
            print("You have successfully withdrawn funds")
        Atm.deposit()


    @staticmethod
    def deposit():
        print('Choose option: \n'
              'Press "1" to view balance \n'
              'Press "2" to to enter deposit \n'
              'Press "3" to withdraw')
        option = input()
        if option == "1":
            print(f"You have {balance} $")
            Atm.deposit()
        if option == "2":
            Atm.enterDeposit()
        if option == "3":
            Atm.withdraw()
        else:
            print("Incorrect number, you must choose 1, 2 or 3")
            Atm.deposit()

    @staticmethod
    def menu():
        print('Press "1" to registration \n'
              'Press "2" to authorisation \n')
        num = input()
        if num == "1":
            Atm.reg()
        if num == "2":
            print("First, you need to create account")
            Atm.reg()
            pass
        else:
            print("Incorrect number, you must choose 1 or 2")
            Atm.menu()


Atm.menu()
