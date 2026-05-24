
# =========================
# ORDER CLASS
# =========================

class Order:

    def __init__(self):
        self.items = {}

    def add_recipe(self, recipe, quantity):
        self.items[recipe] = quantity

