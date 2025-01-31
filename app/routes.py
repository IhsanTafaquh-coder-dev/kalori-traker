from flask import Blueprint, render_template, request, redirect, url_for
from .models import food_entries, calorie_goal
from .models import FoodEntry

main = Blueprint('main', __name__)

@main.route('/')
def home():
    total_calories = sum(food.calories for food in food_entries)
    progress = min((total_calories / calorie_goal.daily_goal) * 100, 100)
    return render_template('index.html', 
                         foods=food_entries,
                         total=total_calories,
                         goal=calorie_goal.daily_goal,
                         progress=progress)

@main.route('/add', methods=['POST'])
def add_food():
    new_id = len(food_entries) + 1
    new_food = FoodEntry(
        id=new_id,
        name=request.form['food_name'],
        calories=int(request.form['calories']),
        portion=int(request.form['portion'])
    )
    food_entries.append(new_food)
    return redirect(url_for('main.home'))

@main.route('/delete/<int:food_id>')
def delete_food(food_id):
    global food_entries
    food_entries = [food for food in food_entries if food.id != food_id]
    return redirect(url_for('main.home'))

@main.route('/set-goal', methods=['POST'])
def set_goal():
    calorie_goal.daily_goal = int(request.form['new_goal'])
    return redirect(url_for('main.home'))