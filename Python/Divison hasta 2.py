def dividirhasta2(n):
    if n%2 !=0:
        return n
    else:
        return dividirhasta2(n/2)
n=int(input("Ingresa un numero:"))

print(dividirhasta2(n))