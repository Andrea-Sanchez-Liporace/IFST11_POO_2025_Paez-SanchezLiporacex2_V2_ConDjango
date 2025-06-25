# Importo el modelo del Perro para usarlo en las funciones relacionadas con perros.
from sistema.models.perro import Perro

# Función para cargar un nuevo perro en la base de datos
def cargar_perro(datos_perro):
    return Perro.objects.create(**datos_perro)

# Función para eliminar un perro por su ID
def eliminar_perro(id_perro):
    try:
        perro = Perro.objects.get(id=id_perro)
        nombre, identificador = perro.nombre, perro.id
        perro.delete()
        return f"El pichiche '{nombre}' (ID: {identificador}) fue eliminado correctamente"
    except Perro.DoesNotExist:
        return f"No se pudo eliminar el registro, el perro no existe en el sistema"

# Función para sugerir perros
# Filtra perros disponibles que coincidan con las preferencias del usuario. Si alguna preferencia es 'indistinto', se omite en el filtro.
def sugerir_perros(preferencias):
    perros = Perro.objects.filter(estado='disponible')

    if preferencias.get("sexo") != "indistinto":
        perros = perros.filter(sexo=preferencias["sexo"])
    if preferencias.get("raza") != "indistinto":
        perros = perros.filter(raza=preferencias["raza"])
    if preferencias.get("edad") != "indistinto":
        perros = perros.filter(edad=preferencias["edad"])
    if preferencias.get("tamaño") != "indistinto":
        perros = perros.filter(tamaño=preferencias["tamaño"])
    return perros

# Función para mostrar todos los perros disponibles.
def mostrar_perros_disponibles():
    return Perro.objects.filter(estado='disponible')

# Función para mostrar todos los perros según su estado.
def mostrar_perros_por_estado(estado):
    if estado == 'disponible':
        return mostrar_perros_disponibles()
    elif estado == 'adoptado':
        return Perro.objects.filter(estado='adoptado')
    elif estado == 'reservado':
        return Perro.objects.filter(estado='reservado')