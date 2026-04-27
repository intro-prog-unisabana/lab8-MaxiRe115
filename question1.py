"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys
if len(sys.argv) != 3:
    
    try:
        newtons = float(sys.argv[1])
    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")
    try:
        soporte = float(sys.argv[2])
    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")
    try:
        load_per_support = newtons / soporte
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
print(f"Load per support point: {load_per_support:.2f} N")   