import random
from clases import Artista, Usuario
from funciones_json import cargar_lista_desde_json, cargar_listas_usuario_desde_json, guardar_lista_como_json
def mostrar_opciones():
    print("\nOpciones adicionales:")
    print("a. Agregar canciones a un artista existente")
    print("b. Agregar un nuevo artista")
    print("c. Generar una lista aleatoria de canciones")
    print("d. Eliminar canciones de un artista")
    print("e. Actualizar información de un artista")
    print("f. Eliminar la información de un artista")
    print("g. Agregar Comentario")
    print("h. Seguir a un artista")
    print("u. Administrar Listas de Reproducción (Usuario)")
    print("s. Salir")


def agregar_artista(lista, usuario):
    nuevo_artista = {}
    print("Ingrese la información del nuevo artista:")
    nuevo_artista['nombre'] = input("Nombre: ")
    nuevo_artista['oyentes'] = int(input("Oyentes: "))
    nuevo_artista['populares'] = [c.strip() for c in input("Canciones populares (separadas por comas): ").split(',')]
    nuevo_artista['álbumes'] = [a.strip() for a in input("Álbumes (separados por comas): ").split(',')]
    nuevo_artista['discografica'] = input("Discográfica: ")
    nuevo_artista['web'] = input("Página web: ")
    nuevo_artista['nacionalidad'] = input("Nacionalidad: ")
    nuevo_artista['wiki'] = input("Enlace a Wikipedia: ")

    lista.append(nuevo_artista)
    print("Nuevo artista agregado exitosamente.")
    guardar_lista_como_json(lista, usuario.listas_reproduccion)

