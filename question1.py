"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys
if len(sys.argv) != 3:
    print("Error: Invalid input! Enter numeric values only.")
else:
    try:
        newtons = float(sys.argv[1])
        soporte = float(sys.argv[2])
        if soporte == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        else:
            load_per_support = newtons / soporte
            print(f"Load per support point: {load_per_support:.2f} N")
    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")