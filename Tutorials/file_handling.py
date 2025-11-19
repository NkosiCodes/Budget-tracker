with open("data.txt", "w") as file:
    file.write("Hello World!")

with open("data.txt", "r") as file:
    print(file.read())