import sys
from mycli.commands import startproject

COMMANDS = {
    "startproject": startproject.run,
}

def main():
    if len(sys.argv) < 3:
        print("Usage: mycli <command> <project_name>")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command in COMMANDS:
        COMMANDS[command](*args)
    else:
        print(f"Unknown command: {command}")