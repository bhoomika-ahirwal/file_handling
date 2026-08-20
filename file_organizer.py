import os
import shutil


def organize_files(folder):
    if not os.path.exists(folder):
        print("Folder not found.")
        return

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        if not extension:
            continue

        folder_name = extension[1:].upper() + "_FILES"

        destination = os.path.join(folder, folder_name)

        os.makedirs(destination, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination, filename)
        )

        print(f"Moved: {filename} → {folder_name}")


folder = input("Enter folder path: ")

organize_files(folder)

print("File organization completed.")