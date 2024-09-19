#Funcion que determina el valor del numero perfecto
def num_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
            resul= sum == num

    return resul

#Ingreso del numero entero
num =int(input("Digite un numero: "))

#Mensaje de repuesta.
if num_perfect(num) == True:
    print("El numero ingresado es prefecto")
else:
    print("El numero ingresado no es prefecto")
