# Importo el módulo de modelos de Django para usar las clases que definen campos de base de datos
from django.db import models
#Importo la clase Perro desde el archivo perro.py para establecer una relación Muchos a Muchos entre el usuario y los perros adoptados
from sistema.models.perro import Perro  # suponiendo que Perro está en otro archivo

# Defino el modelo UsuarioAdoptante que representa a un usuario que adopta perros
class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField()

    # Uso JSONField para guardar las preferencias como un diccionario como en la version anterior
    # default=dict significa que, si no se pasa nada, se guarda un diccionario vacío
    preferencias = models.JSONField(default=dict)

    # Método para obtener el nombre completo del usuario don su DNI en un string
    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"

    # Relación entre el usuario y los perros adoptados
    historial_adopciones = models.ManyToManyField(Perro, blank=True)

    #Método que devuelve todos los perros que el usuario ha adoptado.
    def ver_historial(self):
        return self.historial_adopciones.all()

## Comentarios finales para tener en cuenta:
## Nuestra clase usuarioAdoptante tenía varios métodos que no son necesarios en Django porque ya los maneja el framework, entonces solo adaptamos los que sí necesitamos:

## mostrar_id_usuario() // mostrar_info_usuario() → Son innecesarios, ahora lo mostramos con el método __str__ y el id lo genera el sistema automáticamente no hay que generarlo desde el código.
## modificar_datos() → No es necesario en Django, eso se hace con formularios, vistas o admin.
## ver_historial() → Este método si lo adaptamos para poder mostrar el historial de adopciones del usuario adoptante. Se definió una relación de muchos a muchos.