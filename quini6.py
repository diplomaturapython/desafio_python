import random

grilla=[]
sorteo=[]
player1=[]
player2=[]
contador=0
numero_sorteo=0
#Lleno la lista con los números

for i in range(46):
    grilla.append(i)

#################################

#Compro los numeros para los jugadores

player1=random.sample(range(46), 6)
player2=random.sample(range(46), 6)

##################################################
#Comienza el sorteo
while grilla and player1 and player2:
    numero_sorteo = random.choice(grilla)
    sorteo.append(numero_sorteo)

    if numero_sorteo in player1:
        player1.remove(numero_sorteo)

    if numero_sorteo in player2:
        player2.remove(numero_sorteo)

    grilla.remove(numero_sorteo)

# Mostrar resultados
print("Números sorteados:", sorteo)
print("Player1 restante:", player1)
print("Player2 restante:", player2)

# ¿Quién ganó?
if not player1 and not player2:
    print("¡Empate! Ambos jugadores completaron sus números al mismo tiempo.")
elif not player1:
    print("¡Player 1 ganó!")
elif not player2:
    print("¡Player 2 ganó!")



