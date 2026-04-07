import sys
from mycli.commands import startproject

COMMANDS = {
    "startproject": startproject.run,
}

def main():
    if len(sys.argv) < 3:
        print("Usage: scrapping-cli startproject <project_name>")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        print("Available commands: startproject")
        return

    COMMANDS[command](*args)


if __name__ == "__main__":
    main()