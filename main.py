id_user = 0
balance = 100
state = None
list_of_users = []


def reg():
    global id_user
    print('Create your login: ')
    new_login = input()
    print('Create your password: ')
    new_password = input()
    for l in range(len(list_of_users)):
        for p in range(len(list_of_users[l])):
            if list_of_users[l][1] == new_login:
                print('This login already exist, try something else')
                reg()
    else:
        id_user += 1
        list_of_users.extend([[id_user, new_login, new_password, balance]])
        print("Great, now you must enter in your account")
        auth()

def auth():
    global state
    print('Write your login: ')
    login = input()
    print('Write your password: ')
    password = input()
    for l in range(len(list_of_users)):
        for p in range(len(list_of_users[l])):
            if list_of_users[l][1] == login and list_of_users[l][2] == password:
                state = list_of_users[l][0]
                print(f'Hello, {login}')
                deposit()
    else:
        print("Login or password is incorrect ")
        auth()


def enter_deposit():
    global state
    print("Specify the amount you want to deposit: ")
    count_of_money = input()
    if count_of_money.isdigit():
        for l in range(len(list_of_users)):
            for p in range(len(list_of_users[l])):
                if int(count_of_money) >= 10000:
                    print("Mne kajetsa ti naebchik")
                    auth()
                elif list_of_users[l][0] == state:
                    list_of_users[l][3] += int(count_of_money)
                    print(list_of_users)
                    print("Money has been deposited")
                    deposit()
    else:
        print("You enter not number, please try again")
        enter_deposit()


def withdraw():
    global state
    print("Specify the amount you want to withdraw: ")
    withdraw = input()
    for l in range(len(list_of_users)):
        for p in range(len(list_of_users[l])):
            if list_of_users[l][0] == state:
                if list_of_users[l][3] < int(withdraw):
                    print("There are not enough funds in your account")
                    deposit()
                else:
                    list_of_users[l][3] -= int(withdraw)
                    print("You have successfully withdrawn funds")
                    deposit()


def view_balance():
    global state
    for l in range(len(list_of_users)):
        for p in range(len(list_of_users[l])):
            if list_of_users[l][0] == state:
                print(f"""You have {list_of_users[l][3]} dollars on your account""")
                deposit()


def deposit():
    global balance
    print('Choose option: \n'
          'Press "1" to view balance \n'
          'Press "2" to to enter deposit \n'
          'Press "3" to withdraw \n'
          'Press "4" to exit from your account \n'
          'Press "5" to create new account \n'
          'Press "6" to exit')
    option = input()
    if option == "1":
        view_balance()
    if option == "2":
        enter_deposit()
    if option == "3":
        withdraw()
    if option == "4":
        auth()
    if option == "5":
        reg()
    if option == "6":
        raise SystemExit
    else:
        print("Incorrect number, you must choose 1, 2 or 3")
        deposit()


def menu():
    print('Press "1" to registration \n'
          'Press "2" to authorisation \n')
    num = input()
    if num == "1":
        reg()
    if num == "2":
        print("First, you need to create account")
        reg()
        pass
    else:
        print("Incorrect number, you must choose 1 or 2")
        menu()


menu()
