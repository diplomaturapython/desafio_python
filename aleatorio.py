import random

def generar_lista_aleatoria(tamano_lista, rango_minimo, rango_maximo):
    if tamano_lista > (rango_maximo - rango_minimo + 1):
        raise ValueError("El tamaño de la lista no puede ser mayor que el rango de números disponibles")
    
    lista_aleatoria = []
    while len(lista_aleatoria) < tamano_lista:
        numero = random.randint(rango_minimo, rango_maximo)
        if numero not in lista_aleatoria:
            lista_aleatoria.append(numero)
    
    return lista_aleatoria

print(generar_lista_aleatoria(30, 1, 100))