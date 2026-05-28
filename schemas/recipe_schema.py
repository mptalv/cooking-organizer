from pydantic import BaseModel


class IngredientCreate(BaseModel):
    name: str
    quantity: float
    unit: str


class RecipeCreate(BaseModel):
    name: str
    ingredients: list[IngredientCreate]