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

    def isUser(self, loginInput, passwordInput):
        for user in self.users:
            if user.login == loginInput:
                if user.password == passwordInput:
                    return True
        return False

    def login(self):
        loginInput = connexionView.getLoginInput()
        passwordInput = connexionView.getPasswordInput()
        if self.isUser(loginInput, passwordInput):
            connexionView.printUserConnected()
        else:
            connexionView.printWrongLoginOrPassword()
            self.login()
