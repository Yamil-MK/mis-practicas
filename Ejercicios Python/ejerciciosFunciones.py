import random

#Funciones
def lanzar_dado():
    resultado = random.randint(1,6)
    return resultado
numero_obtenido = lanzar_dado()
print(f"El numero que cayo es el: {numero_obtenido}")

def despedirse():
    print("¡Adios a todos!")
despedirse()

#Funciones con 2 parametros
def calcular_suma(a,b):
    return a + b
resultado = calcular_suma(15,8)
print(resultado)

def calcular_area(base,altura):
    area=(base*altura)
    return area
resultado=calcular_area(10,5)
print(f"El area de la figura es: {resultado}")
