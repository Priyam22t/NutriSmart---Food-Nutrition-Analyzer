from flask import Flask, render_template, request, jsonify
from src.main import analyze_food
from src.ai_model import health_score, health_tip, meal_recommendation

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    food = request.form.get("food")
    nutrition = analyze_food(food)

    if not nutrition:
        return jsonify({"error": "Food not found"}), 404

    score = health_score(nutrition)

    return jsonify({
        "food": food,
        "nutrition": nutrition,
        "health_score": score,
        "health_tip": health_tip(nutrition)
    })


@app.route("/bmi", methods=["POST"])
def bmi():
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))

    bmi_value = round(weight / (height ** 2), 2)

    if bmi_value < 18.5:
        category = "Underweight"
        calories = 2500
    elif bmi_value < 25:
        category = "Normal"
        calories = 2200
    elif bmi_value < 30:
        category = "Overweight"
        calories = 1800
    else:
        category = "Obese"
        calories = 1500

    return jsonify({
        "bmi": bmi_value,
        "category": category,
        "daily_calories": calories
    })


@app.route("/meal", methods=["POST"])
def meal():
    goal = request.form.get("goal")
    return jsonify({
        "recommended_foods": meal_recommendation(goal)
    })


@app.route("/compare", methods=["POST"])
def compare():
    food1_name = request.form.get("food1")
    food2_name = request.form.get("food2")

    food1 = analyze_food(food1_name)
    food2 = analyze_food(food2_name)

    if not food1 or not food2:
        return jsonify({"error": "Food not found"}), 404

    score1 = health_score(food1)
    score2 = health_score(food2)

    if score1 > score2:
        verdict = "🏆 Food 1 is healthier"
    elif score2 > score1:
        verdict = "🏆 Food 2 is healthier"
    else:
        verdict = "🤝 Both are equally healthy"

    return jsonify({
        "food1_nutrition": food1,
        "food2_nutrition": food2,
        "comparison": {
            "food1_score": score1,
            "food2_score": score2,
            "verdict": verdict
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
