# backend/main.py

from fastapi import FastAPI
from controllers.connexionController import ConnexionController

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI!"}

@app.get("/login")
def login(userName: str, password: str):
    return ConnexionController.login(userName, password)
