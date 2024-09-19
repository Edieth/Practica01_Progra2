def division(divid, div):

#Excluir que el divisor no sea cero

    if div == 0:
        return "El divisor no puede ser cero."

    cociente = 0
    residuo = abs(divid)
    div_abs = abs(div)

#Resta repetida para encontrar el cociente

    while residuo >= div_abs:
        residuo -= div_abs
        cociente += 1

    if (divid < 0) != (div < 0):
        cociente = -cociente
    if divid < 0:
        residuo = -residuo

    return cociente, residuo

#Ingreso de informacion

divid = int(input("Ingrese el dividendo: "))
div = int(input("Ingrese el divisor: "))

try:
    divid = int(input("Ingrese el dividendo: "))
    div = int(input("Ingrese el divisor: "))

    resul = division(divid, div)

    if isinstance(resul, str):
        print(resul)
    else:
        cociente, residuo = resul
        print(f"Resultado de la división: {cociente}")
        print(f"Residuo de la división: {residuo}")

except ValueError:
    print("Error: Por favor ingrese números enteros válidos.")
