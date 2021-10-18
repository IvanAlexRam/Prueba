condicion = True

agenda_telefonos = {
    "Camilo" : 6269135,
    "Daniel" : 6269136,
    "Pilar" : 3286015, 
    "Bolt" : 4145577,
}

mensaje = (
    "------------------------------------------------\n"
    "Bienvenidos a la agenda de telefonos de python mision TIC\n"
    "---------------------------------------------------------\n"
    "Usted tiene las siguientes opciones \n"
    "2. Añadir contacto\n"
    "3. Modificar contacto\n"
    "4. Borrar contacto\n"
    "5. Salir \n"
)

while condicion:
    print(mensaje)
    opcion = input("Por favor elija una de las opciones definidas: ")

    while opcion not in("2", "3", "4", "5"):
        opcion = input()
    
    if opcion == "2":
        nombre = input("Digite el nombre que desea consultar: ")
        if nombre in agenda_telefonos:
            print("------------------------------------")
            print("El nombre ingresado ya se encuentra en su agenda")
        else:
            telefono = int(input("Por favor ingrese el numero que desea añadir: "))
            agenda_telefonos[nombre] = telefono
            print("------------------------------------")
            print(f"Hemos agregrado correctamente el contacto")
    
    if opcion == "3":
        nombre = input("Digite el nombre que desea consultar: ")
        if nombre not in agenda_telefonos:
            print("------------------------------------")
            print("El nombre ingresado no se encuentra en su agenda")
        else:
            telefono = int(input("Por favor ingrese el numero que desea añadir: "))
            agenda_telefonos[nombre] = telefono
            print("------------------------------------")
            print(f"Hemos modificado correctamente el contacto")

    if opcion == "4":
        nombre = input("Digite el nombre que desea consultar: ")
        if nombre not in agenda_telefonos:
            print("------------------------------------")
            print("El nombre ingresado no se encuentra en su agenda")
        else:
            del agenda_telefonos[nombre]
            print("------------------------------------")
            print(f"Hemos elimnado el contacto")
    
    if opcion == "5":
        condicion = False
    
print("Finalicé el programa")
