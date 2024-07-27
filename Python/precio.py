#Ingresa el precio oriiginal del producto

precio=float(input("Ingresa el precio del producto:"))

descuento=float(input("Ingresa el descuento en porcentaje:"))

preciofinal=precio*descuento/100
preciofinal2=precio-preciofinal

print(f"EL precio final del producto es de ${preciofinal2} mientras que el precio original era de ${precio} ")