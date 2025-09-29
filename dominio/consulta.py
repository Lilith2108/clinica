# dominio/consulta.py

from datetime import datetime

class Consulta:
    def __init__(self, fecha: str, motivo: str, horas: float, paciente, medico):
        self.fecha = self.validar_fecha(fecha)
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0.")
        self.horas = horas
        self.motivo = motivo
        self.paciente = paciente
        self.medico = medico
        self.costo = self.calcular_costo()

    def calcular_costo(self):
        tarifa = self.medico.get_tarifa_hora()
        base = self.horas * tarifa
        if self.paciente.tiene_seguro:
            return base * 0.8  # 20% descuento
        return base

    def validar_fecha(self, fecha: str):
        try:
            return datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use AAAA-MM-DD.")
