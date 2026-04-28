"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) == 1:
    print("Insufficient arguments provided!")
elif sys.argv[1] == "--help":
    print("Usage: python main.py <file_path> <command> [arguments]...")
    print('add "task"')
    print('remove "task"')
    print("view")
elif len(sys.argv) == 2:
    pass
else:
    try:
        file_path = sys.argv[1]
        command = sys.argv[2]
        if command == "view":
            tasks = read_todo_file(file_path)
            print("Tasks:")
            for task in tasks:
                print(task)
        elif command == "add":
            try:
                task = sys.argv[3]  # puede lanzar IndexError
                tasks = read_todo_file(file_path)
                tasks.append(task)
                write_todo_file(file_path, tasks)
                print(f'Task "{task}" added.')
            except IndexError:
                print('Task description required for "add".')
        else:
            print("Command not found!")
    except Exception:
        pass
        