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

from paciente import Paciente
from datetime import datetime



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


def validar_string(string: str) -> bool:
    '''
    Esta función recibe un string 

    Retorna True si es un string alfabético

    Retorna False si no es un string alfabético
    '''
    retorno = True
    palabras = string.split()

    for palabra in palabras:
        if not palabra.isalpha():
            retorno = False

    return retorno


def validar_nombre() -> str:
    '''
    Esta función recibe un string y valida que sea un nombre que cumpla con los requisitos

    (No puede exceder los 30 caracteres ni contener números o caracteres especiales)
    '''
    bandera = False

    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if len(nombre) > 30:
            UTN_messenger('El nombre no debe superar los 30 caracteres', 'Error')
            continue

        lista_palabras = nombre.split(' ')

        for palabra in lista_palabras:
            if palabra.isalpha() != True:
                UTN_messenger('Debe ingresar un nombre compuesto solamente por caracteres alfabéticos', 'Error')
                bandera = False
                break
            else:
                palabra = palabra.capitalize()
                bandera = True

        if bandera:
            UTN_messenger('Nombre agregado con éxito', 'Success')
            break

    return nombre.capitalize()



def validar_apellido() -> str:
    '''
    Esta función recibe un string y valida que sea un apellido que cumpla con los requisitos
    
    (No puede exceder los 30 caracteres ni contener números o caracteres especiales)
    '''
    bandera = False

    while True:
        apellido = input("Ingrese el apellido del paciente: ")
        if len(apellido) > 30:
            UTN_messenger('El apellido no debe superar los 30 caracteres', 'Error')
            continue

        lista_palabras = apellido.split(' ')

        for palabra in lista_palabras:
            if palabra.isalpha() != True:
                UTN_messenger('Debe ingresar un apellido compuesto solamente por caracteres alfabéticos', 'Error')
                bandera = False
                break
            else:
                palabra = palabra.capitalize()
                bandera = True

        if bandera:
            UTN_messenger('Nombre agregado con éxito', 'Success')
            break

    return apellido.capitalize()


def validar_edad() -> int:
    '''
    Esta funcion recibe un string y valida que sea una edad válida 

    (Un número entero entre 18 y 90)
    '''

    while True:
        edad = input("Ingrese la edad del paciente: ")
        if edad.isdigit() != True:
            UTN_messenger('Asegúrese de ingresar un número válido', 'Error')
        elif int(edad) < 18 or int(edad) > 90:
            UTN_messenger('La edad del paciente debe estar entre 18 y 90 años', 'Error')
        else:
            UTN_messenger('edad agregada correctamente', 'Success')
            break

    return int(edad)


def validar_dni(lista_pacientes: list[Paciente]) -> str:
    '''
    Esta función valida que el dni ingresado no coincida con uno de los dni ya cargados en memoria
    '''

    while True:
        dni_ingresado = input("Ingrese el DNI del paciente: ")
        if dni_ingresado.isnumeric():
            coincidencia_dni = list(filter(lambda paciente: paciente.get_dni() == dni_ingresado, lista_pacientes))

            if not coincidencia_dni:
                UTN_messenger('DNI ingresado correctamente', 'Success')
                break
            else:
                UTN_messenger('El DNI ya está siendo usado', 'Error')
        else:
            UTN_messenger('Ingrese un DNI válido', 'Error')

    return dni_ingresado



def validar_fecha() -> str:
    '''
    Esta función valida que la fecha ingresada sea una fecha válida en el formato DD-MM-AAAA
    '''

    while True:
        fecha_ingresada = input("Ingrese la fecha de registro con el siguiente formato: DD-MM-AAAA: ")

        try:
            fecha_formateada = datetime.strptime(fecha_ingresada, '%d-%m-%Y')
            break

        except ValueError:
            UTN_messenger('Asegúrese de ingresar la fecha en el formato correcto: ', 'Error')
    
    fecha_final = datetime.strftime(fecha_formateada, '%d-%m-%Y')

    return fecha_final



def validar_obra_social() -> str:
    '''
    Esta función valida que la obra social ingresada se encuentre dentro de la lista de obras sociales válidas
    '''
    
    obras_sociales_validas = ['Swiss Medical', 'Apres', 'PAMI', 'Particular']

    while True:

        obra_social_ingresada = input('Ingrese la obra social del paciente: ')

        coincidencias = list(filter(lambda obra: obra == obra_social_ingresada, obras_sociales_validas))

        if coincidencias:
            UTN_messenger('Obra social ingresada con éxito', 'Success')
            break
        else:
            UTN_messenger(f'La obra social no coincide con las opciones válidas: {obras_sociales_validas}', 'Error')
        
    return obra_social_ingresada



def validar_paciente_turno(lista_pacientes: list[Paciente]):
    '''
    Esta función se encarga de validar que el paciente se encuentra en el sistema, usando id o dni

    Retorna el paciente al ingresar un id/dni válido
    '''

    elecciones_posibles = ['dni', 'id']
    paciente = None

    while True:
        eleccion = input('Asignar el turno usando id o dni? ')

        if eleccion.lower() not in elecciones_posibles:
            UTN_messenger('Opción inválida', 'Error')
            continue

        elif eleccion.lower() == 'dni':
            dni_ingresado = input("Ingrese el DNI del paciente: ")
            coincidencia_dni = list(filter(lambda paciente: paciente.get_dni() == dni_ingresado, lista_pacientes))

            if not coincidencia_dni:
                UTN_messenger('El DNI ingresado no se encuentra en el sistema', 'Error')
            else:
                UTN_messenger('DNI encontrado', 'Success')
                paciente = coincidencia_dni[0]
                break

        else:
            id_ingresado = input("Ingrese el ID del paciente: ")
            coincidencia_id = list(filter(lambda paciente: str(paciente.get_id()) == id_ingresado, lista_pacientes))

            if not coincidencia_id:
                UTN_messenger('El ID ingresado no se encuentra en el sistema', 'Error')
            else:
                UTN_messenger('ID encontrado', 'Success')
                paciente = coincidencia_id[0]
                break
            
    return paciente
