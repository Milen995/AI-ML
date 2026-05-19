def askname():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            break
        print("Name must contain letters only, no numbers or symbols.")

    while True:
        age = input("What is your age? ")
        if age.isdigit():
            break
        print("Age must be a number.")

    while True:
        gender = input("What is your gender? ")
        if gender.isalpha():
            break
        print("Gender must contain letters only, no numbers or symbols.")

    print(f"Hello, you are {name}, {age} years old, and {gender}.")
    return name, age, gender

askname()