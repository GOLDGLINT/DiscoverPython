from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='mysql://myuser:mypassword@db/mydatabase',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()