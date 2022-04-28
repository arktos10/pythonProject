def login():
    email = input('enter email:')

    if (email.endswith('@gmail.com')):
        password = input('enter password')
        if (len(password) < 8):
            print('weak password, enter strong password')
        else:
            print("successful login")
    elif (email.endswith("@yahoo.com")):
        print("error in email yahoo email don't support")
    else:
        print("error in email don't support")



login()
