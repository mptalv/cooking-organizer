from fastapi import FastAPI

from database.database import Base
from database.database import engine
from routes.orders import router as orders_router
from routes.recipes import router as recipes_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recipes_router)
app.include_router(orders_router)


@app.get("/")
def home():
    return {
        "message": "Kitchen Manager API Running"
    }