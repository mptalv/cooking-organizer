from pydantic import BaseModel


class OrderCreate(BaseModel):
    recipe_name: str
    quantity: int