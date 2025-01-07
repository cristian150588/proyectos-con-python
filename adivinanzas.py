# juego de adivinanza
import random


def juego_adivinanzas():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado= False

    print("!Bienvenidos al juego de adivinanz de numero de manquique")
    print("Tenes que adivinar el numero entre 1 y 100")
    print("!Vamos a intentarlo")

    while not adivinado:
        adivinanza = input("introduzca un numero de 1 al 100: ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero {adivinanza} es menor al numero secreto")

            elif adivinanza > numero_secreto:
                print(f"El numero {adivinanza} es mayor al numero secreto")

            else:
                print(
                    f"Adivinaste el numero {numero_secreto} era el numero secreto y lo adivinaste en {intentos} intentos"
                )
                break
        else:
            print("introduce un numero valido entre 1 y 100")
       
juego_adivinanzas()