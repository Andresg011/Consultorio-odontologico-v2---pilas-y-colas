from datetime import datetime
from collections import deque

class Consultorio:
    def __init__(self):
        self.citas = []
        self.cola_agenda = deque()

    def agendar_cita(self, cita):
        self.citas.append(cita)

    def filtrar_extracciones_urgentes(self):
        urgentes = []
        for cita in self.citas:
            if cita.tipo_atencion == "extraccion" and cita.prioridad == "urgente":
                urgentes.append(cita)
        return urgentes

    def ordenar_por_fecha(self, lista):
        lista_ordenada = list(lista)
        n = len(lista_ordenada)

        for i in range(n): 
            for j in range(0, n - i - 1):
                fecha_actual = datetime.strptime(lista_ordenada[j].fecha_cita, "%d/%m/%Y")
                fecha_siguiente = datetime.strptime(lista_ordenada[j + 1].fecha_cita, "%d/%m/%Y")

                if fecha_actual > fecha_siguiente:
                    temporal = lista_ordenada[j]
                    lista_ordenada[j] = lista_ordenada[j +1]
                    lista_ordenada[j + 1] = temporal

        return lista_ordenada 

    def generar_informe(self, lista):
        print("Informe de extracciones urgentes")
        total = 0

        for cita in lista:
            total = total + 1
            print(f"Cliente por llamar: {cita.nombre}, fecha de la cita: {cita.fecha_cita}")

        print(f"Total de clientes por llamar: {total}")

    def agregar_a_agenda(self, cita):
        self.cola_agenda.append(cita)

    def atender_siguiente_cita(self):
        if self.cola_agenda:
            cita = self.cola_agenda.popleft()
            self.citas.remove(cita)
            print(f"Atendiendo a: {cita.nombre}, atención: {cita.tipo_atencion}")
        else:
            print("No hay clientes en la agenda.")

    def consultar_agenda(self):
        total = 0
        for cita in self.cola_agenda:
            total = total + 1
            print(f"En agenda: {cita.nombre}, atención: {cita.tipo_atencion}, fecha: {cita.fecha_cita}")
        print(f"Total de clientes en agenda: {total}")

    def ordenar_por_prioridad_y_fecha(self, lista):
        lista_ordenada = list(lista)
        n = len(lista_ordenada)

        for i in range(n):
            for j in range(0, n - i - 1):
                actual = lista_ordenada[j]
                siguiente = lista_ordenada[j + 1]
                fecha_actual = datetime.strptime(actual.fecha_cita, "%d/%m/%Y")
                fecha_siguiente = datetime.strptime(siguiente.fecha_cita, "%d/%m/%Y")

                if (actual.prioridad == "normal" and siguiente.prioridad == "urgente") or (actual.prioridad == siguiente.prioridad and fecha_actual > fecha_siguiente):
                    temporal = lista_ordenada[j]
                    lista_ordenada[j] = lista_ordenada[j + 1]
                    lista_ordenada[j + 1] = temporal

        return lista_ordenada

    def generar_agenda(self):
        self.cola_agenda.clear()
        citas_ordenadas = self.ordenar_por_prioridad_y_fecha(self.citas)
        for cita in citas_ordenadas:
            self.agregar_a_agenda(cita)
        print("Agenda del dia generada correctamente")