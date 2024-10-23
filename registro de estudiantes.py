class Estudiante:
    def __init__(self, numero_estudiante, tipo, numero_documento, nombres):
        self.numero_estudiante = numero_estudiante
        self.tipo = tipo
        self.numero_documento = numero_documento
        self.nombres = nombres

    def __str__(self):
        return f"Número de estudiante: {self.numero_estudiante}, Nombre: {self.nombres}"


class Curso:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}"


class Sesion:
    def __init__(self, codigo_curso, hora_inicio, hora_final, fecha):
        self.codigo_curso = codigo_curso
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha

    def __str__(self):
        return f"Curso: {self.codigo_curso}, Fecha: {self.fecha}, Horario: {self.hora_inicio} - {self.hora_final}"


class Asistencia:
    ESTADOS = {0: 'No llegó', 1: 'Llegó', 2: 'Llegó tarde'}

    def __init__(self, codigo_sesion, numero_estudiante, estado=2):
        self.codigo_sesion = codigo_sesion
        self.numero_estudiante = numero_estudiante
        self.estado = estado

    def __str__(self):
        return f"Sesión: {self.codigo_sesion}, Estudiante: {self.numero_estudiante}, Estado: {Asistencia.ESTADOS.get(self.estado)}"


class Sistema:
    def __init__(self):
        self.estudiantes = []  # Arreglo de estudiantes
        self.cursos = []  # Arreglo de cursos
        self.sesiones = []  # Arreglo de sesiones
        self.asistencias = []  # Arreglo de asistencias

    def agregar_estudiante(self):
        numero_estudiante = input("Número de estudiante: ")
        tipo = input("Tipo (ej. cc, ti): ")
        numero_documento = input("Número de documento: ")
        nombres = input("Nombres del estudiante: ")
        nuevo_estudiante = Estudiante(numero_estudiante, tipo, numero_documento, nombres)
        self.estudiantes.append(nuevo_estudiante)  # Añadiendo al arreglo
        print("Estudiante agregado.")

    def agregar_curso(self):
        codigo = input("Código del curso: ")
        nombre = input("Nombre del curso: ")
        nuevo_curso = Curso(codigo, nombre)
        self.cursos.append(nuevo_curso)  # Añadiendo al arreglo
        print("Curso agregado.")

    def agregar_sesion(self):
        codigo_curso = input("Código del curso: ")
        hora_inicio = input("Hora de inicio (hh:mm): ")
        hora_final = input("Hora final (hh:mm): ")
        fecha = input("Fecha (dd/mm/aaaa): ")
        nueva_sesion = Sesion(codigo_curso, hora_inicio, hora_final, fecha)
        self.sesiones.append(nueva_sesion)  # Añadiendo al arreglo
        print("Sesión agregada.")

    def agregar_asistencia(self):
        codigo_sesion = input("Código de la sesión: ")
        numero_estudiante = input("Número del estudiante: ")
        estado = input("Estado (0: no llegó, 1: llegó, 2: llegó tarde): ")
        estado = int(estado) if estado.isdigit() and int(estado) in [0, 1, 2] else 2
        nueva_asistencia = Asistencia(codigo_sesion, numero_estudiante, estado)
        self.asistencias.append(nueva_asistencia)  # Añadiendo al arreglo
        print("Asistencia registrada.")

    def buscar_estudiante(self, numero):
        for est in self.estudiantes:
            if est.numero_estudiante == numero:
                return est
        return None

    def buscar_curso(self, codigo):
        for cur in self.cursos:
            if cur.codigo == codigo:
                return cur
        return None

    def buscar_sesion(self, codigo_curso):
        for ses in self.sesiones:
            if ses.codigo_curso == codigo_curso:
                return ses
        return None

    def buscar_asistencia(self, codigo_sesion, numero_estudiante):
        for asis in self.asistencias:
            if asis.codigo_sesion == codigo_sesion and asis.numero_estudiante == numero_estudiante:
                return asis
        return None

    def listar_estudiante(self):
        numero = input("Ingrese el número del estudiante: ")
        estudiante = self.buscar_estudiante(numero)
        if estudiante:
            print(estudiante)
        else:
            print("Estudiante no encontrado.")

    def listar_curso(self):
        codigo = input("Ingrese el código del curso: ")
        curso = self.buscar_curso(codigo)
        if curso:
            print(curso)
        else:
            print("Curso no encontrado.")

    def listar_sesion(self):
        codigo = input("Ingrese el código del curso: ")
        sesion = self.buscar_sesion(codigo)
        if sesion:
            print(sesion)
        else:
            print("Sesión no encontrada.")

    def listar_asistencia(self):
        codigo_sesion = input("Código de la sesión: ")
        numero_estudiante = input("Número del estudiante: ")
        asistencia = self.buscar_asistencia(codigo_sesion, numero_estudiante)
        if asistencia:
            print(asistencia)
        else:
            print("Asistencia no encontrada.")

    def saber_llegaron_tarde_sesion(self):
        codigo_sesion = input("Ingrese el código de la sesión: ")
        for asis in self.asistencias:
            if asis.codigo_sesion == codigo_sesion and asis.estado == 2:  # Llegó tarde
                print(f"Estudiante: {asis.numero_estudiante} llegó tarde en la sesión {asis.codigo_sesion}.")

    def saber_llegaron_tarde_rango(self):
        codigo_curso = input("Ingrese el código del curso: ")
        fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
        fecha_final = input("Ingrese la fecha final (dd/mm/aaaa): ")
        llegadas_tarde = {}

        for sesion in self.sesiones:
            if sesion.codigo_curso == codigo_curso and fecha_inicio <= sesion.fecha <= fecha_final:
                for asis in self.asistencias:
                    if asis.codigo_sesion == sesion.codigo_curso and asis.estado == 2:
                        if asis.numero_estudiante in llegadas_tarde:
                            llegadas_tarde[asis.numero_estudiante] += 1
                        else:
                            llegadas_tarde[asis.numero_estudiante] = 1

        if llegadas_tarde:
            for estudiante, veces in llegadas_tarde.items():
                print(f"Estudiante {estudiante} llegó tarde {veces} veces entre {fecha_inicio} y {fecha_final}.")
        else:
            print("No hay estudiantes que hayan llegado tarde en el rango de fechas.")

def main():
    sistema_obj = Sistema()
    while True:
        print("- Menú Principal -")
        print("\n1.  Agregar estudiante")
        print("2.  Agregar curso")
        print("3.  Agregar sesión")
        print("4.  Registrar asistencia")
        print("5.  Buscar datos de un estudiante")
        print("6.  Buscar datos de un curso")
        print("7.  Buscar datos de una sesión")
        print("8.  Buscar datos de una asistencia")
        print("9.  Consultar estudiantes que llegaron tarde")
        print("10. Consultar veces de llegadas tardías de un estudiante")
        print("11. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sistema_obj.agregar_estudiante()
        elif opcion == '2':
            sistema_obj.agregar_curso()
        elif opcion == '3':
            sistema_obj.agregar_sesion()
        elif opcion == '4':
            sistema_obj.agregar_asistencia()
        elif opcion == '5':
            sistema_obj.listar_estudiante()
        elif opcion == '6':
            sistema_obj.listar_curso()
        elif opcion == '7':
            sistema_obj.listar_sesion()
        elif opcion == '8':
            sistema_obj.listar_asistencia()
        elif opcion == '9':
            sistema_obj.saber_llegaron_tarde_sesion()
        elif opcion == '10':
            sistema_obj.saber_llegaron_tarde_rango()
        elif opcion == '11':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
