def health_score(nutrition):
    score = 100

    if nutrition["calories"] > 200:
        score -= 20
    elif nutrition["calories"] > 100:
        score -= 10

    if nutrition["protein"] > 2:
        score += 10

    if nutrition["fat"] > 5:
        score -= 15

    return max(0, min(score, 100))


def health_tip(nutrition):
    score = health_score(nutrition)

    if score >= 80:
        return "Very healthy food 👍"
    elif score >= 60:
        return "Moderately healthy, consume in balance."
    else:
        return "Consume occasionally ⚠️"


def meal_recommendation(goal):
    if goal == "weight_loss":
        return ["apple", "banana", "salad", "oats"]
    elif goal == "muscle_gain":
        return ["eggs", "chicken", "rice", "banana"]
    else:
        return ["rice", "vegetables", "fruits", "milk"]


def compare_foods(food1, food2):
    score1 = health_score(food1)
    score2 = health_score(food2)

    if score1 > score2:
        better = "Food 1 is healthier"
    elif score2 > score1:
        better = "Food 2 is healthier"
    else:
        better = "Both foods are equally healthy"

    return {
        "food1_score": score1,
        "food2_score": score2,
        "verdict": better
    }
