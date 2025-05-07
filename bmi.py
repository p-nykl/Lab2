def calculate_bmi(height, weight):
    print("Height= "+str(height))
    print("Weight= "+str(weight))
    bmi=weight/(height*height)
    print(f"BMI= {bmi:.0f}")

    if bmi>25:
        print("Your BMI is Over Weight")
        if bmi<18.5:
            print("Your BMI is Under Weight")
    else:
        print("Your BMI is Normal Weight")


calculate_bmi(weight=57, height=1.73)

