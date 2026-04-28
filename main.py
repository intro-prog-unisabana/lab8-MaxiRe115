"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
try:
    if len(sys.argv) >= 2:
        archivo = sys.argv[1]
        print("Command-line arguments:")
        for i in archivo:
            print(i)
        print("\nTasks:")
        tareas = read_todo_file(archivo)
        for x in tareas:
            print(x)
    else:
        print("Insufficient arguments provided!")
except IndexError as e:
    print(e)
if len(sys.argv) < 3:
    pass  
else:
    file_path = sys.argv[1]
    command = sys.argv[2]
    if command == "view":
        tasks = read_todo_file(file_path)
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("Command not found!")
        