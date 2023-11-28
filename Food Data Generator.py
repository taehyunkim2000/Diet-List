import json


import requests

def get_specific_nutrients(food_item, api_key):
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food_item}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    nutrition = {"Calories": None, "Sugars": None, "Protein": None, "Total Fat": None}

    for nutrient in data["foods"][0]["foodNutrients"]:
        if nutrient["nutrientName"] == "Energy":
            nutrition["Calories"] = nutrient.get("value")
        elif "Sugar" in nutrient["nutrientName"]:
            nutrition["Sugars"] = nutrient.get("value")
        elif nutrient["nutrientName"] == "Protein":
            nutrition["Protein"] = nutrient.get("value")
        elif "Fat" in nutrient["nutrientName"]:
            nutrition["Total Fat"] = nutrient.get("value")

    return nutrition

def main():
    api_key = "87cHbS8Cb36gN4CLQRZkr2DBbuniBUl4OZGWaHn8"
    foods = ["Lettuce", "Cabbage", "Bok choy", "Arugula", "Kale", "Watercress", "Collard greens", "Spinach", "Swiss chard", "Asparagus", "Celery", "Bamboo shoots", "Turmeric", "Carrots", "Parsley", "Parsnips", "Turnips", "Radishes", "Wasabi", "Horseradish", "Beetroot", "Cassava", "Potatoes", "Sweet potatoes", "Purple yam", "Artichokes", "Bitter gourd", "Okra", "Bell peppers", "Cauliflower", "Broccolini", "Broccoli", "Brussels sprouts", "Garlic", "Onions", "Leeks", "Maitake mushrooms", "Oyster mushrooms", "Enoki mushrooms", "Shiitake mushrooms", "Blueberries", "Blackberries", "Lemon", "Lime", "Watermelon", "Cantaloupes", "Apples", "Pears", "Bananas", "Passion fruit", "Brown rice", "Oats", "Barley", "Chickpeas", "Black beans", "Kidney beans", "Lentils", "Soybeans", "Almonds", "Walnuts", "Cashews", "Chia seeds", "Flax seeds", "Pumpkin seeds", "Salmon", "Sardines", "Trout", "Cod", "Tuna", "Oysters", "Lobsters", "Squid", "Abalone", "Lean pork", "Lean beef", "Chicken breast", "Chicken thighs", "Turkey", "Duck liver", "Eggs", "Cow’s milk", "Plain yogurt", "Fortified goat’s milk", "Cheese", "Extra virgin olive oil", "Sesame oil", "Safflower oil", "Avocado oil", "Canola oil", "Grapeseed oil", "Sunflower oil", "Soybean oil", "Amaranth", "Quinoa", "Goji berries", "Acai berries", "Maca root", "Moringa powder", "Green tea", "Matcha powder"]  # Extend this list
    food_nutrition_table = []

    for food in foods:
        nutrition = get_specific_nutrients(food, api_key)
        if nutrition:
            nutrition["Food"] = food
            food_nutrition_table.append(nutrition)

    # Save data to a JSON file
    with open('food_nutrition_data.json', 'w') as file:
        json.dump(food_nutrition_table, file)

    print("Data saved to food_nutrition_data.json")

if __name__ == "__main__":
    main()

