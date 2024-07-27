def celsius_a_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

def fahrenheit_a_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# Mostrar opciones al usuario
opcion = int(input("Elige una opción:\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\nOpción: "))

# Procesar la opción seleccionada
if opcion == 1:
    c = float(input("Ingresa la temperatura en Celsius: "))
    f = celsius_a_fahrenheit(c)
    print(f"La temperatura en Fahrenheit es de {f:.2f} grados.")
elif opcion == 2:
    f = float(input("Ingresa la temperatura en Fahrenheit: "))
    c = fahrenheit_a_celsius(f)
    print(f"La temperatura en Celsius es de {c:.2f} grados.")
else:
    print("Opción no válida.")
