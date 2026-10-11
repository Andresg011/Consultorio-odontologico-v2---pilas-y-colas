from consultorio import Consultorio
from cita import Cita

agenda = Consultorio()

while True:
    print("1. Registrar una cita")
    print("2. Ver informe de extracciones urgentes")
    print("3. Generar agenda del dia")
    print("4. Atender siguiente cliente de la agenda")
    print("5. Consultar la agenda")
    print("6. Salir")

    try:
        opcion = int(input("Ingrese una opcion de 1 a 6: "))
    except ValueError:
        print("Error: debe ingresar un numero")
        continue

    if opcion == 1:
        print("Vamos a registrar una cita")
        while True:
            try:
                nombre = input("Escriba el nombre del cliente: ")
                tipo = input("Ingrese el tipo de atención (limpieza, diagnostico, calzas, extraccion): ")
                prioridad = input("Ingrese la prioridad (normal, urgente): ")
                fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
                cita = Cita(nombre, tipo, prioridad, fecha)
                agenda.agendar_cita(cita)
                print("Cita registrada correctamente")
                print("seleccione la opcion 3 para guardar")
                break
            except ValueError as error:
                print(f"Error: {error}")

    elif opcion == 2:
        urgentes = agenda.filtrar_extracciones_urgentes()
        urgentes_ordenados = agenda.ordenar_por_fecha(urgentes)
        agenda.generar_informe(urgentes_ordenados)

    elif opcion == 3:
        agenda.generar_agenda()

    elif opcion == 4:
        agenda.atender_siguiente_cita()

    elif opcion == 5:
        agenda.consultar_agenda()

    elif opcion == 6:
        print("Hasta luego")
        break

    else:
        print("Error: la opcion debe estar entre 1 y 6")