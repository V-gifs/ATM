def account_number_validation(account_number):

    if account_number:



        try:
            int(account_number)
            if len(str(account_number)) == 10:
                return True

        except ValueError:

            return False
        except TypeError:

            return False
    return False

def deposit_validation(deposit):
    if deposit:
        try:
            int(deposit)
            if int(deposit) > 0:
                return True
        except ValueError:
            return False
    return False

def withdrawl_validation(withdrawl):
    if withdrawl:
        try:
            int(withdrawl)
            if int(withdrawl) > 0:
                return True
        except ValueError:
            return False
    return False






