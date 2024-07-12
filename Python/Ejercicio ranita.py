#Un ranita está parada en el número 1 de la recta numérica. 
# Va a ir dando saltos del tamaño del número entero en el que caiga. 
# Por ejemplo, el primer salto será uno, y el segundo 2 
# ¿En qué número estará en su octavo salto?.

def posicion_ranita(n):
    # Inicializamos la posición de la ranita en 1
    posicion = 1
    
    # Recorremos desde el primer salto hasta el enésimo salto
    for i in range(1, n + 1):
        posicion += i
    
    return posicion

# Solicitar al usuario el número de saltos
num_saltos = int(input("Ingresa el número de saltos: "))
posicion_final = posicion_ranita(num_saltos)
print(f"La ranita estará en el número {posicion_final} después de {num_saltos} saltos.")
