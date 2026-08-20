FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll_number},{name},{course}\n")

    print("Student added successfully.")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\nStudent Records")
        print("----------------")

        for record in records:
            roll, name, course = record.strip().split(",")

            print(f"Roll No : {roll}")
            print(f"Name    : {name}")
            print(f"Course  : {course}")
            print("----------------")

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_roll = input("Enter roll number: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        for record in records:
            roll, name, course = record.strip().split(",")

            if roll == search_roll:
                print("\nStudent Found")
                print("-------------")
                print("Roll No :", roll)
                print("Name    :", name)
                print("Course  :", course)
                return

        print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")