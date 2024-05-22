import json

ARCHIVO_JSON = 'cantantes.json'
ARCHIVO_LISTAS_JSON = 'listas_reproduccion.json'



def cargar_lista_desde_json():
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            lista_cargada = json.load(archivo)
            return lista_cargada
    except FileNotFoundError:
        return []


def cargar_listas_usuario_desde_json():
    try:
        with open(ARCHIVO_LISTAS_JSON, 'r', encoding='utf-8') as archivo:
            listas_usuario_cargadas = json.load(archivo)
            return listas_usuario_cargadas
    except FileNotFoundError:
        return []


def guardar_lista_como_json(lista_artistas, listas_usuario):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(lista_artistas, archivo, ensure_ascii=False, indent=4)

    with open(ARCHIVO_LISTAS_JSON, 'w', encoding='utf-8') as archivo_listas:
        json.dump(listas_usuario, archivo_listas, ensure_ascii=False, indent=4)