def potencia(b,p):
    if p==0 or b==0:
        return 1
    else:
        return b*(potencia(b,p-1))

b=int(input("Ingresa la base"))
p=int(input("Ingresa la potencia"))
print(potencia(b,p))