from datetime import datetime

class Cita:
    def __init__(self, nombre, tipo_atencion, prioridad, fecha_cita):
        self.nombre = nombre
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        valor = valor.strip()
        if valor == "" or not valor.replace(" ", ""). isalpha():
            raise ValueError("el nombre solo puede tener letras y no estar vacio")
        self._nombre = valor.title()

    @property
    def tipo_atencion(self):
        return self._tipo_atencion

    @tipo_atencion.setter
    def tipo_atencion(self, valor):
        valor = valor.strip().lower()
        opciones_validas = ["limpieza", "diagnostico", "calzas", "extraccion"]
        if valor not in opciones_validas:
            raise ValueError("el tipo de atencion debe ser limpieza, diagnostico, calzas o extraccion")
        self._tipo_atencion = valor

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        valor = valor.strip().lower()
        opciones_validas = ["normal", "urgente"]
        if valor not in opciones_validas:
            raise ValueError("la prioridad debe ser normal o urgente")
        self._prioridad = valor

    @property
    def fecha_cita(self):
        return self._fecha_cita

    @fecha_cita.setter
    def fecha_cita(self, valor):
        valor = valor.strip()
        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError ("la fecha debe tener formato dd/mm/aaaa y ser una fecha valida")
        self._fecha_cita = valor
    


