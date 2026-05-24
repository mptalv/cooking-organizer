from pydantic import BaseModel

class OrderRequest(BaseModel):
    recipe_name: str
    quantity: int