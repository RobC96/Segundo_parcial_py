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
import json

class Clinica:
    def __init__(self, razon_social, lista_pacientes, lista_turnos, especialidades, obras_sociales_validas, recaudacion, hay_pacientes_sin_atencion):
        self.__razon_social = razon_social
        self.__lista_pacientes = lista_pacientes
        self.__lista_turnos = lista_turnos
        self.__especialidades = especialidades
        self.__obras_sociales_validas = obras_sociales_validas
        self.__recaudacion = recaudacion
        self.__hay_pacientes_sin_atencion = hay_pacientes_sin_atencion

    def get_lista_pacientes(self):
        return self.__lista_pacientes

    def get_especialidades(self):
        return self.__especialidades
    
    def get_lista_turnos(self):
        return self.__lista_turnos

    def mostrar_pacientes_en_espera(self):
        pacientes_en_espera = []

        for turno in self.__lista_turnos:
            if turno.get_estado_del_turno() == "Activo":
                paciente = next((p for p in self.__lista_pacientes if p.get_id() == turno.get_id_paciente()), None)
                if paciente:
                    pacientes_en_espera.append(paciente)

        if pacientes_en_espera:
            print("Pacientes en espera:")
            for paciente in pacientes_en_espera:
                print(f"ID: {paciente.get_id()}, Nombre: {paciente.get_nombre()}, Apellido: {paciente.get_apellido()}")
        else:
            print("No hay pacientes en espera.")

    def atender_pacientes(self):
        pacientes_atendidos = 0

        for turno in self.__lista_turnos:
            if turno.get_estado_del_turno() == "Activo":
                turno.set_estado_del_turno("Finalizado")
                pacientes_atendidos += 1
                
                paciente = next((paciente for paciente in self.__lista_pacientes if paciente.get_id() == turno.get_id_paciente()), None)
                if paciente:
                    print(f"Paciente atendido: {paciente.get_nombre()} {paciente.get_apellido()}")

                if pacientes_atendidos >= 2:
                    break
        
        if pacientes_atendidos == 0:
            print("No hay pacientes en espera.")

    def cobrar_atenciones(self):
        total_recaudado = 0

        for turno in self.__lista_turnos:
            if turno.get_estado_del_turno() == "Finalizado":
                paciente = next((paciente for paciente in self.__lista_pacientes if paciente.get_id() == turno.get_id_paciente()), None)
                if paciente:
                    monto_a_pagar = turno.get_monto_a_pagar()

                    turno.set_estado_del_turno("Pagado")

                    self.__recaudacion += monto_a_pagar

                    total_recaudado += monto_a_pagar

        if total_recaudado > 0:
            print(f"Se ha recaudado un total de ${total_recaudado}")
        else:
            print("No hay turnos finalizados para cobrar.")

    def cerrar_caja(self):
        pacientes_por_atender = any(turno.get_estado_del_turno() in ["Activo", "Finalizado"] for turno in self.__lista_turnos)
        
        if pacientes_por_atender:
            print("Aún hay pacientes por atender.")
        else:
            pacientes_dict_list = [paciente.pasar_a_dict() for paciente in self.__lista_pacientes]
            turnos_dict_list = [turno.pasar_a_dict() for turno in self.__lista_turnos]
            
            # Cargar el JSON existente
            with open('configs.json', 'r', encoding='utf-8') as file:
                datos = json.load(file)
            
            # Actualizar lista de pacientes y turnos en el JSON
            datos['lista_pacientes'] = pacientes_dict_list
            datos['lista_turnos'] = turnos_dict_list
            
            # Sobreescribir el JSON
            with open('configs.json', 'w', encoding='utf-8') as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
            
            # Mostrar total recaudado
            print(f"Se ha recaudado un total de ${self.__recaudacion}")

    def obra_social_menos_ingresos(self):
        ingresos_por_obra_social = {
            "Swiss Medical": 0,
            "Apres": 0,
            "PAMI": 0,
            "Particular": 0
        }

        # Acumular los montos pagados por cada obra social
        for turno in self.__lista_turnos:
            if turno.get_estado_del_turno() == "Pagado":
                paciente = next((paciente for paciente in self.__lista_pacientes if paciente.get_id() == turno.get_id_paciente()), None)
                if paciente:
                    obra_social = paciente.get_obra_social()
                    monto_a_pagar = turno.get_monto_a_pagar()
                    ingresos_por_obra_social[obra_social] += monto_a_pagar
        
        # Encontrar la obra social con menos ingresos
        obra_social_menos_ingresos = min(ingresos_por_obra_social, key=ingresos_por_obra_social.get)

        # Mostrar resultado
        print(f"La obra social con menos ingresos es: {obra_social_menos_ingresos}")
