# datos/repositorio.py

import sqlite3
from dominio.consulta import Consulta
from dominio.paciente import Paciente
from dominio.medico import Medico

class Repositorio:
    def __init__(self, db_name='clinica.db'):
        self.conn = sqlite3.connect(db_name)
        self.crear_tablas()

    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            historial TEXT,
            seguro INTEGER
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            especialidad TEXT,
            tarifa_hora REAL
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            motivo TEXT,
            horas REAL,
            paciente_id INTEGER,
            medico_id INTEGER,
            costo REAL,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY (medico_id) REFERENCES medicos(id)
        )""")
        self.conn.commit()

    # CRUD para Pacientes
    def agregar_paciente(self, paciente: Paciente):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO pacientes (nombre, edad, historial, seguro) VALUES (?, ?, ?, ?)",
                       (paciente.nombre, paciente.edad, paciente.obtener_historial(), int(paciente.tiene_seguro)))
        self.conn.commit()
        return cursor.lastrowid

    def agregar_medico(self, medico: Medico):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO medicos (nombre, edad, especialidad, tarifa_hora) VALUES (?, ?, ?, ?)",
                       (medico.nombre, medico.edad, medico.especialidad, medico.get_tarifa_hora()))
        self.conn.commit()
        return cursor.lastrowid

    def registrar_consulta(self, consulta: Consulta, paciente_id: int, medico_id: int):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO consultas (fecha, motivo, horas, paciente_id, medico_id, costo)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            consulta.fecha.strftime("%Y-%m-%d"),
            consulta.motivo,
            consulta.horas,
            paciente_id,
            medico_id,
            consulta.costo
        ))
        self.conn.commit()

    def obtener_consultas_por_medico_y_fecha(self, medico_nombre, fecha_inicio, fecha_fin):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT c.fecha, c.motivo, c.horas, c.costo, p.nombre 
        FROM consultas c
        JOIN medicos m ON c.medico_id = m.id
        JOIN pacientes p ON c.paciente_id = p.id
        WHERE m.nombre = ? AND date(c.fecha) BETWEEN ? AND ?
        """, (medico_nombre, fecha_inicio, fecha_fin))
        return cursor.fetchall()
