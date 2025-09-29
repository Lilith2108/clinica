# app.py

from dominio.paciente import Paciente
from dominio.medico import Medico
from dominio.consulta import Consulta
from datos.repositorio import Repositorio
import sqlite3

if __name__ == "__main__":
    print(" Iniciando aplicación clínica...\n")

    repo = Repositorio()

    # Crear paciente y médico
    paciente = Paciente("Juan Pérez", 30, "Historial limpio", True)
    medico = Medico("Dra. López", 45, "Cardiología", 40000)

    id_paciente = repo.agregar_paciente(paciente)
    id_medico = repo.agregar_medico(medico)

    print(f" Paciente creado (ID: {id_paciente}): {paciente.nombre}")
    print(f" Médico creado (ID: {id_medico}): {medico.nombre}")

    # Crear consulta
    consulta = Consulta("2025-09-15", "Chequeo general", 1.5, paciente, medico)
    repo.registrar_consulta(consulta, id_paciente, id_medico)

    print(f" Consulta registrada para {paciente.nombre} con {medico.nombre}. Costo: ${consulta.costo:,.0f}")

    # Mostrar consultas del médico en el mes
    consultas = repo.obtener_consultas_por_medico_y_fecha("Dra. López", "2025-09-01", "2025-09-30")
    print("\n Consultas encontradas entre 2025-09-01 y 2025-09-30:")

    if not consultas:
        print(" No se encontraron consultas para ese médico en ese rango de fechas.")
    else:
        for c in consultas:
            print(f" Fecha: {c[0]}, Motivo: {c[1]}, Horas: {c[2]}, "
                  f"Costo: ${c[3]:,.0f}, Paciente: {c[4]}")

    # --- Debug temporal: mostrar datos en la BD ---
    print("\n DEBUG: Contenido actual de la base de datos (clinica.db):")

    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()

    print("\n Tabla: pacientes")
    cursor.execute("SELECT * FROM pacientes")
    for row in cursor.fetchall():
        print(row)

    print("\n Tabla: medicos")
    cursor.execute("SELECT * FROM medicos")
    for row in cursor.fetchall():
        print(row)

    print("\n Tabla: consultas")
    cursor.execute("SELECT * FROM consultas")
    for row in cursor.fetchall():
        print(row)

    conn.close()
