FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note added successfully.")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes available.")
            return

        print("\nYour Notes")
        print("----------")

        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note.strip()}")

    except FileNotFoundError:
        print("No notes available.")


def delete_notes():
    with open(FILE_NAME, "w") as file:
        file.write("")

    print("All notes deleted.")


while True:
    print("\n--- Notes Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        delete_notes()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")