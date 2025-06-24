from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.models import Ingredient, Recipe

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine) # Create tables for all imported models

Session = sessionmaker(bind=engine)
session = Session()

ingredients = session.query(Ingredient).all()

# Query all recipes and their ingredients
recipes_with_ingredients = session.query(Recipe).all()

for recipe in recipes_with_ingredients:
    print(f"Recipe: {recipe.name}")
    for ingredient in recipe.ingredients:
        print(f" - Ingredient: {ingredient.name}")

app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipe_name = request.form['name']
        new_recipe = Recipe(name=recipe_name)
        try: 
            session.add(new_recipe)
            session.commit()
            return redirect('/ingredients/add')
        except:
            return 'There was an issue adding your recipe'
    else:
        return render_template('index.html', recipes=recipes_with_ingredients)
    
@app.route('/ingredients/add', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        ingredient_name = request.form['name']
        new_ingredient = Ingredient(name=ingredient_name)
        try: 
            session.add(new_ingredient)
            session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your ingredient'
    else:
        return render_template('ingredients.html', ingredients=ingredients)
    
# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'
    
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)
#     if request.method == 'POST':
#         task.content = request.form['content']
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'
#     else:
#         return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)