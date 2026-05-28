from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from database.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    ingredients = relationship(
        "RecipeIngredient",
        back_populates="recipe",
        cascade="all, delete"
    )

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    unit = Column(String, nullable=False)

    recipes = relationship(
        "RecipeIngredient",
        back_populates="ingredient"
    )

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)

    recipe_id = Column(
        Integer,
        ForeignKey("recipes.id")
    )

    ingredient_id = Column(
        Integer,
        ForeignKey("ingredients.id")
    )

    quantity = Column(Float, nullable=False)

    recipe = relationship(
        "Recipe",
        back_populates="ingredients"
    )

    ingredient = relationship(
        "Ingredient",
        back_populates="recipes"
    )

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)