#Calculadora basica, sirve para poder sumar, restar, dividir y multiplicar 2 valores.
#Variables para almacenar los 2 numeros ingresados.
#Se utiliza el tipo float como tipo, para que no haya problemas al ingresar numeros con decimales.
numero1 = float(input("Ingrese un numero: "))
operador = input("Elija el operador para realizar la operacion ( +, -, *, / ): ")
numero2 = float(input("Ingrese otro numero: "))

#Se utiliza la condicional para saber que operador elije el usuario. (suma)
if operador == "+":
    resultado = numero1 + numero2
#Se utiliza la condicional para saber que operador elije el usuario. (resta)
elif operador == "-":
    resultado = numero1 - numero2
#Se utiliza la condicional para saber que operador elije el usuario. (multiplicacion)
elif operador == "*":
    resultado = numero1 * numero2
#Se utiliza la condicional para saber que operador elije el usuario. (division)
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error, division por 0"
else: resultado = "Operador no valido"
#Imprimimos en consola el resultado de la operacion realizada.
print(f"El resultado de {numero1} {operador} {numero2} es: {resultado}")


    