
class Atm:

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
        else:
            print("Wrong login or password")

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
