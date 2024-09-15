from models.User import User
from models.SCP import SCP
from controllers.connexionController import ConnexionController

class MainApp:
    def __init__(self):
        self.users = [
            User("gold", "glint"),
            User("nico", "pass")
        ]
        self.scps = [
            SCP("002", "contained", "euclid", None),
            SCP("096", "contained", "euclid", None),
            SCP("409", "contained", "keter", None)
        ]
        
    def run(self):
        ConnexionController.login(self)


if __name__ == "__main__":
    app = MainApp()
    app.run()