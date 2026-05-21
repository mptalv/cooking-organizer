# =========================
# INGREDIENT CLASS
# =========================

class Ingredient:

    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def scaled_amount(self, quantity):
        return self.amount * quantity


# =========================
# RECIPE CLASS
# =========================

class Recipe:

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.tasks = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_task(self, task):
        self.tasks.append(task)


# =========================
# ORDER CLASS
# =========================

class Order:

    def __init__(self):
        self.items = {}

    def add_recipe(self, recipe, quantity):
        self.items[recipe] = quantity


# =========================
# KITCHEN MANAGER
# =========================




# =========================
# CREATE RECIPES
# =========================

cake = Recipe("Chocolate Cake")

cake.add_ingredient(
    Ingredient("Flour", 3, "cups")
)

cake.add_ingredient(
    Ingredient("Eggs", 4, "count")
)

cake.add_ingredient(
    Ingredient("Sugar", 2, "cups")
)

cake.add_task("Preheat oven")
cake.add_task("Mix ingredients")
cake.add_task("Bake cake")


cookies = Recipe("Cookies")

cookies.add_ingredient(
    Ingredient("Flour", 2, "cups")
)

cookies.add_ingredient(
    Ingredient("Eggs", 1, "count")
)

cookies.add_task("Prepare dough")
cookies.add_task("Bake cookies")


# =========================
# CREATE ORDER
# =========================

order = Order()

order.add_recipe(cake, 2)
order.add_recipe(cookies, 3)


# =========================
# PROCESS ORDER
# =========================

manager = KitchenManager()

ingredient_totals = manager.calculate_ingredients(order)

tasks = manager.generate_tasks(order)


# =========================
# OUTPUT RESULTS
# =========================

print("\nINGREDIENT TOTALS")
print("===================")

for ingredient, amount in ingredient_totals.items():
    print(f"{ingredient}: {amount}")


print("\nTASKS")
print("===================")

for task in tasks:
    print(task)