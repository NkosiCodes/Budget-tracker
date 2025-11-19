print("Sum of two numbers\nInput two numbers\n")

# Input
try:
   num_one = int(input("First number: "))
   num_two = int(input("Second number: "))
except ValueError:
   print("Please enter a valid number")

# Process
sumoftwo = num_one + num_two

# Output
print(f"Answer = {sumoftwo}")