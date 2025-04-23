def can_enroll(age):
    if 10 <= age <= 20:
        return ("You are allowed to enroll in the class.")
    else:
        return ("Sorry, you are not allowed to enroll.")


try:
    age = int(input("Enter your age: "))
    result = can_enroll(age)
    print(result)
except ValueError:
    print("Please enter a valid number for age.")