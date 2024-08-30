'''
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
        # Verificar si hay pacientes por atender
        pacientes_por_atender = any(turno.get_estado_del_turno() in ["Activo", "Finalizado"] for turno in self.__lista_turnos)
        
        if pacientes_por_atender:
            print("Aún hay pacientes por atender.")
        else:
            # Actualizar archivos de pacientes y turnos
            pacientes_dict_list = [paciente.__dict__ for paciente in self.__lista_pacientes]
            turnos_dict_list = [turno.__dict__ for turno in self.__lista_turnos]
            
            with open('pacientes.json', 'w') as file:
                json.dump(pacientes_dict_list, file, indent=4)
            
            with open('turnos.json', 'w') as file:
                json.dump(turnos_dict_list, file, indent=4)
            
            # Mostrar total recaudado
            print(f"Se ha recaudado un total de ${self.__recaudacion}")


class Turno:
    def __init__(self, id, id_paciente, especialidad, monto_a_pagar, estado_del_turno):
        self.__id = id
        self.__id_paciente = id_paciente
        self.__especialidad = especialidad
        self.__monto_a_pagar = monto_a_pagar
        self.__estado_del_turno = estado_del_turno

    def get_monto_a_pagar(self):
        return self.__monto_a_pagar
    
    def get_id_paciente(self):
        return self.__id_paciente
'''