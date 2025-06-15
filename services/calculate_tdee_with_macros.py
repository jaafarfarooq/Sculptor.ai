def calculate_tdee_with_macros(weight_kg, height_cm, age, gender, activity_level, goal):
    if gender.lower() == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Choose 'male' or 'female'.")
    
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "heavy": 1.725,
        "athlete": 1.9
    }
    
    if activity_level.lower() not in activity_multipliers:
        raise ValueError("Invalid activity level.")
        
    tdee = bmr * activity_multipliers[activity_level.lower()]
    
    goals = {
        "cut": tdee * 0.8,
        "maintain": tdee,
        "bulk": tdee * 1.2
    }
    
    if goal.lower() not in goals:
        raise ValueError("Invalid goal.")
        
    adjusted_calories = round(goals[goal.lower()], 2)
    
    protein_ratio = 0.4
    carb_ratio = 0.4
    fat_ratio = 0.2
    
    protein_grams = round((adjusted_calories * protein_ratio) / 4, 2)
    carb_grams = round((adjusted_calories * carb_ratio) / 4, 2)
    fat_grams = round((adjusted_calories * fat_ratio) / 9, 2)
    
    return {
        "TDEE": round(tdee, 2),
        "Adjusted Calories": adjusted_calories,
        "Protein (g)": protein_grams,
        "Carbs (g)": carb_grams,
        "Fats (g)": fat_grams
    }
