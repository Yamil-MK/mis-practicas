# 1. mostrar_encabezado_escuela
def mostrar_encabezado_escuela():
    print("INSTITUTO X")
    print("Titulo del reporte")

mostrar_encabezado_escuela()

# 2. obtener_nota_minima_aprobatoria
def obtener_nota_minima_aprobatoria():
    nota_minima = 6.0
    return nota_minima
    print(f"La nota minima para pasar es de: {nota_minima}")

obtener_nota_minima_aprobatoria()

# 3. evaluar_rendimiento
def evaluar_rendimiento(nota_final):
    return nota_final

calificacion = evaluar_rendimiento(8.3)
if calificacion <= 7.0:
    print(f"Tu rendimiento es {calificacion}, es Reprobatoria")
elif calificacion <= 9.4:
    print(f"Tu rendimiento es {calificacion}, es Aprobatoria")
else:
    print(f"Tu rendimiento es {calificacion}, es Excelente")

# 4. calcular_promedio_ponderado
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

resultado = calcular_promedio_ponderado(8.5, 4.5)
print(f"La calificacion final es: {resultado}")

# 5. generar_boleta
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    extraordinario = "Si" if nota_final < nota_minima else "No"

    print("-"*20)
    print("Boleta de calificaciones")
    print("-"*20)
    print(f"Nombre: {nombre_alumno}")
    print(f"Nota final: {nota_final}")
    print(f"Estado academico: {estado}")
    print(f"Necesita examen extraordinario: {extraordinario}")

generar_boleta("Juan Perez", 8.2, 6.7)