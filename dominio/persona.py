# dominio/persona.py

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        if self.edad < 18:
            raise ValueError("La persona debe ser mayor de edad.")
