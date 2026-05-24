# FastAPI open here

from fastapi import FastAPI
from routes.orders import router as orders_router

app = FastAPI()

recipes = [
    {
        "name" : "Chocolate Chip Cookies",
        "ingredients" : [
                "flour",
                "baking soda",
                "salt",
                "brown sugar",
                "butter",
                "sugar",
                "eggs",
                "vanilla extract",
                "chocolate chips"
        ]
    },
    {
        "name": "tiramisu",
        "ingredients" : [
            "heavy whipping cream",
            "mascarpone",
            "sugar",
            "vanilla extract",
            "coffee",
            "ladyfingers",
            "cocoa powder"
        ]
    },
    {
        "name" : "lemon cookies",
        "ingredients" : [
            "flour",
            "cornstarch",
            "baking soda",
            "salt",
            "butter",
            "sugar",
            "eggs",
            "lemon juice",
            "lemon zest",
            "vanilla extract",
            "powdered sugar"
        ]
    }
]



@app.get("/")
def home():
    return {"message": "Kitchen API running"}

@app.get("/recipes")
def get_recipes():
    return recipes