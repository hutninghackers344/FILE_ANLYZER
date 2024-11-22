import subprocess
import os


os.system('clear')


red = "\033[31m"
reset = "\033[0m"


text = ''' 
 ________        ______        __              ________          ______         __    __        __              __      __        ________        ________        _______  
|        \      |      \      |  \            |        \        /      \       |  \  |  \      |  \            |  \    /  \      |        \      |        \      |       \ 
| $$$$$$$$       \$$$$$$      | $$            | $$$$$$$$       |  $$$$$$\      | $$\ | $$      | $$             \$$\  /  $$       \$$$$$$$$      | $$$$$$$$      | $$$$$$$\
| $$__            | $$        | $$            | $$__           | $$__| $$      | $$$\| $$      | $$              \$$\/  $$           /  $$       | $$__          | $$__| $$
| $$  \           | $$        | $$            | $$  \          | $$    $$      | $$$$\ $$      | $$               \$$  $$           /  $$        | $$  \         | $$    $$
| $$$$$           | $$        | $$            | $$$$$          | $$$$$$$$      | $$\$$ $$      | $$                \$$$$           /  $$         | $$$$$         | $$$$$$$\
| $$             _| $$_       | $$_____       | $$_____        | $$  | $$      | $$ \$$$$      | $$_____           | $$           /  $$___       | $$_____       | $$  | $$
| $$            |   $$ \      | $$     \      | $$     \ ______| $$  | $$      | $$  \$$$      | $$     \          | $$          |  $$    \      | $$     \      | $$  | $$
 \$$             \$$$$$$       \$$$$$$$$       \$$$$$$$$|      \\$$   \$$       \$$   \$$       \$$$$$$$$           \$$           \$$$$$$$$       \$$$$$$$$       \$$   \$$
'''


print(f"{red}{text}{reset}")
print(f"Created by @devilxuser & @bat")


file = input(f"Enter the file{red}: ").strip()


if not os.path.exists(file):
    print(f"Error: The file '{file}' does not exist.")
else:

    print(f"1. Enter the specific metadata key to extract{red}")
    print("2. Dump all metadata")
    print("3. Do you want the md5 hash of the file?")
    choice = input("Enter your choice ('1/2/3'): ").strip()

    try:
        if choice == '1':

            key = input("Enter the metadata key you want: ").strip()
            result = subprocess.run(
                ["exiftool", f"-{key}", file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            else:
                print(f"Metadata for specific {key}: {result.stdout.strip()}")

        elif choice == '2':

            result = subprocess.run(
                ["exiftool", file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            else:
                print("All extracted metadata:")
                print(result.stdout.strip())

        elif choice == '3':

            os.system(f"md5sum {file}")

        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

    except Exception as e:
        print(f"An error occurred: {e}")
