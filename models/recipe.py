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

