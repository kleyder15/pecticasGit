# info-proyecto.py
# Completa este archivo con los datos reales de tu proyecto
# Ejecutalo con: python info-proyecto.py

# ── DATOS DEL PROYECTO ──────────────────────────────────────
nombre_proyecto = "Doc-Smart"        # escribe el nombre de tu proyecto
descripcion = "Facilita la comunicación entre Paciente y Médico, Además permite agendar citas medicas y resolver dudas mediante un ChatBot"            # que problema resuelve
tecnologias = ["React", "Django", "MySql"]            # ["React", "Django", "MySQL"]
integrantes = ["Pablo Alvarez Montoya", "Miguel Angel Racero", "Kleider Yesid Echeverrry"]            # ["Nombre1", "Nombre2", "Nombre3"]
funcionalidades = [         # lista las funcionalidades principales
    "Agendamiento y gestión de citas médicas",
    "Historial clínico digital",
    "Registro y administración de médicos",
    "Asistente médico con inteligencia artificial",
    "Búsqueda rápida de pacientes y citas",
    "Gestión de diagnósticos y tratamientos",
    "Panel administrativo",
    "Inicio de sesión seguro",
    "Visualización organizada de información médica"
    "Asistente con funcionalidades "
]
estado = "En Construcción"                 # "En construccion", "Beta", "Terminado"

# ── TAREAS DEL EQUIPO ────────────────────────────────────────
tareas_completadas = [
    "Diseno de base de datos",
    "Prototipo de interfaz",
    "Frontend del inicio",
    "Frontend y backend del login y del registro",
    "Proteccion de rutas de paciente y de doctor",
    "Validaciones",
    "Metodos crud de todas las tablas",
    "Obtener datos mediante token",
]
tareas_pendientes = [
    "Pagina principal del medico,paciente,administrador",
    "Seccion para agendar citas",
    "Añadir rol de administrador",
    "Backend y frontend del chat bot, y chat entre paciente y medico",
    "Dashboard medico y administrador"
]
tareas_en_progreso = [
    "Pagina principal del medico,paciente,administrador",  
]

# ── FUNCIONES ────────────────────────────────────────────────
def mostrar_info():
    print("=" * 45)
    print(f"  PROYECTO: {nombre_proyecto}")
    print("=" * 45)
    print(f"  Descripcion : {descripcion}")
    print(f"  Estado      : {estado}")
    print(f"  Tecnologias : {', '.join(tecnologias)}")
    print(f"  Integrantes : {', '.join(integrantes)}")

def mostrar_funcionalidades():
    print("\n  FUNCIONALIDADES:")
    for i, f in enumerate(funcionalidades, 1):
        print(f"    {i}. {f}")

def mostrar_tareas():
    print("\n  TAREAS COMPLETADAS:")
    for t in tareas_completadas:
        print(f"    [x] {t}")
    print("\n  EN PROGRESO:")
    for t in tareas_en_progreso:
        print(f"    [~] {t}")
    print("\n  PENDIENTES:")
    for t in tareas_pendientes:
        print(f"    [ ] {t}")
    total = len(tareas_completadas) + len(tareas_pendientes) + len(tareas_en_progreso)
    print(f"\n  Total tareas: {total} | Completadas: {len(tareas_completadas)}")

# ── EJECUTAR ─────────────────────────────────────────────────
mostrar_info()
mostrar_funcionalidades()
mostrar_tareas()
print("\n" + "=" * 45)