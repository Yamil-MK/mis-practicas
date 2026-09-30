import datetime

def saludar():
    print("Hola, Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es: {resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")
    saludar_persona("Raul",19)
