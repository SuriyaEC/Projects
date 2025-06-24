import re
import password_checker
import getpass

def is_email_valid(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def register():
    while True:
        email = input("Email : ")
        if is_email_valid(email):
            break
        else:
            print("invalid email format")
    while True:
        password = getpass.getpass("Password : ")
        result = password_checker.password_check(password)
        print(result)
        if "STRONG" in result:
            break

    user = input("Username : ")
    country = input("Country : ")

    with open("user_account.txt",'a') as file:
        file.write(f"{email}:{user}:{password}:{country}\n")
        print("registered successfully")





