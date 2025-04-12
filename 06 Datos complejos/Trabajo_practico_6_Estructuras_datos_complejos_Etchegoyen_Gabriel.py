#Trabajo Practico 6: Estructuras de datos complejas
#Estudiante: Etchegoyen Gabriel

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

listado_frutas = list(precios_frutas.keys())
print(listado_frutas)

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

sujeto1 = Persona("Gabriel", "Argentina", 20)
sujeto1.saludar()

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

prueba = Circulo(5)
print(f"El área del círculo es: {prueba.calcular_area()}")
print(f"El perímetro del circulo es: {prueba.calcular_perimetro()}")

# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.


string = "({[]})"

class Pila:

    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return self.items == []


def esta_balanceado(cadena):
    pila = Pila()
    cierre = {')': '(', '}': '{', ']': '['}
    for c in cadena:
        print(c)      
        if c in cierre.values():
          pila.apilar(c)
        else:
          apertura = pila.desapilar()
          
          if apertura is None:
            return False
          if apertura != cierre.get(c):
            return False
    return True

intento1 = esta_balanceado(string)
intento2 = esta_balanceado("(({[]))")
print(intento1)
print(intento2)

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila.

from collections import deque

class Cola():
  def __init__(self):
    self.cola = deque()
    
  def agregar_clientes(self,cliente):
    self.cola.append(cliente)

  def atender_clientes(self):
    return self.cola.popleft() if len(self.cola) > 0 else None 

  def mostrar_siguiente(self):
    return self.cola[0] if len(self.cola) > 0 else None 

      
fila = Cola()
fila.agregar_clientes("juancito")
fila.agregar_clientes("Lolo Polo")
fila.agregar_clientes("Luciano")
fila.mostrar_siguiente()
print(fila.atender_clientes())
print(fila.atender_clientes())
print(fila.atender_clientes())
print(fila.atender_clientes())
print(fila.mostrar_siguiente())

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.

class Nodo:
    def __init__ (self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__ (self):
        self.cabeza = None
  
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None")  

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.mostrar()

#9) Dada una lista enlazada, implementa una función para invertirla.

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None")

    def invertida(self):
        lista_invertida = ListaEnlazada()
        actual = self.cabeza
        while actual:
            lista_invertida.insertar(actual.dato)
            actual = actual.siguiente
        return lista_invertida

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)

print("Lista original:")
lista.mostrar()

print("Lista invertida:")
lista_invertida = lista.invertida()
lista_invertida.mostrar()