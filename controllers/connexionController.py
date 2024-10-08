from views import connexionView
from controllers.scpController import ScpController

class ConnexionController:
    def isUser(self, loginInput: str, passwordInput: str):
        for user in self.users:
            if user.login == loginInput:
                if user.password == passwordInput:
                    return True
        return False
    
    def login(self):
        loginInput = connexionView.getLoginInput()
        passwordInput = connexionView.getPasswordInput()
        if ConnexionController.isUser(self, loginInput, passwordInput):
            connexionView.printUserConnected()
            ScpController.listSCPs(self)
        else:
            connexionView.printWrongLoginOrPassword()
            ConnexionController.login()
