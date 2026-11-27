

def calculate_calories(carbs, fat, protein):
    total_calories = (carbs * 4) + (fat * 9) + (protein * 4)
    return total_calories


carbs = float(input("Enter carbohydrates (in grams): "))
fat = float(input("Enter fat (in grams): "))
protein = float(input("Enter protein (in grams): "))


calories = calculate_calories(carbs, fat, protein)


print("Total calorie intake in a day:", calories, "calories")