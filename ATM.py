import datetime as dt
name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
today = dt.date.today()
if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        print(today.strftime("%B %d, %Y"))
        print('these are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')
        selectedOption = int(input('Please select an option:'))

        if (selectedOption == 1):
            withdraw = int(input('How much would you like to withdraw? \n'))
            print('Take your cash!')
            print('Welcome %s' % name)
            print(today.strftime("%B %d, %Y"))
            print('these are the available options:')
            print('1. Withdrawl')
            print('2. Cash Deposit')
            print('3. Complaint')
            selectedOption = int(input('Please select an option:'))
        elif(selectedOption == 2):
            deposit = int(input('How much would you like to deposit?'))
            print('Current Balance: %d' % deposit)
            print('Welcome %s' % name)
            print(today.strftime("%B %d, %Y"))
            print('these are the available options:')
            print('1. Withdrawl')
            print('2. Cash Deposit')
            print('3. Complaint')
        elif(selectedOption == 3):
            complaint = input('What issue would you like to report?')
            print('Thank you for contacting us')
            print('Welcome %s' % name)
            print(today.strftime("%B %d, %Y"))
            print('these are the available options:')
            print('1. Withdrawl')
            print('2. Cash Deposit')
            print('3. Complaint')
        else:
            print('Invalid Option selected, please try again')
    else:
        print('Password Incorrect, please try again')
else:
    print('Name not found, please try again')
