from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base import Base

# Association table for many-to-many relationship
recipe_ingredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', ForeignKey('ingredients.id'), primary_key=True)
)

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    ingredients = relationship('Ingredient', secondary=recipe_ingredient, back_populates='recipes')

    def __repr__(self):
        return '<Recipe %r>' % self.id

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand_name = Column(String, nullable=True)
    serving_size = Column(String, nullable=True)
    quantity = Column(Integer, default=1)
    calories = Column(Integer, default=0)
    protein = Column(Integer, default=0)
    carbohydrates = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.utcnow)

    recipes = relationship('Recipe', secondary=recipe_ingredient, back_populates='ingredients')

    def __repr__(self):
        return '<Ingredient %r>' % self.id