import datetime as dt
import random

database = {6377565748:[ 'Seyi', 'Onifade', 'seyi@zuri.team', 'passwordSeyi' ],
            5632186970:[ 'Mike', 'Johnson', 'mike@gmail.com','passwordMike' ],
            2065930257:[ 'Love', 'Wins', 'love@yahoo.com','passwordLove' ]}

balanceInfo = {6377565748: -50, 5632186970: 100, 2065930257: 1000}

today = dt.date.today()

def init():

    print("Welcome to bankPHP")
    print(today.strftime("%B %d, %Y"))
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    
    if(haveAccount == 1):
        isValidOptionSelected = True
        login()
    elif(haveAccount == 2):
        isValidOptionSelected = True
        register()
    else:
        print("You have selected invalid option")
        init()

def login():

    print("****** Log In ******")
    
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")
    global userDetails
    global accountNumber
    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                 
    print('Invalid account or password')
    login()
    

def register():

    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, ]
    balanceInfo[accountNumber] = 0 #Balance is 0 when account first opens until first deposit
    print("Your account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0],user[1]))
    
    selectedOption = int(input("What would you like to do? \n (1) Deposit \n (2) Withdraw \n (3) Check Balance \n (4) Log Out \n (5) Exit \n"))
    
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawlOperation()
    elif(selectedOption == 3):
        checkBalance()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(userDetails)
        
def withdrawlOperation():
    withdrawl = int(input("How much would you like to withdraw? \n"))
    if (balanceInfo[accountNumber] > withdrawl):
        newBalance = balanceInfo[accountNumber] - withdrawl
        balanceInfo[accountNumber] = newBalance
        print("Your current balance is %d" % newBalance)
        print("Take your cash!")
    else:
        print("Insufficient funds")
    bankOperation(userDetails)

def depositOperation():
    deposit = int(input("How much would you like to deposit? \n"))
    newBalance = balanceInfo[accountNumber] + deposit
    balanceInfo[accountNumber] = newBalance
    print("Current Balance: %d" % newBalance)
    bankOperation(userDetails)

def checkBalance():
    balance = balanceInfo[accountNumber]
    print("Your current balance is %d" % balance)
    bankOperation(userDetails)
    
def generationAccountNumber():
    
    return random.randrange(1111111111,9999999999)

def logout():
    login()


#### ACTUAL BANKING SYSTEM ###

init()               
