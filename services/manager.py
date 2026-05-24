# =========================
# KITCHEN MANAGER
# =========================

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
    
    def process_sample_order(self):

        return {
            "ingredients": {
                "Flour": 6,
                "Eggs": 8
            },
            "tasks": [
                "Bake cake",
                "Prepare frosting"
            ]
        }