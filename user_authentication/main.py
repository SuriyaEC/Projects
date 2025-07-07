import registration
import login

print("(1) New User  (2) Existing User")
ch = input(" choose (1/2) : ")

if ch == '1' :
    registration.register()
    login.login()
if ch == '2' :
    login.login()
else:
    print("invalid input")