# user = {"name": "Nkosi", "age": 22}
# print(f"Name: {user["name"]}\nAge: {user["age"]}\n")

# user["email"] = "test@gmail.com"
# print(f"Name: {user["name"]}\nAge: {user["age"]}\nEmail: {user['email']}")

import os
import csv

def login():

    print("Welcome to the student login")
    print("Please enter all your student details")

# Input

    try:
        student_name = input("Student Name: ")

        if student_name.replace(" ", "").isalpha():
            print("valid name")
        else:
            print("please enter a valid name")
            return

        student_id = input("DOB eg.(030925): ")

        if len(student_id) == 6 and student_id.isdigit():
            print("valid id")
        else:
            print("Invalid Id")
            return

        student_email = input("Email: ")

        if "@" in student_email and "." in student_email:
            print("valid email")
        else:
            print("Invalid email")
            return
        
        # student_id = int(student_id)

        Student = {
            "name": student_name,
            "id": "#" + student_id,
            "S_email": student_email
        }
        
        file_exists = os.path.isfile("database.csv")


        with open('database.csv', 'a', newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Student name", "Student Id", "Student Email"])

            writer.writerow([
                Student["name"],
                Student["id"],
                Student["S_email"]
            ])
        
        print(f"Student name: {Student['name']}\nStudent Id: {Student['id']}\nStudent email: {Student['S_email']}")
        
    except ValueError:
        print("Please enter a valid DOB")
    except NameError:
        print("Please enter a valid email")

login()