def calculate_macros(weight, height, age, activity_level, goal):
    activity_miltipliers = {
        "low": 1.2,
        "medium": 1.55,
        "high": 1.8
    }

    multuplier = activity_miltipliers.get(activity_level, 1.2)

    #Формула Миффина-Сан Жеора
    bmr = 10*weight + 6.25*height - 5*age + 5

    calories = bmr * multuplier

    if goal == "cut":
        calories -= 300
    elif goal == "bulk":
        calories += 300

    protein = weight * 2
    fat = weight * 0.8
    carbs = (calories - (protein*4+fat*9))/4

    return {
        "calories": round(calories),
        "protein": round(protein),
        "fat": round(fat),
        "carbs": round(carbs)
    }