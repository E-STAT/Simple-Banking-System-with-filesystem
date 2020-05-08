import random
import os, sys
#Staff login page
def staff():
    option = int(input('1. Login. 2. Close App:'))
    return option

#user choice of actions; create bank account, check account details, log out
def user_choice():
    user_select = input('1. Create new bank account. 2. Check account details. 3. Log out ')
    user_select = int(user_select)
    return user_select

#get account details to print to customers
def account_details():
    number = int(input('Enter your account number:'))
    if number == int(show_account_number()):
        file = open('customer.txt', 'r')
        file = file.readlines()
        print(file)
    

#getting user details when creating account
def get_user():
    account_name = input('Enter Account Name:')
    opening_bal = input('Enter opening balance:')
    account_type = input('Enter Account type:')
    account_email = input('Enter Account email:')
    account_number = random.randint(0000000000, 9999999999)
    return account_name,opening_bal,account_type,account_email,account_number

#show account details to customer
def show_account_number():
    with open('customer.txt', 'r') as f:
        details = f.readlines()
        num = details[-1][67:-1]
    return num


############################### The banking process ########################################
############################### The banking process ########################################

if staff() ==1:
    username = str(input("Enter your username: ").strip())
    password = input("Enter your password: ").strip()

    with open("staff.txt", "r") as f:
        for line in f.readlines():
            loginInfo = line.strip().split(",")
            if username == loginInfo[0] and password == loginInfo[1]:
                print('Authorized') 

                with open('session.txt', 'w') as s:
                    user_action =user_choice()
                    while user_action == 1:
                        file = open('customer.txt', 'w')
                        file = file.writelines(str(get_user()))
#                         file_cus = open('session.txt', 'w')
#                         file_cus.writelines(str(file))
                        print('Dear customer, your account number: {}'.format(show_account_number()))
                        user_action = user_choice()
                    while user_action ==2:

                        account_details()
                        user_action = user_choice()
                    else:
                        os.remove('session.txt')
                        user_action = user_choice()
            else:
                print('Wrong uername of password, please try again')

    # print(type(loginInfo[1]), type(password))
    # assert loginInfo[0] == username
    # assert loginInfo[1] == password