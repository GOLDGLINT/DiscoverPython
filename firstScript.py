login = ""
password = ""
loginStatus = False
passwordStatus = False

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

antoine = User("gold", "glint")
nico = User("nico", "pass")

users = [antoine, nico]

loginInput = input("Enter your login :\n")

while loginStatus is False:
    for user in users:
        if user.login == loginInput:
            loginStatus = True
            userConnected = user
    if loginStatus is False:
        print("Wrong login")
        loginInput = input("Enter your login :\n")

passwordInput = input("Enter your password :\n")

while passwordStatus is False:
    if userConnected.password == passwordInput:
        passwordStatus = True
    if passwordStatus is False:
        print("Wrong password")
        passwordInput = input("Enter your password :\n")

print("Your logged in")
