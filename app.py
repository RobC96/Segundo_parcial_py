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

import library_utn as utn
import re


def main_app():
    """
    Aplicacion principal del Segundo Parcial de Laboratorio 1
    """

    clinica = utn.cargar_clinica()
    
    while True:

        menu =\
            """
            1  - Alta paciente.
            2  - Alta turno.
            3  - Ordenar turnos.
            4  - Mostrar pacientes en espera.
            5  - Atender pacientes.
            6  - Cobrar atenciones.
            7  - Cerrar caja.
            8  - Mostrar informe.
            9  - Salir.
            """

        opcion = 0
        selected_option = input(f'{menu}Su opcion: ')
        if re.match('^[0-9]', selected_option):
            opcion = int(selected_option)
        
        match opcion:
            case 1: # Alta paciente
                utn.alta_paciente(clinica)
            case 2: # Alta turno
                utn.alta_turno(clinica)
            case 3: # Ordenar turnos
                utn.ordenar_turnos(clinica)
            case 4: # Mostrar pacientes en espera
                clinica.mostrar_pacientes_en_espera()
            case 5: # Atender pacientes
                clinica.atender_pacientes()
            case 6: # Cobrar atenciones
                clinica.cobrar_atenciones()
            case 7: # Cerrar caja
                clinica.cerrar_caja()
            case 8: # Mostrar informe
                clinica.obra_social_menos_ingresos()
            case 9: # Salir
                break
            case _:
                utn.UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        utn.clear_console()
            