def main():
    lista = cargar_lista_desde_json()
    usuario = Usuario("NombreUsuario", "email@example.com")  # Cambia a mayúscula la instancia
    usuario.listas_reproduccion = cargar_listas_usuario_desde_json()
    while True:
        print("\nArtistas disponibles:")
        for i, artista in enumerate(lista, start=1):
            print(f"{i}. {artista['nombre']}")

        mostrar_opciones()
        eleccion_usuario = input("\nIngrese el número del artista del cual busca información, o la letra de la opción adicional que desea: ")

        if eleccion_usuario.lower() == 's':
            print("¡Hasta luego!")
            guardar_lista_como_json(lista, usuario.listas_reproduccion)
            break
        elif eleccion_usuario.lower() == 'a':
            try:
                opcion_artista = int(input("Ingrese el número del artista al que desea agregar canciones: ")) - 1
                artista_seleccionado = lista[opcion_artista]
                print(f"\nAgregando canciones a {artista_seleccionado['nombre']}")
                nuevas_canciones = input("Ingrese las nuevas canciones separadas por comas: ").split(',')
                artista_seleccionado['populares'].extend(nuevas_canciones)
                print("Canciones agregadas exitosamente.")
            except IndexError:
                print("Artista inválido.")

        elif eleccion_usuario.lower() == 'b':
            agregar_artista(lista, usuario)
            guardar_lista_como_json(lista, usuario.listas_reproduccion)

        elif eleccion_usuario.lower() == 'c':
            todas_las_canciones = [cancion for artista in lista for cancion in artista['populares']]
            total_canciones = len(todas_las_canciones)
            mitad_total_canciones = total_canciones // 2
            random_playlist = random.sample(todas_las_canciones, mitad_total_canciones)

            print("\nLista de reproducción aleatoria:")
            for cancion in random_playlist:
                print(cancion)

        elif eleccion_usuario.lower() == 'd':
            try:
                opcion_artista_eliminar = int(input("Ingrese el número del artista del que desea eliminar canciones: ")) - 1
                artista_seleccionado_eliminar = lista[opcion_artista_eliminar]
                print(f"\nEliminando canciones de {artista_seleccionado_eliminar['nombre']}")
                canciones_actuales = artista_seleccionado_eliminar['populares']
                print("Canciones actuales:", ', '.join(canciones_actuales))
                canciones_eliminar = input("Ingrese las canciones que desea eliminar (separadas por comas): ").split(',')
                artista_seleccionado_eliminar['populares'] = [c for c in canciones_actuales if c not in canciones_eliminar]
                print("Canciones eliminadas exitosamente.")
            except IndexError:
                print("Artista inválido.")
        elif eleccion_usuario.lower() == 'e':
            # Actualizar información de un artista
            try:
                opcion_artista_actualizar = int(input("Ingrese el número del artista que desea actualizar: ")) - 1
                artista_seleccionado_actualizar = lista[opcion_artista_actualizar]
                print(f"\nActualizando información de {artista_seleccionado_actualizar['nombre']}")
                artista_seleccionado_actualizar['oyentes'] = int(input(f"Nuevo número de oyentes ({artista_seleccionado_actualizar['oyentes']}): "))
                nuevas_populares = input(f"Nuevas canciones populares ({', '.join(artista_seleccionado_actualizar['populares'])}): ")
                artista_seleccionado_actualizar['populares'] = [c.strip() for c in nuevas_populares.split(',')]
                nuevos_albumes = input(f"Nuevos álbumes ({', '.join(artista_seleccionado_actualizar['álbumes'])}): ")
                artista_seleccionado_actualizar['álbumes'] = [a.strip() for a in nuevos_albumes.split(',')]
                artista_seleccionado_actualizar['discografica'] = input(f"Nueva discográfica ({artista_seleccionado_actualizar['discografica']}): ")
                artista_seleccionado_actualizar['web'] = input(f"Nueva página web ({artista_seleccionado_actualizar['web']}): ")
                artista_seleccionado_actualizar['nacionalidad'] = input(f"Nueva nacionalidad ({artista_seleccionado_actualizar['nacionalidad']}): ")
                artista_seleccionado_actualizar['wiki'] = input(f"Nueva Wikipedia ({artista_seleccionado_actualizar['wiki']}): ")
                print("Información actualizada exitosamente.")
            except IndexError:
                print("Artista inválido.")

        elif eleccion_usuario.lower() == 'f':
            # Eliminar información de un artista
            try:
                opcion_artista_eliminar = int(input("Ingrese el número del artista que desea eliminar: ")) - 1
                artista_seleccionado_eliminar = lista.pop(opcion_artista_eliminar)
                print(f"\nEliminando información de {artista_seleccionado_eliminar['nombre']}")
                print("Información eliminada exitosamente.")
            except IndexError:
                print("Artista inválido.")
        elif eleccion_usuario.lower() == 'g':
    # Agregar comentario
            try:
                opcion_artista_comentario = int(input("Ingrese el número del artista al que desea agregar un comentario: ")) - 1
                artista_seleccionado_comentario = lista[opcion_artista_comentario]
                print(f"\nAgregando comentario a {artista_seleccionado_comentario['nombre']}")

        # Verificar si 'comentarios' ya existe en el diccionario del artista
                if 'comentarios' not in artista_seleccionado_comentario:
                    artista_seleccionado_comentario['comentarios'] = []

                usuario_comentario = input("Ingrese su nombre de usuario: ")
                contenido_comentario = input("Ingrese el contenido del comentario: ")
                artista_seleccionado_comentario['comentarios'].append({
                    'usuario': usuario_comentario,
                    'contenido': contenido_comentario
                })
                print("Comentario agregado exitosamente.")
            except IndexError:
                print("Artista inválido.")
        elif eleccion_usuario.lower() == 'h':
            # Agregar seguidor
            try:
                opcion_artista_seguidor = int(input("Ingrese el número del artista al que desea seguir: ")) - 1
                artista_seleccionado_seguidor = lista[opcion_artista_seguidor]

                # Verificar si 'seguidores' ya existe en el diccionario del artista
                if 'seguidores' not in artista_seleccionado_seguidor:
                    artista_seleccionado_seguidor['seguidores'] = []

                print(f"\nSiguiendo a {artista_seleccionado_seguidor['nombre']}")
                nombre_seguidor = input("Ingrese su nombre: ")
                ubicacion_seguidor = input("Ingrese su ubicación: ")
                artista_seleccionado_seguidor['seguidores'].append({
                    'nombre': nombre_seguidor,
                    'ubicacion': ubicacion_seguidor
                })
                print("Ahora sigue a", artista_seleccionado_seguidor['nombre'])
            except IndexError:
                print("Artista inválido.")

        elif eleccion_usuario.lower() == 'u':
            # Menú de administración de listas de reproducción del usuario
            while True:
                usuario.mostrar_listas_reproduccion()

                print("\nOpciones adicionales:")
                print("a. Crear nueva lista de reproducción")
                print("b. Agregar canción a lista de reproducción")
                print("c. Eliminar canción de lista de reproducción")
                print("d. Eliminar lista de reproducción")
                print("s. Salir al menú principal")

                eleccion_usuario = input("\nSeleccione una opción adicional para gestionar sus listas de reproducción: ")

                if eleccion_usuario.lower() == 's':
                    print("Guardando cambios y volviendo al menú principal...")
                    break

                elif eleccion_usuario.lower() == 'a':
                    nombre_nueva_lista = input("Ingrese el nombre de la nueva lista de reproducción: ")
                    usuario.crear_lista_reproduccion(nombre_nueva_lista)
                elif eleccion_usuario.lower() == 'b':
                    nombre_lista_agregar = input("Ingrese el nombre de la lista a la que desea agregar la canción: ")
                    
                    cancion_a_agregar = input("Ingrese el nombre de la canción que desea agregar: ")
                    usuario.agregar_cancion_a_lista(nombre_lista_agregar, cancion_a_agregar)
                    print(f"Canción {cancion_a_agregar} agregada a la lista {nombre_lista_agregar}")

                elif eleccion_usuario.lower() == 'c':
                    nombre_lista_eliminar = input("Ingrese el nombre de la lista de la que desea eliminar la canción: ")
                    cancion_a_eliminar = input("Ingrese el nombre de la canción que desea eliminar: ")
                    usuario.eliminar_cancion_de_lista(nombre_lista_eliminar, cancion_a_eliminar)
                    print(f"Canción {cancion_a_eliminar} eliminada de la lista {nombre_lista_eliminar}")
                elif eleccion_usuario.lower() == 'd':
                    nombre_lista_eliminar = input("Ingrese el nombre de la lista de reproducción que desea eliminar: ")
                    usuario.eliminar_lista_reproduccion(nombre_lista_eliminar)

                else:
                    print("Opción no válida.")

            # Guardar las listas de reproducción del usuario en el archivo JSON
            guardar_lista_como_json(lista, usuario.listas_reproduccion)
        else:
            try:
                eleccion_usuario = int(eleccion_usuario)
                if 0 < eleccion_usuario <= len(lista):
                    artista_mostrar = lista[eleccion_usuario - 1]
                    print(f"\nInformación de {artista_mostrar['nombre']}:\n")
                    print(f"Oyentes: {artista_mostrar['oyentes']}")
                    print(f"Populares: {', '.join(artista_mostrar['populares'])}")
                    print(f"Álbumes: {', '.join(artista_mostrar['álbumes'])}")
                    print(f"Discográfica: {artista_mostrar['discografica']}")
                    print(f"Página web: {artista_mostrar['web']}")
                    print(f"Nacionalidad: {artista_mostrar['nacionalidad']}")
                    print(f"Wikipedia: {artista_mostrar['wiki']}")
                else:
                    try:
                        eleccion_usuario = int(eleccion_usuario)
                        if 0 < eleccion_usuario <= len(lista):
                            artista_seleccionado = Artista(**lista[eleccion_usuario - 1])
                            artista_seleccionado.mostrar_informacion()
                        else:
                            print("Opción inválida.")
                    except ValueError:
                        print("Opción inválida. Ingrese un número o una letra válida.")

                respuesta = input("\n¿Desea seguir consultando? (s/n): ")
                if respuesta.lower() == 'n':
                    print("¡Hasta luego!")
                    guardar_lista_como_json(lista, usuario.listas_reproduccion)
                    break
            except ValueError:
                print("Opción inválida. Ingrese un número o una letra válida.")


if __name__ == "__main__":
    main()