
# #1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159265359
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area} y su perímetro es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.


segundos = int(input("Introduce la cantidad de segundos: "))
horas = segundos // 3600  
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

if numero1 != 0 and numero2 != 0:
    suma = numero1 + numero2
    division = numero1 / numero2
    multiplicacion = numero1 * numero2
    resta = numero1 - numero2
    print(f"La suma de {numero1} y {numero2} es {suma}")
    print(f"La división de {numero1} y {numero2} es {division}")
    print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}")
    print(f"La resta de {numero1} y {numero2} es {resta}")
else:
    print("Los numeros introducidos no pueden ser igual a 0")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. El índice de masa corporal se calcula con la fórmula: peso / altura^2

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / altura ** 2
print(f"Tu índice de masa corporal es {imc:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. La fórmula de conversión es: F = C * 9/5 + 32

celsius = float(input("Introduce una temperatura en grados Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de {numero1}, {numero2} y {numero3} es {promedio:.2f}")