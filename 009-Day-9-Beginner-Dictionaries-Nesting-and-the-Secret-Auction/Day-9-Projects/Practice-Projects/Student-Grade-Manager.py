# Student Grade Manager
grades = {}


def add_student():
    name = input("Enter student name: ")
    if name in grades:
        print("Student already exists.")
    else:
        grades[name] = []
        print("Student added successfully!")


def add_grade():
    name = input("Enter student name: ")
    if name not in grades:
        add = input(
            "Student not found. Would you like to add them first? (yes/no): "
        ).lower()
        if add == "yes":
            add_student()
            while True:
                grade = input("Enter grade (0-100): ")
                if grade.isdigit():
                    grades[name].append(int(grade))
                    break
                else:
                    print("Enter in a digit!")
        else:
            print("Returning to menu.")
            return

    else:
        while True:
            grade = input("Enter grade (0-100): ")
            if grade.isdigit():
                grades[name].append(int(grade))
                break
            else:
                print("Enter in a digit!")
    print("Grade added successfully!")


def get_average(name):
    if grades[name]:
        grades_list = grades[name]
        avg_grade = round(sum(grades_list) / len(grades_list), 2)
        return avg_grade
    else:
        return f"{name} has no grades yet."


def display_all():
    if grades:
        print("--- All Students ---")
        num = 0
        for student in grades:
            num += 1
            print(f" - {num} - {student}: {get_average(student)}")
    else:
        print("No students in the system.")


while True:
    while True:
        choice = input("""Student Grade Tracker
- 1. Add student
- 2. Add grade
- 3. Display student average
- 4. Display all students with averages
- 5. Quit
===> Choose: """)
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print("You must enter in a number")
    if choice == 1:
        add_student()
    elif choice == 2:
        add_grade()
    elif choice == 3:
        name = input("Enter student name: ")
        if name in grades:
            print(f"{name}'s average: {get_average(name)}")
        else:
            print("Student not found.")

    elif choice == 4:
        display_all()
    elif choice == 5:
        print("Goodbye!")
        print(grades)
        break
    else:
        print("Invalid choice. Please try again.")
