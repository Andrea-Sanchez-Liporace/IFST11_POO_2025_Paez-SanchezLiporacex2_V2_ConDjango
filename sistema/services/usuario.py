# Importo el modelo del usuarioAdoptante para usarlo en sus funciones.
from sistema.models.usuario_adoptante import UsuarioAdoptante

# Función para registrar un nuevo usuario adoptante
def registrar_usuario(datos_usuario):
    return UsuarioAdoptante.objects.create(**datos_usuario)

# Función para buscar un usuario por su DNI
def buscar_usuario_por_dni(dni):
    try:
        return UsuarioAdoptante.objects.get(dni=dni)
    except UsuarioAdoptante.DoesNotExist:
        return f"El usuario no existe en el sistema"

# Función para mostrar todos los usuarios adoptantes registrados
def mostrar_usuarios():
    return UsuarioAdoptante.objects.all()