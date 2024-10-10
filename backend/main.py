from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import init_db
from models import User

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

register_tortoise(
    app,
    db_url="mysql://myuser:mypassword@db/mydatabase",
    modules={"models": ["models.User"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.put("/users/")
async def create_user(email: str, password: str):
    user = await User.create(email=email, hashed_password=password)
    return user