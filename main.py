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
if len(sys.argv) == 3:
    try:
        if sys.argv[2] == 'view':
            print("\nTasks:")
            tareas = read_todo_file(archivo)
            for x in tareas:
                print(x)
    except ValueError:
        print("Command not found!")
else:
    pass
        