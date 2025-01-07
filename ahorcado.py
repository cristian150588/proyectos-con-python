import random


def obtener_palabra_secreta() -> str:
    palabras = ["python", "javascript", "typescript", "flask", "git", "react", "django"]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tienes {intentos} intentos para adivinar la palabra")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")

    while not juego_terminado:
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Ganaste! La palabra era {palabra_secreta}.")
            break

        print(f"Te quedan {intentos} intentos.")
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor, introduce una sola letra válida.")
        elif adivinanza in letras_adivinadas:
            print(f"Ya usaste la letra '{adivinanza}', elige otra.")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"¡Muy bien! La letra '{adivinanza}' está en la palabra secreta.")
            else:
                intentos -= 1
                print(f"La letra '{adivinanza}' no está en la palabra secreta.")
                
            if intentos == 0:
                juego_terminado = True
                print(f"Perdiste. La palabra correcta era {palabra_secreta}.")

juego_ahorcado()
