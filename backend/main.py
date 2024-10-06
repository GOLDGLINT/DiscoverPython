from fastapi import FastAPI
from controllers import connexionController

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI!"}

@app.get("/login")
def login(userName: str, password: str):
    return connexionController.login(userName, password)
