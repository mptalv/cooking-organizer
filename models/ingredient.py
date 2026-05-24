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

