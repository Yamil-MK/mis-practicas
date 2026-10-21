# PASO 1
juegos_nintendoswitch = []

# PASO 2
juegos_totales = [
    "Zelda Ocarina of Time","Kirby y la Tierra Perdida", "Nintendo Switch Sports", "Splatoon Raiders", "Donkey Kong Bananza",
    "Pokemon Pokopia", "Metroid Prime", "Super Mario Oddsesey", "Splatoon 2", "Minecraft"
]

for juegos in juegos_totales:
    juegos_nintendoswitch.append(juegos)

print("Juegos totales en la pila: ", juegos_nintendoswitch)

# PASO 3
print("Ultimo juego en la pila: ", juegos_nintendoswitch[-1])

# PASO 4
primera_salida = juegos_nintendoswitch.pop()
print("Salida del juego 1: ", primera_salida)

segunda_salida = juegos_nintendoswitch.pop()
print("Salida del juego 2: ", segunda_salida)

tercera_salida = juegos_nintendoswitch.pop()
print("Salida del juego 3: ", tercera_salida)

cuarta_salida = juegos_nintendoswitch.pop()
print("Salida del juego 4: ", cuarta_salida)

print("La lista actual de los juegos despues de sus salidas: ", juegos_nintendoswitch)

# PASO 5
total_juegos = len(juegos_nintendoswitch)
print("Cantidad de juegos restantes: ", total_juegos)

if total_juegos == 0:
    print("La pila esta vacia, ya no existen elementos")
else:
    print("La pila todavia no esta vacia, existen elementos")

# PASO 6
while len(juegos_nintendoswitch) > 0:
    juegos_nintendoswitch.pop()
print("La pila esta completamente vacia: ", juegos_nintendoswitch)