import getpass


def login():
    email = input("email : ")
    password =getpass.getpass("password : ")
    ch = ("enter s for sign in or fg for forgot password : ")

    if ch == 's' :
        with open("user_account.txt",'r') as file:
            for line in file:
                if ':' in line:
                    stored_email, stored_user, stored_password, stored_country = line.strip().split(':')
                if stored_email == email and stored_password == password:
                    print("Logged in Successfully")
                    print("welcome ",stored_user)
                    return True
        print("Enter valid credentials")
        return False
    if ch == 'fg':

