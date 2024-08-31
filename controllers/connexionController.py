from models.User import User
from views import connexionView

class ConnexionController:
    def __init__(self):
        self.users = [
            User("gold", "glint"),
            User("nico", "pass")
        ]
        self.loginStatus = False
        self.passwordStatus = False

    def verifyLogin(self):
        loginInput = connexionView.getLoginInput()
        while self.loginStatus is False:
            for user in self.users:
                if user.login == loginInput:
                    self.loginStatus = True
                    self.userConnected = user
            if self.loginStatus is False:
                connexionView.printWrongLogin()
                loginInput = connexionView.getLoginInput()

    def verifyPassword(self):
        passwordInput = connexionView.getPasswordInput()
        while self.passwordStatus is False:
            if self.userConnected.password == passwordInput:
                self.passwordStatus = True
            if self.passwordStatus is False:
                connexionView.printWrongPassword()
                passwordInput = connexionView.getPasswordInput()

    def login(self):
        self.verifyLogin()
        self.verifyPassword()