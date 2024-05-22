class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class ComentarioSeguidor:
    def __init__(self):
        self.comentarios = []
        self.seguidores = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def agregar_seguidor(self, seguidor):
        self.seguidores.append(seguidor)


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []


class Artista(Persona, ComentarioSeguidor):
    def __init__(self, nombre, oyentes, populares, álbumes, discografica, web, nacionalidad, wiki):
        super().__init__(nombre)
        self.oyentes = oyentes
        self.populares = populares
        self.álbumes = álbumes
        self.discografica = discografica
        self.web = web
        self.nacionalidad = nacionalidad
        self.wiki = wiki


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.listas_reproduccion = []

    def crear_lista_reproduccion(self, nombre):
        nueva_lista = {'nombre': nombre, 'canciones': []}
        self.listas_reproduccion.append(nueva_lista)
        print(f"Nueva lista de reproducción creada: {nombre}")

    def agregar_cancion_a_lista(self, nombre_lista, cancion):
        for lista in self.listas_reproduccion:
            if lista['nombre'] == nombre_lista:
                lista['canciones'].append(cancion)
                print(f"Canción {cancion} agregada a la lista {nombre_lista}")
                return
        print(f"No se encontró la lista de reproducción {nombre_lista}")

    def eliminar_cancion_de_lista(self, nombre_lista, cancion):
        for lista in self.listas_reproduccion:
            if lista['nombre'] == nombre_lista and cancion in lista['canciones']:
                lista['canciones'].remove(cancion)
                print(f"Canción {cancion} eliminada de la lista {nombre_lista}")
                return
        print(f"No se encontró la lista de reproducción {nombre_lista} o la canción {cancion}")

    def mostrar_listas_reproduccion(self):
        print("\nListas de Reproducción del Usuario:")
        for i, lista_usuario in enumerate(self.listas_reproduccion, start=1):
            print(f"{i}. {lista_usuario['nombre']}")
            print("   Canciones:")
            for cancion in lista_usuario['canciones']:
                print(f"    - {cancion}")
    def eliminar_lista_reproduccion(self, nombre_lista):
        for lista in self.listas_reproduccion:
            if lista['nombre'] == nombre_lista:
                self.listas_reproduccion.remove(lista)
                print(f"Lista de reproducción '{nombre_lista}' eliminada.")
                return
        print(f"No se encontró la lista de reproducción '{nombre_lista}'.")