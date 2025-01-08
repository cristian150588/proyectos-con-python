def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar un contacto")
    print("3. Buscar un contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("_" * 20)


def agregar_contacto(agenda):
    nombre = input("por favor introduzca nombre completo del contacto: ")
    telefono = input("por favor introduzca numero de telefono del contacto: ")
    email = input("por favor introduzca email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"se ha agregado el contacto {nombre} correctamente")


def eliminar_contacto(agenda):
    nombre = input("ingrese nombre de la agenda que se desea elminiar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"el contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"no se ha encontrado el nombre {nombre}")


def buscar_contacto(agenda):
    nombre = input("ingrese nombre de contacto:")
    if nombre in agenda:
        print(f"Nombre:{nombre}")
        print(f"Telefono:{agenda [nombre]['telefono']}")
        print(f"Email:{agenda[nombre]['email']}")
    else:
        print(f"el contacto {nombre} no fue encontrado en la agenda")


def listar_contactos(agenda):
    if agenda:
        print("\n lista de contactos:")
        for nombre, info in agenda.items():
            print(f"nombre: {nombre}")
            print(f"telefono: {info['telefono']}")
            print(f"email: {info['email']}")
            print("_" * 20)
    else:
        print("la agenda aun esta vacia")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("por favor elija una opcion: ")
        print(" " * 20)
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("saliendo de la agenda")
            break
        else:
            print("por favor seleccione una opcion correcta")


agenda_contactos()
