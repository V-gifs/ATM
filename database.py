import os
import validation
import datetime as dt

user_db_path = 'data/user_record/'
auth_session = 'data/auth_session/'
today = dt.date.today()

def create(user_account_number, first_name, last_name, email, password):
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if does_account_number_exist(user_account_number):
        return False
    if does_email_exist(email):
        print("User already exists")
        return False
    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
    else:
        f.write(str(user_data))
        completion_state = True
    finally:
        f.close()
        return completion_state


def read(user_account_number):
    is_validation_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_validation_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't exist")
    except TypeError:
        print("Invalid account number format")
    else:
        return f.readline()
    return False

def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the file
    # save the file
    # return true


def delete(user_account_number):
    is_delete_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful


def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user),',')
        if email in user_list:
            return True
    return False

def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False

def authenticated_user(user_account_number,password):
    if does_account_number_exist(user_account_number):
        user = str.split(read(user_account_number), ',')
        if password == user[3]:
            return user

    return False


def create_balance (account_number):
    f = open(user_db_path + str(account_number) + "_balance" + ".txt", "x")
    f.write(str(0))
    f.close()

def add_deposit_to_balance (account_number,deposit):
     pull_balance = open(user_db_path + str(account_number) + "_balance" + ".txt", "r")
     current_balance = int(pull_balance.readline())
     new_balance = current_balance + int(deposit)
     w = open(user_db_path + str(account_number) + "_balance" + ".txt", "w")
     w.write(str(new_balance))
     pull_balance.close()
     w.close()

def withdraw_from_balance (account_number, withdrawl):
    pull_balance = open(user_db_path + str(account_number) + "_balance" + ".txt", "r")
    current_balance = int(pull_balance.readline())
    if current_balance >= int(withdrawl):
        new_balance = current_balance - int(withdrawl)
        w = open(user_db_path + str(account_number) + "_balance" + ".txt", "w")
        w.write(str(new_balance))
        return True
        w.close()
    else:
        return False
    pull_balance.close()


def read_balance(account_number):
    pull_balance = open(user_db_path + str(account_number) + "_balance" + ".txt", "r")
    current_balance = int(pull_balance.readline())
    return current_balance
    pull_balance.close()

def create_auth_session(account_number):
    try:
        f = open(auth_session + str(account_number) + ".txt", "x")
        f.write("User is currently logged in")
        f.close()
    except FileExistsError:
        return False
    return True

def delete_auth_session(account_number):
    is_delete_successful = False
    if os.path.exists(auth_session + str(account_number) + ".txt"):
        try:
            os.remove(auth_session + str(account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User is not logged in")
        finally:
            return is_delete_successful
