#1. Interfaz del programa:
#• El sistema debe mostrar un menú interactivo para que el usuario pueda elegir entre las diferentes 
#opciones del sistema (cargar pacientes, buscar paciente por Historia Clínica, determinar paciente con más/menos días 
#de internación, ordenar pacientes por número de historia clínica, salir del sistema, etc.).
#• El menú debe estar dentro de un bucle que permita al usuario realizar múltiples operaciones hasta que decida salir.


pacientes = []

def mostrar_menu():
    print("\n *** Sistema de gestion de clinica ***" 
"\n 1. Cargar pacientes"
"\n 2. Mostrar pacientes por historia clinica"
"\n 3. Buscar pacientes por historia clinica"
"\n 4. Paciente con mas dias de internacion"
"\n 5. Paciente con menos dias de internacion"
"\n 6. Pacientes con mas de 5 dias de internacion"
"\n 7. Promedios dias de internacion"
"\n 8. Salir del sistema")
    
#2. Cargar pacientes:
#• Permitir al usuario ingresar los datos de los pacientes, almacenando 
#la información en una lista anidada (arreglo bidimensional), como se muestra 
#en la imagen de arriba. La cantidad de pacientes a ingresar debe ser determinada por el usuario.

def agregar_paciente(pacientes):
    numero_hist_clinica = int(input(f"Ingrese el numero de la historia clinica del paciente : "))
    nombre = input(f"Ingrese el nombre del paciente {numero_hist_clinica}: ")
    edad = int(input(f"Ingrese la edad del paciente ´{numero_hist_clinica}´ que desea agregar: "))
    diagnostico = (input(f"Ingrese el diagnostico de ´{numero_hist_clinica}´: "))
    dias_internacion = int(input(f"Ingrese los dias de internacion de {numero_hist_clinica}: "))
    pacientes.append([numero_hist_clinica, nombre, edad, diagnostico, dias_internacion])
    print(f"Paciente '{numero_hist_clinica}' agregado al sistema.")

#3. Mostrar la lista de pacientes:
#• Imprimir en pantalla todos los datos de los pacientes almacenados en el arreglo bidimensional, 
#mostrando cada fila como un paciente.
def mostrar_pacientes(pacientes):
    for i in pacientes:
        print(f"Numero de historia clinica: {i[0]}, nombre: {i[1]}, Edad: {i[2]}, Diagnostico: {i[3]}, Dias de internacion: {i[4]}")

#4. Búsqueda de pacientes:
#• Implementar una función que, dado el número de historia clínica de un paciente, busque en la
#lista y muestre todos los datos de dicho paciente (o un mensaje indicando que no se encontró al paciente).
def buscar_paciente(pacientes):
    numero_busqueda = int(input("Ingrese el numero del paciente a buscar: "))
    
    for i in pacientes:
        if i[0] == numero_busqueda: 
            print(f"\n**Paciente encontrado: **")
            print(f"Numero de historia clinica: {i[0]}")
            print(f"Nombre del paciente: {i[1]}")
            print(f"Edad del paciente: {i[2]}")
            print(f"Diagnostico del paciente: {i[3]}")
            print(f"Dias de internacion: {i[4]}")
            return
    print("Paciente no encontrado.")


#5. Ordenamiento de pacientes:
#• Implementar una función que permita ordenar la lista de pacientes por el número de Historia Clínica 
#en forma ascendente. Se podrá utilizar cualquier algoritmo de ordenamiento.
def ordenar_pacientes(pacientes):
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][3] > pacientes[j+1][3]:  # Comparamos la Historia Clínica
                # Intercambiamos si el elemento encontrado es mayor
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

#6. Determinar el paciente con mayor cantidad de días de internación:
#• Implementar una función que calcule e imprima el paciente con más días de internación, mostrando sus datos completos.
def paciente_mayor_dias(pacientes : list[list]):
    paciente_mayor = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > paciente_mayor[4]:
            paciente_mayor = paciente
    print(f"Paciente con menos dias de internacion es: {paciente_mayor}")

def paciente_menor_dias(pacientes : list[list]):
    paciente_menor = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < paciente_menor[4]:
            paciente_menor = paciente
    print(f"Paciente con menos dias de internacion es: {paciente_menor}")

#8. Cantidad de pacientes con días de internación mayor a 5 días.
#• Implementar una función que recorra la lista de pacientes y cuente cuántos pacientes tienen más de 5 días de internación.
def internacion_mayor_5(pacientes):

    if not pacientes:
        print("No hay pacientes registrados.")
    else: 
        contador_pacientes = 0
        for pacientes in pacientes:
            if pacientes[4]>5:
                contador_pacientes +=1
        print(f"Cantidad de pacientes con mas de 5 dias de internacion: {contador_pacientes}")

#9. Promedio de días de internación de todos los pacientes.
#• Implementar una función que calcule el promedio de días de internación de todos los pacientes registrados.

def promedio_dias_internacion(pacientes):
    """Calcula el promedio de dias de internacion de todos los pacientes registrados"""
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        total_dias = 0
        for paciente in pacientes:
            total_dias += paciente[4]
        promedio = total_dias / len(pacientes)
        print(f"Promedio de dias de internacion de todos los pacientes {promedio:2f}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == "1":
            agregar_paciente(pacientes)
        elif opcion == "2":
            mostrar_pacientes(pacientes)
        elif opcion == "3":
            buscar_paciente(pacientes)
        elif opcion == "4":
            paciente_mayor_dias(pacientes)
        elif opcion == "5":
            paciente_menor_dias(pacientes)
        elif opcion == "6":
            internacion_mayor_5(pacientes)
        elif opcion == "7":
            promedio_dias_internacion(pacientes)
        elif opcion == "8":
            print("Salir del Sistema.")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

main()



