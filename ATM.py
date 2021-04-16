import datetime as dt
import random
import validation
import database
import getpass

today = dt.date.today()


def init():
    print("Welcome to bankPHP")
    print(today.strftime("%B %d, %Y"))
    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("****** Log In ******")
    # global user_details
    # global account_number
    global account_number_from_user
    global user
    account_number_from_user = input("What is your account number? \n")
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass.getpass("What is your password? \n")
        user = database.authenticated_user(account_number_from_user,password)
        if user:
            current_session = database.create_auth_session(account_number_from_user)
            if current_session:
                bank_operation(user)
            else:
                print("User is already logged in")

        print('Invalid account or password')
        login()
    else:
        print("Account Number Invalid")
        init()


def register():
    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass.getpass(prompt="Create a password \n")
    account_number = generation_account_number()
    is_user_created = database.create(account_number, first_name, last_name, email, password)
    if is_user_created:
        print("Your account has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")
        database.create_balance(account_number)
        login()
    else:
        print("Something went wrong. Please try again.")
        register()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selected_option = int(input(
        "What would you like to do? \n (1) Deposit \n (2) Withdraw \n (3) Check Balance \n (4) Log Out \n (5) Exit \n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawl_operation()
    elif selected_option == 3:
        check_balance()
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user_details)


def withdrawl_operation():
    withdrawl = input("How much would you like to withdraw? \n")
    is_valid_withdrawl = validation.withdrawl_validation(withdrawl)
    if is_valid_withdrawl:
        if database.withdraw_from_balance(account_number_from_user,withdrawl):
            print("%s has been withdrawn" % withdrawl)
        else:
            print("Insufficient Funds")
    else:
        print("Input must be number with no symbols")
    bank_operation(user)


def deposit_operation():
    deposit = input("How much would you like to deposit? \n")
    is_valid_deposit = validation.deposit_validation(deposit)
    if is_valid_deposit:
        database.add_deposit_to_balance(account_number_from_user,deposit)
        print("%s has been deposited" % deposit)
        bank_operation(user)
    else:
        print ("Input must be number with no symbols")
        deposit_operation()


def check_balance():
    balance = database.read_balance(account_number_from_user)
    print("Your current balance is %d" % balance)
    bank_operation(user)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    database.delete_auth_session(account_number_from_user)
    login()


#### ACTUAL BANKING SYSTEM ###

init()
