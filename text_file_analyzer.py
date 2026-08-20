def analyze_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        print("\nFile Analysis")
        print("-------------")
        print("Lines      :", len(lines))
        print("Words      :", len(words))
        print("Characters :", characters)

    except FileNotFoundError:
        print("File not found.")


filename = input("Enter file name: ")
analyze_file(filename)