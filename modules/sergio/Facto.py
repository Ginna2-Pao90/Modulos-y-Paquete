def factorial():
    numero = int(input("ingrese un numero: "))
    factor = int(1)
    for s in range(1, numero + 1):
        factor = factor * s
    print("el numero de la factorial es: " + str(factor))
