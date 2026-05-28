from sqlalchemy.orm import Session

from database.models import Ingredient
from database.models import Order
from database.models import Recipe
from database.models import RecipeIngredient

from data.recipes import recipes

class KitchenManager:

    def create_recipe(self, db: Session, recipe_data):

        recipe = Recipe(
            name=recipe_data.name
        )

        db.add(recipe)
        db.commit()
        db.refresh(recipe)

        for ingredient_data in recipe_data.ingredients:

            ingredient = db.query(Ingredient).filter(
                Ingredient.name == ingredient_data.name
            ).first()

            if not ingredient:
                ingredient = Ingredient(
                    name=ingredient_data.name,
                    unit=ingredient_data.unit
                )

                db.add(ingredient)
                db.commit()
                db.refresh(ingredient)

            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                quantity=ingredient_data.quantity
            )

            db.add(recipe_ingredient)

        db.commit()

        return {
            "message": "Recipe created",
            "recipe": recipe.name
        }

    def get_recipes(self, db: Session):

        recipes = db.query(Recipe).all()

        results = []

        for recipe in recipes:

            ingredient_list = []

            for item in recipe.ingredients:

                ingredient_list.append({
                    "name": item.ingredient.name,
                    "quantity": item.quantity,
                    "unit": item.ingredient.unit
                })

            results.append({
                "id": recipe.id,
                "name": recipe.name,
                "ingredients": ingredient_list
            })

        return results
    
    def process_order(self, db: Session, order_data):

        recipe = db.query(Recipe).filter(
            Recipe.name == order_data.recipe_name
        ).first()

        if not recipe:
            return {
                "error": "Recipe not found"
            }

        ingredient_totals = []

        for item in recipe.ingredients:

            total_quantity = (
                item.quantity * order_data.quantity
            )

            ingredient_totals.append({
                "name": item.ingredient.name,
                "quantity": total_quantity,
                "unit": item.ingredient.unit
            })

        tasks = [
            f"Gather ingredients for {recipe.name}",
            f"Prepare {order_data.quantity} batch(es)",
            f"Cook/Bake {recipe.name}",
            "Package order"
        ]

        order = Order(
            recipe_name=order_data.recipe_name,
            quantity=order_data.quantity
        )

        db.add(order)
        db.commit()

        return {
            "recipe": recipe.name,
            "quantity": order_data.quantity,
            "ingredients": ingredient_totals,
            "tasks": tasks
        }