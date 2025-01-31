# File: app/models.py
from datetime import datetime

class FoodEntry:
    def __init__(self, id, name, calories, portion=1):
        self.id = id
        self.name = name
        self.calories = calories * portion  # Total kalori = kalori per porsi × porsi
        self.date = datetime.now().strftime("%d-%m-%Y")

class CalorieGoal:
    def __init__(self):
        self.daily_goal = 2000  # Default target kalori

# Data dummy
food_entries = [
    FoodEntry(1, "Nasi Putih", 200, 2),
    FoodEntry(2, "Ayam Goreng", 250),
]

calorie_goal = CalorieGoal()