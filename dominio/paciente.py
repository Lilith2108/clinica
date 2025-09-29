# dominio/paciente.py

from dominio.persona import Persona

class Paciente(Persona):
    def __init__(self, nombre: str, edad: int, historial: str, tiene_seguro: bool):
        super().__init__(nombre, edad)
        self.__historial = historial  # Encapsulado
        self.tiene_seguro = tiene_seguro

    def obtener_historial(self):
        return self.__historial

def actualizar_historial(self, nuevo_historial: str):
    if nuevo_historial != '':
        self.__historial = nuevo_historial

