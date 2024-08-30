# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import validaciones as val
from paciente import Paciente
from clinica import Clinica
from turno import Turno

def obtener_id():
    '''
    Esta función lee el archivo json para obtener el último id 
    '''
    with open('configs.json', 'r') as file:
        datos = json.load(file)

    lista_pacientes = datos['lista_pacientes']

    if lista_pacientes:
        ultimo_paciente = lista_pacientes[-1]
        ultimo_id = ultimo_paciente.get('id')
    else:
        ultimo_id = 0

    return int(ultimo_id)


id_auto_incremental = obtener_id()


def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1

def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1



def clear_console():
    """
    The function `clear_console` prompts the user to press Enter to continue and then clears the console
    screen based on the operating system.
    """
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    



def UTN_messenger(message: str, message_type: str = None, new_line: bool = False) -> None:
    """
    This is a Python function that prints a message with a specific color and message type.
    
    :param message: The message that needs to be displayed in the console
    :param message_type: The type of message being passed, which can be 'Error', 'Success', 'Info',
    or None. If None, the message will be printed without any formatting
    """
    _b_red: str = '\033[41m'
    _b_green: str = '\033[42m'
    _b_blue: str = '\033[44m'
    _f_white: str = '\033[37m'
    _no_color: str = '\033[0m'
    message_type = message_type.strip().capitalize()
    new_line_char = '\n'
    final_message = f'{new_line_char if new_line else ""}'
    match message_type:
        case 'Error':
            final_message += f'{_b_red}{_f_white}> Error: {message}{_no_color}'
        case 'Success':
            final_message += f'{_b_green}{_f_white}> Success: {message}{_no_color}'
        case 'Info':
            final_message += f'{_b_blue}{_f_white}> Information: {message}{_no_color}'
        case _:
            final_message += message
    print(final_message)


def cargar_json_en_memoria ():
    '''
    Esta función se encarga de leer el json y cargar los datos en memoria

    Datos:

    Especialidades (dict)

    Obras sociales válidas (dict)

    Lista de pacientes (list)
    '''
    with open('configs.json', 'r', encoding='utf-8') as file:
        datos = json.load(file)

    #Cargo las especialidades y obras sociales
    especialidades = datos['especialidades']
    obras_sociales_validas = datos['obras_sociales_validas']

    #Cargo la lista de pacientes
    lista_pacientes = []
    for diccionario in datos['lista_pacientes']:

        paciente = Paciente(diccionario)
        lista_pacientes.append(paciente)


    return especialidades, obras_sociales_validas, lista_pacientes


def cargar_clinica():
    especialidades, obras_sociales_validas, lista_pacientes = cargar_json_en_memoria()

    clinica = Clinica(
        razon_social="Clinica privada",
        lista_pacientes=lista_pacientes,
        lista_turnos=[],
        especialidades=especialidades,
        obras_sociales_validas=obras_sociales_validas,
        recaudacion=0.0,
        hay_pacientes_sin_atencion=False
    )

    return clinica


def alta_paciente(clinica: Clinica):
    '''
    Esta función se encarga de solicitar y validar los datos para dar de alta un paciente
    '''
    nombre = val.validar_nombre()
    apellido = val.validar_apellido()
    dni = val.validar_dni(clinica.get_lista_pacientes())
    edad = val.validar_edad()
    fecha = val.validar_fecha()
    obra_social = val.validar_obra_social()
    incrementar_id()

    paciente = {
        "id": id_auto_incremental,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "fecha_de_registro": fecha,
        "obra_social": obra_social
    }
    
    objeto_paciente = Paciente(paciente)

    clinica.get_lista_pacientes().append(objeto_paciente)

    UTN_messenger('Paciente agregado con éxito', 'Success')



