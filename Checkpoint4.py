#Ejercicio 1:
# Lista
lista = [6, "Train", 7, 8, 9, 10]

#Tupla
tupla = (50, 60, 70 )

# Operación con Floats
altura = 1.95
peso = 80.5
imc = peso / (altura ** 2)  


# Número entero
numero_entero = 28

# Número decimal 
from decimal import Decimal
tasa_interes = Decimal("0.02")
cantidad = Decimal("100.00")
interes = cantidad * tasa_interes


# Diccionario
diccionario = {
    "nombre": "Teresa",
    "edad": 25,
    "ocupacion": "Manager",
}


print("Lista:", lista)
print("Tupla:", tupla)
print("Float", imc)
print("Entero:", numero_entero)
print("Decimal", interes)
print("Diccionario:",diccionario)

print()

#Ejercicio 2:
import math

print(imc)
float_redondeado = math.ceil(21.17028270874425)

print(float_redondeado)

#Ejercicio 3:
print(imc)
raiz_cuadrada_float = math.sqrt(21.17028270874425)

print(raiz_cuadrada_float)

#Ejercicio 4:

elemento_1 = list(diccionario.items())[0]

print(elemento_1)

#Ejercicio 5:

elemento_2 = tupla [1]

print(elemento_2)

#Ejercicio 6:

lista.append(11)

print(lista)

#Ejercicio 7:

lista[0] = "Dog"

print(lista)

#Ejercicio 8:

lista = [str(x) for x in lista]
lista.sort()

print(lista)

#Ejercicio 9:

nuevo_elemento = "Chocolate"
tupla = tupla + (nuevo_elemento,)

print(tupla)