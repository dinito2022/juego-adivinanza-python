import random

numero_secreto= random.randint(0,20)
adivinado= False

print("Bienvenido al juego de avidivinar el numero secreto!")
i=0
while not adivinado:
    print("-----------------",numero_secreto,"adivinado  ",adivinado)
    numero= input("introduce un numero del 1 al 20 :")
    numeroCasteado=int(numero)
    i+=1
    if numeroCasteado==numero_secreto:
        print("Felicidades adivinaste el nummero secreto al intento:",i)
        adivinado= True