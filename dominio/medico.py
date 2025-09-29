# dominio/medico.py

from dominio.persona import Persona

class Medico(Persona):
    def __init__(self, nombre: str, edad: int, especialidad: str, tarifa_hora: float):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.__tarifa_hora = None
        self.set_tarifa_hora(tarifa_hora)

    def get_tarifa_hora(self):
        return self.__tarifa_hora

    def set_tarifa_hora(self, tarifa: float):
        if tarifa <= 0:
            raise ValueError("La tarifa por hora debe ser mayor a 0.")
        self.__tarifa_hora = tarifa
