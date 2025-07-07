import re

def password_check(password):

    if len(password) < 8 :
        return "WEAK : strong password length should be atleast 8"
    
    if not re.search("[a-z]",password):
        return "WEAK : should contain atleast one lowercase "
    if not re.search("[A-Z]",password):
        return "WEAK : should contain atleast one uppercase"
    if not re.search("[0-9]",password):
        return "WEAK : should contain numbers"
    if not re.search("[!@$%^&*_]",password):
        return "WEAK : should contain speacial characters"
    
    common_passwords = ['password','123456789','acdef']
    if password.lower() in common_passwords:
        return "WEAK"
    
    else:
        return "STRONG"

