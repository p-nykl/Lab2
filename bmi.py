def calculate_bmi(height, weight):
    print("Height= "+str(height))
    print("Weight= "+str(weight))
    bmi=weight/(height*height)
    print(f"BMI= {bmi:.0f}")


    if bmi>25:
        print("Your BMI is Over Weight")
        return (1)
    elif bmi<18.5:
            print("Your BMI is Under Weight")
            return(-1)
    elif(bmi>=18.5 and bmi<=25):
        print("Your BMI is Normal Weight")
        return (0)


calculate_bmi(weight=40, height=1.73)
