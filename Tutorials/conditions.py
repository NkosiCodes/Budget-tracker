print("Input your age from 12 - 35")

try:
    age = int(input("Age: "))
    if age < 12 or age > 35:
        print("please enter a number within parameters")
    else:
        if age >= 18:
           print("Adult")
        elif age == 17:
            print("Ahh not quite there buddy")
        else:
            print("probably A minorrrrrr")
except ValueError:
    print("please enter a valid number")
