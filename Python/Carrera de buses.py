import random
import time
import os

# Función para limpiar la consola
def clear_console():
    os.system('clear')

# Función para mostrar el estado de la carrera
def print_race(buses):
    bus_art = [
        "  ______",
        " /|_||_\`.__",
        "(   _    _ _\\",
        "=`-(_)--(_)-' "
    ]
    for bus in buses:
        for line in bus_art:
            print(" " * bus + line)
        print()

# Función principal del juego
def race():
    # Número de buses y longitud de la carrera
    num_buses = 5
    race_length = 50
    
    # Inicializar posiciones de los buses
    buses = [0] * num_buses
    
    # Bucle de la carrera
    while max(buses) < race_length:
        clear_console()
        print_race(buses)
        for i in range(num_buses):
            buses[i] += random.randint(0, 2)  # Cada bus avanza entre 0 y 2 espacios
        time.sleep(0.3)  # Pausa para hacer la animación más visible
    
    # Determinar el ganador
    winner = buses.index(max(buses)) + 1
    clear_console()
    print_race(buses)
    print(f"¡El autobús {winner} ha ganado la carrera!")

# Ejecutar el juego
if __name__ == "__main__":
    race()
