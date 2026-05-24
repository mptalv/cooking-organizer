# FastAPI open here

from fastapi import FastAPI
from routes.orders import router as orders_router
from recipes import recipes

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Kitchen API running"}

@app.get("/recipes")
def get_recipes():
    return recipes