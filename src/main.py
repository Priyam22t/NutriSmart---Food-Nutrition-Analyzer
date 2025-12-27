import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths & API key
DATA_PATH = os.path.join("data", "foods.json")
USDA_API_KEY = os.getenv("USDA_API_KEY")


def get_food_from_usda(food_name):
    """
    Fetch nutrition data from USDA FoodData Central API
    """
    if not USDA_API_KEY:
        return None

    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "query": food_name,
        "pageSize": 1,
        "api_key": USDA_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
    except Exception:
        return None

    if "foods" not in data or len(data["foods"]) == 0:
        return None

    nutrients = data["foods"][0].get("foodNutrients", [])

    nutrition = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    for n in nutrients:
        name = n.get("nutrientName", "").lower()
        value = n.get("value", 0)

        if "energy" in name:
            nutrition["calories"] = value
        elif "protein" in name:
            nutrition["protein"] = value
        elif "carbohydrate" in name:
            nutrition["carbs"] = value
        elif "fat" in name:
            nutrition["fat"] = value

    return nutrition


def analyze_food(food_name):
    """
    Main function used by app.py
    Tries:
    1. Local JSON dataset
    2. USDA API
    3. Safe fallback estimation
    """
    if not food_name:
        return None

    food_name = food_name.lower().strip()

    # 1️⃣ Try local dataset
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            foods = json.load(f)

        if food_name in foods:
            return foods[food_name]

    # 2️⃣ Try USDA API
    api_data = get_food_from_usda(food_name)
    if api_data:
        return api_data

    # 3️⃣ Fallback estimation (never fails)
    return {
        "calories": 120,
        "protein": 2.0,
        "carbs": 20.0,
        "fat": 2.0
    }
