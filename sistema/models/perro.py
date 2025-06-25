# Importo el módulo de modelos de Django para usar las clases que definen campos de base de datos
from django.db import models

# Defino el modelo Perro que representa a un perro en el sistema de adopción
class Perro(models.Model):
    # Defino las opciones para los campos de estado, tamaño y sexo como listas de tuplas
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado'),
    ]

    TAMAÑOS = [
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]

    SEXOS = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
        ('indistinto', 'Indistinto'),
    ]

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15, choices=SEXOS)
    tamaño = models.CharField(max_length=15, choices=TAMAÑOS)
    peso = models.FloatField()
    # no podria ser una tupla tmb?
    estado_salud = models.TextField()
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='disponible')
    # no podria ser una tupla tmb?
    temperamento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.raza} - ID: {self.id}) - Edad: {self.edad} años, Tamaño: {self.tamaño}, Estado: {self.estado}"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.save()
    
    @property # Lo ponemos como propiedad para que se pueda acceder como un atributo de tipo booleano
    def es_adulto(self):
        return self.edad >=8 # Considerando adulto a partir de 8 años
    
    # Método para mostrar una info distinta de los pichichos de acuerdo a la edad, como haciamos con las clases Perro y PerroAdulto en nuestro código anterior.
    def mostrar_info_perro(self):
        if self.es_adulto:
            return f"{self.nombre} (ID: {self.id}) es un {self.raza} de {self.edad} años - Estado: {self.estado}. ¡Es un perrito adulto lleno de amor para dar!"
        else:
            return f"{self.nombre} (ID: {self.id}) es un {self.raza} de {self.edad} años - Estado: {self.estado}."

## Comentarios finales para tener en cuenta:
## Nuestra clase Perro tenía varios métodos que no son necesarios en Django porque ya los maneja el framework, entonces solo adaptamos los que sí necesitamos:

## mostrar_id_perro() → Es innecesario, ahora lo mostramos con el método __str__ y el id lo genera el sistema automáticamente no hay que generarlo desde el código.
## cambiar_estado() → Lo adaptamoso y usamos save()
## es_adulto → Adaptamos la subclase PerroAdulto ya que no podemos aplicar Herencia y poliformismo de la misma forma. Ahora lo usamos como una propiedad para dar un mensaje distinto con el método mostrar_info_perro().
## mostrar_info_perro() → Lo adaptamos con un if para usar la propiedad es_adulto y mostrar un mensaje distinto si se cumple la condición. De esta forma, mantenemos la funcionalidad original de nuestro sistema.