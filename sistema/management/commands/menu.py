# Importo los modulos de Django y los servicios necesarios para nuestro menú interactivo.
from django.core.management.base import BaseCommand
from sistema.services.usuario import registrar_usuario, buscar_usuario_por_dni, mostrar_usuarios
from sistema.services.perro import (cargar_perro,eliminar_perro,mostrar_perros_disponibles,mostrar_perros_por_estado, sugerir_perros)
from sistema.services.adopcion import (reservar_perro,confirmar_adopcion)

class Command(BaseCommand):
    help = "Menú interactivo del sistema de adopción de perros"

    def handle(self, *args, **kwargs):
        while True:
            print("\n Menú del Sistema de Adopción")
            print("1. Registrar usuario")
            print("2. Cargar perro")
            print("3. Eliminar perro")
            print("4. Mostrar perros disponibles")
            print("5. Postular a adopción")
            print("6. Confirmar adopción")
            print("7. Sugerencias por preferencias")
            print("8. Ver historial de usuario")
            print("9. Ver listado de usuarios adoptantes")
            print("10. Ver listado de perros según estado")
            print("0. Salir del menú")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = input("DNI: ")
                email = input("Email: ")
                sexo = input("Preferencia de sexo (o 'indistinto'): ")
                raza = input("Preferencia de raza (o 'indistinto'): ")
                edad = input("Preferencia de edad (o 'indistinto'): ")
                tamaño = input("Preferencia de tamaño (o 'indistinto'): ")

                datos_usuario = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "dni": dni,
                    "email": email,
                    "preferencias": {
                        "sexo": sexo,
                        "raza": raza,
                        "edad": edad,
                        "tamaño": tamaño
                    }
                }
                registrar_usuario(datos_usuario)
                print("Usuario registrado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre del perro: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                sexo = input("Sexo: ")
                tamaño = input("Tamaño: ")
                peso = float(input("Peso: "))
                estado_salud = input("Estado de salud: ")
                vacunado = input("¿Está vacunado? (s/n): ").lower() == "s"
                estado = input("Estado (disponible / reservado / adoptado): ")
                temperamento = input("Temperamento: ")

                datos_perro = {
                    "nombre": nombre,
                    "raza": raza,
                    "edad": edad,
                    "sexo": sexo,
                    "tamaño": tamaño,
                    "peso": peso,
                    "estado_salud": estado_salud,
                    "vacunado": vacunado,
                    "estado": estado,
                    "temperamento": temperamento
                }
                cargar_perro(datos_perro)
                print("El pichicho se registró correctamente.")

            elif opcion == "3":
                id_perro = input("ID del perro a eliminar: ")
                eliminar_perro(id_perro)

            elif opcion == "4":
                perros = mostrar_perros_disponibles()
                if perros:
                    print("Perros disponibles:")
                    for p in perros:
                        print(f"{p.nombre} (ID: {p.id}) - {p.raza}, edad: {p.edad}, estado: {p.estado}")
                else:
                    print("No hay perros disponibles.")

            elif opcion == "5":
                dni = input("DNI del usuario: ")
                id_perro = input("ID del perro: ")
                reservar_perro(dni, id_perro)

            elif opcion == "6":
                dni = input("DNI del usuario: ")
                id_perro = input("ID del perro: ")
                confirmar_adopcion(dni, id_perro)

            elif opcion == "7":
                dni = input("DNI del usuario: ")
                usuario = buscar_usuario_por_dni(dni)
                if usuario:
                    perros = sugerir_perros(usuario.preferencias)
                    if perros.exists():
                        print("Tenemos estos pichichos que matchean con vos:")
                        for p in perros:
                            print(f"{p.nombre} (ID: {p.id}) - {p.raza}, edad: {p.edad}, tamaño: {p.tamaño}, estado: {p.estado}")
                    else:
                        print("No encontramos perros que coincidan con tus preferencias.")
                else:
                    print("Usuario no encontrado.")

            elif opcion == "8":
                dni = input("DNI del usuario: ")
                usuario = buscar_usuario_por_dni(dni)
                if usuario:
                    historial = usuario.ver_historial()
                    if historial.exists():  # Verifica si hay perros adoptados
                        print(f"Historial de adopciones de {usuario.nombre} {usuario.apellido}:")
                        for perro in historial:
                            print(f"- {perro.nombre} (ID: {perro.id}) - {perro.raza}, estado: {perro.estado}")
                    else:
                        print(f"{usuario.nombre}, {usuario.apellido} aún no ha adoptado ningún perro.")
                else:
                    print("No se encontró el usuario, lo creaste?.")

            elif opcion == "9":
                usuarios = mostrar_usuarios()
                if usuarios:
                    print("Usuarios registrados en el sistema:")
                    for u in usuarios:
                        print(f"- {u}")
                else:
                    print("No hay usuarios registrados aún.")

            elif opcion == "10":
                estado = input("Ingrese el estado a consultar (disponible/reservado/adoptado): ")
                perros = mostrar_perros_por_estado(estado)
                if perros:
                    print("Listado de perros solicitados:")
                    for p in perros:
                        print(f"{p.nombre} (ID: {p.id}) - {p.raza}, edad: {p.edad}, estado: {p.estado}")
                else:
                    print("En el sistema no hay perros con el estado solicitado.")

            elif opcion == "0":
                print("¡Gracias por usar nuestro sistema!")
                break

            else:
                print("Ingresaste una opción inválida. Por favor, elegí un número del 0 al 10.")