def calcular_monto_a_pagar(paciente: Paciente, precio_base: float = 4000) -> float:
    '''
    Esta función recibe un paciente y calcula el monto a pagar dependiendo de su obra social y edad
    '''
    obra_social = paciente.get_obra_social()
    edad = paciente.get_edad()
    monto = precio_base

    if obra_social == "Swiss Medical":
        monto *= 0.60
        if 18 <= edad <= 60:
            monto *= 0.90

    elif obra_social == "Apres":
        monto *= 0.75
        if 26 <= edad <= 59:
            monto *= 0.97

    elif obra_social == "PAMI":
        monto *= 0.40
        if edad >= 80:
            monto *= 0.97

    elif obra_social == "Particular":
        monto *= 1.05
        if 40 <= edad <= 60:
            monto *= 1.15
    
    return monto



def alta_turno(clinica: Clinica):
    '''
    Esta función se encarga de asignar un turno a un paciente que ya se encuentre en el sistema
    '''
    paciente = val.validar_paciente_turno(clinica.get_lista_pacientes())
    
    especialidades_validas = list(clinica.get_especialidades().values())
    
    while True:
        print(f"Especialidades disponibles: {', '.join(especialidades_validas)}")
        especialidad = input("Ingrese la especialidad para el turno: ")

        if val.validar_string(especialidad):
            especialidad = especialidad.strip().title()

            if especialidad not in especialidades_validas:
                UTN_messenger('Especialidad no válida', 'Error')

            else:
                break
    
    monto_a_pagar = calcular_monto_a_pagar(paciente)
    estado_del_turno = "Activo"
    
    ultimo_id = clinica.get_lista_turnos()[-1].get_id() if clinica.get_lista_turnos() else 0
    nuevo_id = ultimo_id + 1
    
    nuevo_turno = Turno(nuevo_id, paciente.get_id(), especialidad, monto_a_pagar, estado_del_turno)
    
    clinica.get_lista_turnos().append(nuevo_turno)
    
    UTN_messenger('Turno agregado exitosamente', 'Success')



def quick_sort(elemento: list, key=None):
    if len(elemento) <= 1:
        return elemento
    
    pivot = elemento.pop()
    mas_chicos = [x for x in elemento if key(x) <= key(pivot)]
    mas_grandes = [x for x in elemento if key(x) > key(pivot)]

    return quick_sort(mas_chicos, key) + [pivot] + quick_sort(mas_grandes, key)



def mostrar_turnos_ordenados(clinica, criterio: str):
    '''
    Esta función se encarga de llamar a la función quick sort y ordenar los turnos en base a la obra social o monto
    '''
    lista_turnos = clinica.get_lista_turnos()

    def key_func(turno):
        if criterio == "obra_social_asc":
            paciente = next((paciente for paciente in clinica.get_lista_pacientes() if paciente.get_id() == turno.get_id_paciente()), None)
            return paciente.get_obra_social() if paciente else ""
        elif criterio == "monto_desc":
            return turno.get_monto_a_pagar()

    turnos_ordenados = quick_sort(lista_turnos[:], key=key_func)

    if criterio == "monto_desc":
        turnos_ordenados.reverse()

    for turno in turnos_ordenados:
        paciente = next((paciente for paciente in clinica.get_lista_pacientes() if paciente.get_id() == turno.get_id_paciente()), None)
        obra_social = paciente.get_obra_social() if paciente else "No disponible"

        print(f"ID: {turno.get_id()}, ID Paciente: {turno.get_id_paciente()}, Obra social: {obra_social} Especialidad: {turno.get_especialidad()}, Monto a Pagar: ${turno.get_monto_a_pagar()}, Estado: {turno.get_estado_del_turno()}")



def ordenar_turnos(clinica):
    '''
    Esta función da a elegir el criterio de ordenamiento y llama a las demás funciones relacionadas
    '''
    while True:
        print("[1] Obra Social ASC")
        print("[2] Monto DESC")
        opcion = input("Seleccione el criterio de ordenamiento: ")
        if opcion == '1':
            mostrar_turnos_ordenados(clinica, 'obra_social_asc')
            break
        elif opcion == '2':
            mostrar_turnos_ordenados(clinica, 'monto_desc')
            break
        else:
            UTN_messenger('Opción incorrecta', 'Error')
            