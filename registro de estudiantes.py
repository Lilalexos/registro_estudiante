class Estudiante:
    def __init__(self, tipo_documento, numero_documento, nombres):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.nombres = nombres

    def __str__(self):
        return f"{self.nombres} (Tipo: {self.tipo_documento}, Documento: {self.numero_documento})"

    def mostrar_informacion(self):
        print(f"Tipo de Documento: {self.tipo_documento}")
        print(f"Número de Documento: {self.numero_documento}")
        print(f"Nombres del Estudiante: {self.nombres}")


class Curso:
    def __init__(self, codigo_curso, nombre_curso):
        self.codigo_curso = codigo_curso
        self.nombre_curso = nombre_curso

    def __str__(self):
        return f"Código: {self.codigo_curso}, Nombre: {self.nombre_curso}"

    def mostrar_informacion(self):
        print(f"Código del curso: {self.codigo_curso}")
        print(f"Nombre del curso: {self.nombre_curso}")


class Sesion:
    def __init__(self, codigo_curso, hora_inicio, hora_final, fecha):
        self.codigo_curso = codigo_curso
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha

    def __str__(self):
        return f"Curso: {self.codigo_curso}, Fecha: {self.fecha}, Horario: {self.hora_inicio} - {self.hora_final}"

    def mostrar_informacion(self):
        print(f"Código del Curso: {self.codigo_curso}")
        print(f"Hora de Inicio: {self.hora_inicio}")
        print(f"Hora Final: {self.hora_final}")
        print(f"Fecha: {self.fecha}")


class Asistencia:
    ESTADOS = {0: 'Llegó a tiempo', 1: 'Llegó tarde', 2: 'No llegó'}

    def __init__(self, codigo_sesion, documento_estudiante, estado_asistencia):
        self.codigo_sesion = codigo_sesion
        self.documento_estudiante = documento_estudiante
        self.estado_asistencia = estado_asistencia

    def __str__(self):
        return f"Sesión: {self.codigo_sesion}, Documento: {self.documento_estudiante}, Estado: {self.ESTADOS[self.estado_asistencia]}"

    def mostrar_informacion(self):
        print(f"Código de la Sesión: {self.codigo_sesion}")
        print(f"Documento del Estudiante: {self.documento_estudiante}")
        print(f"Estado de Asistencia: {self.ESTADOS[self.estado_asistencia]}")


class Sistema:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []
        self.sesiones = []
        self.asistencias = []

    def agregar_estudiante(self):
        tipo_documento = input("Ingresa el tipo de documento: ")
        numero_documento = input("Ingresa el número de documento: ")
        nombres = input("Ingresa los nombres del estudiante: ")
        estudiante = Estudiante(tipo_documento, numero_documento, nombres)
        self.estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.")

    def agregar_curso(self):
        codigo_curso = input("Ingresa el código del curso: ")
        nombre_curso = input("Ingresa el nombre del curso: ")
        curso = Curso(codigo_curso, nombre_curso)
        self.cursos.append(curso)
        print("Curso agregado correctamente.")

    def agregar_sesion(self):
        codigo_curso = input("Ingresa el código del curso: ")
        hora_inicio = input("Ingresa la hora de inicio (HH:MM): ")
        hora_final = input("Ingresa la hora final (HH:MM): ")
        fecha = input("Ingresa la fecha (DD/MM/AAAA): ")
        sesion = Sesion(codigo_curso, hora_inicio, hora_final, fecha)
        self.sesiones.append(sesion)
        print("Sesión agregada correctamente.")

    def agregar_asistencia(self):
        codigo_sesion = input("Ingresa el código de la sesión: ")
        documento_estudiante = input("Ingresa el número de documento del estudiante: ")
        estado = int(input("Estado de asistencia (0: Llegó a tiempo, 1: Llegó tarde, 2: No llegó): "))
        asistencia = Asistencia(codigo_sesion, documento_estudiante, estado)
        self.asistencias.append(asistencia)
        print("Asistencia registrada correctamente.")

    def buscar_estudiante(self, documento):
        for estudiante in self.estudiantes:
            if estudiante.numero_documento == documento:
                return estudiante
        return None

    def listar_estudiantes(self):
        print("Lista de estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante)

    def listar_cursos(self):
        print("Lista de cursos:")
        for curso in self.cursos:
            print(curso)

    def listar_sesiones(self):
        print("Lista de sesiones:")
        for sesion in self.sesiones:
            print(sesion)

    def listar_asistencias(self):
        print("Lista de asistencias:")
        for asistencia in self.asistencias:
            print(asistencia)

    def estudiantes_tarde_en_sesion(self):
        fecha = input("Ingresa la fecha de la sesión (DD/MM/AAAA): ")
        codigo_curso = input("Ingresa el código del curso: ")
        
        print(f"Estudiantes que llegaron tarde en la sesión del curso {codigo_curso} el {fecha}:")
        for sesion in self.sesiones:
            if sesion.codigo_curso == codigo_curso and sesion.fecha == fecha:
                for asistencia in self.asistencias:
                    if asistencia.codigo_sesion == codigo_curso and asistencia.estado_asistencia == 1:
                        estudiante = self.buscar_estudiante(asistencia.documento_estudiante)
                        if estudiante:
                            print(estudiante)

    def contar_tardanzas_por_estudiante(self):
        documento_estudiante = input("Ingresa el número de documento del estudiante: ")
        codigo_curso = input("Ingresa el código del curso: ")
        fecha_inicio = input("Ingresa la fecha de inicio (DD/MM/AAAA): ")
        fecha_fin = input("Ingresa la fecha de fin (DD/MM/AAAA): ")

        contador = 0
        for sesion in self.sesiones:
            if sesion.codigo_curso == codigo_curso and fecha_inicio <= sesion.fecha <= fecha_fin:
                for asistencia in self.asistencias:
                    if (asistencia.codigo_sesion == sesion.codigo_curso and
                        asistencia.documento_estudiante == documento_estudiante and
                        asistencia.estado_asistencia == 1):
                        contador += 1

        print(f"El estudiante con documento {documento_estudiante} llegó tarde {contador} veces en el curso {codigo_curso} entre {fecha_inicio} y {fecha_fin}.")

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar estudiante")
    print("2. Agregar curso")
    print("3. Agregar sesión")
    print("4. Registrar asistencia")
    print("5. Listar estudiantes")
    print("6. Listar cursos")
    print("7. Listar sesiones")
    print("8. Listar asistencias")
    print("9. Estudiantes que llegaron tarde en una sesión")
    print("10. Contar tardanzas por estudiante")
    print("11. Salir")

def main():
    sistema = Sistema()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sistema.agregar_estudiante()
        elif opcion == '2':
            sistema.agregar_curso()
        elif opcion == '3':
            sistema.agregar_sesion()
        elif opcion == '4':
            sistema.agregar_asistencia()
        elif opcion == '5':
            sistema.listar_estudiantes()
        elif opcion == '6':
            sistema.listar_cursos()
        elif opcion == '7':
            sistema.listar_sesiones()
        elif opcion == '8':
            sistema.listar_asistencias()
        elif opcion == '9':
            sistema.estudiantes_tarde_en_sesion()
        elif opcion == '10':
            sistema.contar_tardanzas_por_estudiante()
        elif opcion == '11':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
