# Importo los modelos (Perro / usuarioAdoptante) para usarlos en las funciones relacionadas a un proceso de adopción.
from sistema.models.usuario_adoptante import UsuarioAdoptante
from sistema.models.perro import Perro

# Función para reservar un perro para un usuario adoptante
def reservar_perro(dni_usuario, id_perro):
    try:
        usuario = UsuarioAdoptante.objects.get(dni=dni_usuario)
        perro = Perro.objects.get(id=id_perro)
        if perro.estado != "disponible":
            return f"El perro '{perro.nombre}' no está disponible, ya fue '{perro.estado}'"
        perro.estado = "reservado"
        perro.save()
        return f"{usuario.nombre} {usuario.apellido}, te reservamos a '{perro.nombre}' exitosamente."
    except (UsuarioAdoptante.DoesNotExist, Perro.DoesNotExist):
        if not UsuarioAdoptante.objects.filter(dni=dni_usuario).exists():
            return "No encontramos al usuario, ¿lo creaste paparule?."
        if not Perro.objects.filter(id=id_perro).exists():
            return "No encontramos al pichiche... no lo habrás eliminado, ¿no?."

# Función para confirmar la adopción de un perro previamente reservado
# Cambia el estado del perro a 'adoptado' y lo agrega al historial del usuario si estaba reservado.
def confirmar_adopcion(dni_usuario, id_perro):
    try:
        usuario = UsuarioAdoptante.objects.get(dni=dni_usuario)
        perro = Perro.objects.get(id=id_perro)
        if perro.estado != "reservado":
            return f"No reservaste a '{perro.nombre}', nos figura como '{perro.estado}'. No se puede confirmar la adopción. ¿Lo reservaste con otro usuario?"
        perro.estado = "adoptado"
        perro.save()
        usuario.historial_adopciones.add(perro)
        return f"¡Felicitaciones! Te confirmamos la adopción de '{perro.nombre}', ya es parte de tu familia {usuario.nombre} {usuario.apellido}."
    except (UsuarioAdoptante.DoesNotExist, Perro.DoesNotExist):
        if not UsuarioAdoptante.objects.filter(dni=dni_usuario).exists():
            return "No encontramos al usuario, ¿lo creaste paparule?."
        if not Perro.objects.filter(id=id_perro).exists():
            return "No encontramos al pichiche... no lo habrás eliminado, ¿no?."