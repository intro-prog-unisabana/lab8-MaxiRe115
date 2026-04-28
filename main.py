"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) == 1:
    print("Insufficient arguments provided!")
elif sys.argv[1] == "--help":
    print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
elif len(sys.argv) < 3:
    print("Insufficient arguments provided!")
else:
    try:
        file_path = sys.argv[1]
        command = sys.argv[2]
        tasks = read_todo_file(file_path)
        if command == "add":
            try:
                task = sys.argv[3]
                tasks.append(task)
                write_todo_file(file_path, tasks)
                print(f'Task "{task}" added.')
            except IndexError:
                print('Task description required for "add".')
        elif command == "remove":
            try:
                task = sys.argv[3]
                try:
                    tasks.remove(task)
                    write_todo_file(file_path, tasks)
                    print(f'Task "{task}" removed.')
                except ValueError:
                    print(f'Task "{task}" not found.')
            except IndexError:
                print('Task description required for "remove".')
        elif command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
        else:
            print("Command not found!")
    except Exception:
        pass
        