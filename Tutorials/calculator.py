print("Welcome to the Calculator")

print("Choose 1 of the 4 options below:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

def choice():
    try:
        choice_choices = int(input("Choice(Number): "))

        if choice_choices > 4 or choice_choices < 1:
            print("Please enter number from 1 - 4")
    except:
        print("Please enter a valid number")

    return choice_choices 

num_1 = float(input("Number 1: "))
num_2 = float(input("Number 2:"))

sum_Of_Num = num_1 + num_2
product_Of_Num = num_1 * num_2
difference_Of_Num = num_1 - num_2
quotient_Of_Num = num_1/num_2

num_Choice = choice()

def add(): 
        return f"Sum of {int(num_1)} + {int(num_2)} = {int(sum_Of_Num)}"

def subtract(): 
        return f"Sum of {int(num_1)} - {int(num_2)} = {int(difference_Of_Num)}"
    
def multiply():  
        return f"Sum of {int(num_1)} * {int(num_2)} = {int(product_Of_Num)}"
    
def divide():
    return f"Sum of {int(num_1)} / {int(num_2)} = {int(quotient_Of_Num)}"
    
if num_Choice == 1: 
    print(add())
elif num_Choice == 2:
    print(subtract())
elif num_Choice == 3:
    print(multiply())
elif num_Choice == 4:
    print(divide())
     