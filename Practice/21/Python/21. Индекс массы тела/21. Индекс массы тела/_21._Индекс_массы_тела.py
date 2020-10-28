weight, height = map(int, input("weight and height: ").split())
height /= 100
def bmi(weight: float, height: float) -> float:
    return weight / (height*height)
def print_bmi(bmi: float) -> float:
    if (bmi < 18.0):
        print("Underweight")
    if (bmi >= 18.0 and bmi < 25.0):
        print("Normal")
    if (bmi >= 25.0 and bmi < 30.0):
         print("Overweight")
    if (bmi > 30):
        print("Obesity")
print_bmi(bmi(weight, height))
