from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.recipe_schema import RecipeCreate
from services.manager import KitchenManager

router = APIRouter()

manager = KitchenManager()


@router.post("/recipes")
def create_recipe(
    recipe: RecipeCreate,
    db: Session = Depends(get_db)
):

    return manager.create_recipe(db, recipe)


@router.get("/recipes")
def get_recipes(
    db: Session = Depends(get_db)
):

    return manager.get_recipes(db)