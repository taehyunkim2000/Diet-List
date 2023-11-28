import tkinter as tk
from tkinter import messagebox
import json
import random

def load_nutritional_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_target_calories(current_calories, goal_calories):
    if goal_calories > current_calories:  # Weight gain
        return goal_calories
    elif goal_calories < current_calories:  # Weight loss
        return goal_calories
    else:  # Maintenance
        return current_calories

def select_foods_for_meal(foods, used_foods, max_calories, max_items=3):
    selected_foods = []
    total_calories = 0
    for food in random.sample(foods, len(foods)):  # Randomize the selection
        if food['Food'] in used_foods:
            continue  # Skip if the food was already used in a previous meal
        food_calories = food.get("Calories", 0) or 0
        if total_calories + food_calories <= max_calories and len(selected_foods) < max_items:
            selected_foods.append(food)
            total_calories += food_calories
            used_foods.add(food['Food'])
    return selected_foods

def submit_action():
    current_weight = float(current_weight_var.get())
    sex = sex_var.get().lower()
    current_calories = float(current_calories_var.get())
    goal = goal_var.get().lower()

    target_calories = 2500 if sex == 'male' else 2000
    if goal == 'lose':
        target_calories -= 500
    elif goal == 'gain':
        target_calories += int(target_calories * 0.20)

    daily_calories = calculate_target_calories(current_calories, target_calories)
    meal_calories = daily_calories / 3

    file_path = 'C:/Users/ROG/food_nutrition_data.json'  # Update the path accordingly
    food_nutrition_table = load_nutritional_data(file_path)

    used_foods = set()  # Track foods that have been used
    meals = {"Breakfast": [], "Lunch": [], "Dinner": []}
    for meal in meals:
        meals[meal] = select_foods_for_meal(food_nutrition_table, used_foods, meal_calories)

    diet_plan_message = "Your personalized daily diet plan:\n"
    for meal, items in meals.items():
        diet_plan_message += f"{meal}:\n"
        for item in items:
            diet_plan_message += f"  - {item['Food']} ({item.get('Calories', 0)} Calories)\n"

    messagebox.showinfo("Diet Plan", diet_plan_message)

# GUI setup
root = tk.Tk()
root.title("Diet Plan Generator")

tk.Label(root, text="Current weight (kg):").pack()
current_weight_var = tk.StringVar()
tk.Entry(root, textvariable=current_weight_var).pack()

tk.Label(root, text="Sex (male/female):").pack()
sex_var = tk.StringVar()
tk.Entry(root, textvariable=sex_var).pack()

tk.Label(root, text="Current daily calorie intake:").pack()
current_calories_var = tk.StringVar()
tk.Entry(root, textvariable=current_calories_var).pack()

tk.Label(root, text="Goal (lose/gain/maintain):").pack()
goal_var = tk.StringVar()
tk.Entry(root, textvariable=goal_var).pack()

submit_button = tk.Button(root, text="Generate Diet Plan", command=submit_action)
submit_button.pack()

root.mainloop()
