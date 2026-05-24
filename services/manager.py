# =========================
# KITCHEN MANAGER
# =========================

from data.recipes import recipes

class KitchenManager:

    def calculate_ingredients(self, order):

        totals = {}

        for recipe, quantity in order.items.items():

            for ingredient in recipe.ingredients:

                total_amount = ingredient.scaled_amount(quantity)

                key = f"{ingredient.name} ({ingredient.unit})"

                if key in totals:
                    totals[key] += total_amount
                else:
                    totals[key] = total_amount

        return totals

    def generate_tasks(self, order):

        tasks = []

        for recipe, quantity in order.items.items():

            tasks.append(
                f"Prepare {quantity} batch(es) of {recipe.name}"
            )

            for task in recipe.tasks:
                tasks.append(f"- {task}")

        return tasks
    
    def process_order(self, recipe_name, quantity):

        recipe = None

        for r in recipes:
            if r["name"] == recipe_name:
                recipe = r

        if not recipe:
            return {
                "error": "Recipe not found"
            }

        ingredient_totals = []

        for ingredient in recipe["ingredients"]:

            total_quantity = (
                ingredient["quantity"] * quantity
            )

            ingredient_totals.append({
                "name": ingredient["name"],
                "quantity": total_quantity,
                "unit": ingredient["unit"]
            })

        return {
            "recipe": recipe_name,
            "quantity": quantity,
            "ingredients": ingredient_totals,
            "tasks": recipe["tasks"]
        }