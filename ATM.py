import datetime as dt
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
today = dt.date.today()
while True:
    name = input("What is your name? \n")
    if(name in allowedUsers):
        while True:
            password = input("Your password? \n")
            userId = allowedUsers.index(name)
            if(password == allowedPassword[userId]):
                print('Welcome %s' % name)             
                break
            print('Wrong password')
        break
    print('Name not found, please try again')
flag = True
while flag:
    selectedOption = int(input('These are the available options: \n 1. Withdrawl \n 2. Cash Deposit \n 3. Complaint \n 4. Exit \n Please select an option:'))
    if (selectedOption == 1):
        withdrawl = int(input('How much would you like to withdraw? \n'))
        print('Take your cash!')
    elif (selectedOption == 2):
        deposit = int(input('How much would you like to deposit? \n'))
        print('Current Balance: %d' % deposit)
    elif (selectedOption == 3):
        complaint = input('What issue would you like to report? \n')
        print('Thank you for contacting us.')
    elif (selectedOption == 4):
        print('Goodbye!')
        flag = False
    else:
        print('Invalid Option selected, please try again.')
    

    
                
