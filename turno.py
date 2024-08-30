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

class Turno:
    def __init__(self, id, id_paciente, especialidad, monto_a_pagar, estado_del_turno):
        self.__id = id
        self.__id_paciente = id_paciente
        self.__especialidad = especialidad
        self.__monto_a_pagar = monto_a_pagar
        self.__estado_del_turno = estado_del_turno

    def get_id(self):
        return self.__id

    def get_monto_a_pagar(self):
        return self.__monto_a_pagar
    
    def get_especialidad(self):
        return self.__especialidad
    
    def get_id_paciente(self):
        return self.__id_paciente
    
    def get_estado_del_turno(self):
        return self.__estado_del_turno
    
    def set_estado_del_turno(self, estado):
        self.__estado_del_turno = estado

    def pasar_a_dict(self):
        return {
            'id': self.__id,
            'id_paciente': self.__id_paciente,
            'especialidad': self.__especialidad,
            'monto_a_pagar': self.__monto_a_pagar,
            'estado_del_turno': self.__estado_del_turno
        }
