import random

# Función para generar la grilla de números
def generar_grilla():
    return list(range(46))

# Función para generar un jugador con 6 números únicos
def generar_jugador():
    return random.sample(range(46), 6)

# Función principal del sorteo
def sorteo_quini6(grilla, player1, player2):
    sorteo = []

    while grilla and player1 and player2:
        numero_sorteo = random.choice(grilla)
        sorteo.append(numero_sorteo)

        print(f"Número sorteado: {numero_sorteo}")

        if numero_sorteo in player1:
            player1.remove(numero_sorteo)
            print("¡Player 1 tenía el número!")

        if numero_sorteo in player2:
            player2.remove(numero_sorteo)
            print("¡Player 2 tenía el número!")

        grilla.remove(numero_sorteo)

        print("-" * 30)

    return sorteo, player1, player2

# Función para mostrar el resultado final
def mostrar_resultados(sorteo, player1, player2):
    print("\nNúmeros sorteados:", sorteo)
    print("Player1 restante:", player1)
    print("Player2 restante:", player2)

    if not player1 and not player2:
        print("¡Empate! Ambos jugadores completaron sus números al mismo tiempo.")
    elif not player1:
        print("¡Player 1 ganó!")
    elif not player2:
        print("¡Player 2 ganó!")

# ----------- EJECUCIÓN PRINCIPAL -----------
def main():
    grilla = generar_grilla()
    player1 = generar_jugador()
    player2 = generar_jugador()

    print("Player 1:", player1)
    print("Player 2:", player2)
    print("=" * 30)

    sorteo, restante1, restante2 = sorteo_quini6(grilla, player1, player2)
    mostrar_resultados(sorteo, restante1, restante2)

# Llamada principal
if __name__ == "__main__":
    main()
