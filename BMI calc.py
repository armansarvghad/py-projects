def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def main():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = calculate_bmi(height, weight)
    
    if bmi < 18.5:
        print("Your BMI is", bmi, "which means you are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print("Your BMI is", bmi, "which means you have a normal weight.")
    elif bmi >= 25 and bmi < 30:
        print("Your BMI is", bmi, "which means you are overweight.")
    else:
        print("Your BMI is", bmi, "which means you are obese.")

if __name__ == "__main__":
    main()
