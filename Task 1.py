try:
    with open("sample.txt","r") as file:
        print("reading file content:")

        for i, line in enumerate(file, start=1):
            print(f"{line.strip()}")
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")


try:
    with open("samply.txt","r") as file:
        print("reading file content:")

        for i, line in enumerate(file, start=1):
            print(f"{line.strip()}")
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")
