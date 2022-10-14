from color_comands import *
from decimal import Decimal
import os
import hashlib
import decimal

id_user = 0
balance = 100
state = None
list_of_users = []


def validation(login, password):
    if len(login) < 5:
        print('Your login is too short')
        reg()
    elif len(password) < 7:
        print('Your password is too short')
        reg()
    elif not login.isalnum():
        print("Login should not contain special characters, only letters and numbers ")
        reg()
    elif not password.isalnum():
        print("Password should not contain special characters, only letters and numbers ")
        reg()
    else:
        pass


def reg():
    global id_user
    print(create_login)
    new_login = input()
    print(create_pass)
    new_password = input()
    validation(new_login, new_password)
    for line in range(len(list_of_users)):
        for column in range(len(list_of_users[line])):
            if list_of_users[line][1] == new_login:
                print(login_exist)
                reg()
    else:
        id_user += 1
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt, 100000)
        list_of_users.extend([[id_user, new_login, key, balance, salt]])
        print(enter)
        auth()


def auth():
    global state
    print(write_login)
    login = input()
    print(write_pass)
    password = input()
    for line in range(len(list_of_users)):
        for column in range(len(list_of_users[line])):
            new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), list_of_users[line][4], 100000)
            if list_of_users[line][1] == login and list_of_users[line][2] == new_key:
                state = list_of_users[line][0]
                print(welcome, login)
                deposit()
    else:
        print(incorrect_log_pass)
        auth()


def enter_deposit():
    global state
    print(count_deposit)
    try:
        count_of_money = Decimal(input())
        if isinstance(count_of_money, Decimal):
            for line in range(len(list_of_users)):
                for column in range(len(list_of_users[line])):
                    if Decimal(count_of_money) >= 10000:
                        print(naebchik)
                        auth()
                    elif list_of_users[line][0] == state:
                        list_of_users[line][3] += Decimal(count_of_money)
                        print(deposited)
                        deposit()
    except decimal.InvalidOperation:
        print(not_number)
    finally:
        enter_deposit()


def withdraw():
    global state
    print(withdraw_count)
    try:
        count_of_withdraw = Decimal(input())
        for line in range(len(list_of_users)):
            for column in range(len(list_of_users[line])):
                if list_of_users[line][0] == state:
                    if list_of_users[line][3] < Decimal(count_of_withdraw):
                        print(not_enough_funds)
                        deposit()
                    else:
                        list_of_users[line][3] -= Decimal(count_of_withdraw)
                        print(success_withdraw)
                        deposit()
    except decimal.InvalidOperation:
        print(not_number)
    finally:
        withdraw()


def view_balance():
    global state
    for line in range(len(list_of_users)):
        for column in range(len(list_of_users[line])):
            if list_of_users[line][0] == state:
                print(f"""You have {list_of_users[line][3]} dollars on your account""")
                deposit()


def deposit():
    global balance
    print(options,
          option1,
          option2,
          option3,
          option4,
          option5,
          option6)
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
        print(incorrect_number)
        deposit()


def menu():
    print(registration, authorisation)
    num = input()
    if num == "1":
        reg()
    if num == "2":
        print(first_create_acc)
        reg()
        pass
    else:
        print(incorrect_numbers12)
        menu()


menu()
