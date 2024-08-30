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

class Paciente:
    def __init__(self, paciente_dicc : dict):
        self.__id = paciente_dicc.get('id')
        self.__nombre = paciente_dicc.get('nombre')
        self.__apellido = paciente_dicc.get('apellido')
        self.__dni = paciente_dicc.get('dni')
        self.__edad = paciente_dicc.get('edad')
        self.__fecha_de_registro = paciente_dicc.get('fecha_de_registro')
        self.__obra_social = paciente_dicc.get('obra_social')

    def get_dni(self):
        return self.__dni
    
    def get_id(self):
        return self.__id
    
    def get_obra_social(self):
        return self.__obra_social
    
    def get_edad(self):
        return self.__edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def pasar_a_dict(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'dni': self.__dni,
            'edad': self.__edad,
            'fecha_de_registro': self.__fecha_de_registro,
            'obra_social': self.__obra_social
        }
    