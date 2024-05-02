def calculate_bmi(height, weight):     
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    bmi=(weight/height**2)
    print(str(bmi))
    if bmi < 18.5:
       result = -1
       print ("You are Underweight.")
    elif 18.5 <= bmi <= 25.0:
        result = 0
        print ("You are of Normal Weight")
    elif 25.0 < bmi :
        result = 1
        print ("You are Overweight.")
    return result


