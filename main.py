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
elif len(sys.argv) == 2:
    pass
else:
    try:
        file_path = sys.argv[1]
        args = iter(sys.argv[2:])
        tasks = read_todo_file(file_path)
        error = False
        for command in args:
            if command == "add":
                try:
                    task = next(args)
                    tasks.append(task)
                    print(f'Task "{task}" added.')
                except StopIteration:
                    print('Task description required for "add".')
                    error = True
                    break
            elif command == "remove":
                try:
                    task = next(args)
                    try:
                        tasks.remove(task)
                        print(f'Task "{task}" removed.')
                    except ValueError:
                        print(f'Task "{task}" not found.')
                except StopIteration:
                    print('Task description required for "remove".')
                    error = True
                    break
            elif command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("Command not found!")
                error = True
                break
        if not error:
            write_todo_file(file_path, tasks)
    except Exception:
        pass
        