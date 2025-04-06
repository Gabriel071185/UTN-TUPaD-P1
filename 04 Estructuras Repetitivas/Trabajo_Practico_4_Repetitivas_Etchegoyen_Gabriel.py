#Trabajo Practico 4: Estrucuturas Repetitivas
#Estudiante: Etchegoyen Gabriel

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i, end="\n")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

ingreso = int(input("Ingrese un número entero: "))
num = ingreso
digitos = 0
while ingreso > 0:
    ingreso //= 10
    digitos += 1
print(f"El número {num} tiene {digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero de inicio de valor: "))
num2 = int(input("Ingrese un numero de fin de valor: "))
suma= 0 
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es: {suma}.")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0 

while (num := int(input("Escriba un número: "))) != 0:
    suma += num 
    print(f"Su acumulado al momento es:{suma}")
print(f"El programa termino y su total es {suma}")    



# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
contador = 0
while (num := int(input("Pruebe su suerte: "))) != random.choice(range(10)):
    contador += 1
    print(f"Intente otra vez")
print(f"Felicidades el {num} es correcto y utilizó {contador} intentos")  



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i, end="\n")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print(f"La suma de los números entre 0 y {num} es: {suma}.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad = 100
acumulador = 0
for i in range(cantidad):
  num= int(input("ingrese su valor a calcular: "))
  acumulador += num
print(f"La media de los numeros ingresados es: {acumulador/cantidad}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número entero: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print(f"El número invertido es: {invertido}.")