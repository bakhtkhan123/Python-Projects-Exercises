#calculate bmi
weight=float(input("Enter your weight"))
height=float(input("Enter your height"))
BMI=round(weight/height**2)
if BMI <18:
    print(f"with {BMI} BMI you are under weight")
elif BMI <25:
    print(f"with {BMI} BMI you are in normal weight")
elif BMI<30:
    print(f"with {BMI} BMI you have obese class1")
elif BMI <35:
    print(f"with {BMI} BMI you have obese class2")
else:
    print("you have clinically obese")