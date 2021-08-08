def bmi(weight, height):
    #your code here
    bmi = weight/(height*height)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
