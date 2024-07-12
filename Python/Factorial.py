#Indicar el resultado de el factorial de un numrero n

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    
n=int(input("Elige un numero:"))
print(f"El numero factorial de {n} es {factorial(n)}")