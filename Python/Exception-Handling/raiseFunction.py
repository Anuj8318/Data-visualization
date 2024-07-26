def verify_age():
    try:
        age = int(input("Enter the age you want to "))
        if age<18:
            raise ValueError("Your age less than 18")
        else:
            print("Your are eligible to vote")
    except ValueError as e:
        print("Your are not eligible to vote as",e)
    
verify_age()