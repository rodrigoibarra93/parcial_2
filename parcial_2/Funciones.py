import random
import os
import pygame
import json
import datetime
import csv
from Constantes import *

def limpiar_consola():
    """
  Descripción: Limpia la consola del terminal.
  Esta función espera a que el usuario presione cualquier tecla antes de limpiar la 
  pantalla. Esto es útil para pausar la ejecución del programa y permitir al usuario 
  revisar la salida antes de continuar.

  Parametros: Esta función no toma ningún argumento.

  Retorna: Esta función no retorna ningún valor.
  """
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    """
    Descripción: Esta función solicita al usuario 
    que ingrese un número entero dentro de un rango específico. 
    Continúa solicitando el número hasta 
    que el usuario ingrese un valor válido.

    Parámetros:
        mensaje: Un mensaje de cadena que se muestra al usuario para solicitar el número.
        mensaje_error: Un mensaje de cadena que se muestra al usuario si el número ingresado está fuera del rango.
        minimo: El valor mínimo permitido para el número.
        maximo: El valor máximo permitido para el número.
    
    Retorno: Retorna el número entero válido ingresado por el usuario.
    """
    numero_ingresado = int(input(mensaje))
    while numero_ingresado > maximo or numero_ingresado < minimo:
        numero_ingresado = int(input(mensaje_error))
    return numero_ingresado

def mostrar_pregunta(pregunta_juego:dict) -> None :
    print(f"PREGUNTA: {pregunta_juego['pregunta']}")
    print(f"1 - {pregunta_juego['respuesta_1']}")
    print(f"2 - {pregunta_juego['respuesta_2']}")
    print(f"3 - {pregunta_juego['respuesta_3']}")
    print(f"4 - {pregunta_juego['respuesta_4']}")
    
def mezclar_lista(lista:list) -> None:
    random.shuffle(lista)



def terminar_juego(datos_juego:dict,nombre:str,lista_ranking:list,ruta_archivo) -> None:
    fecha = datetime.datetime.now()
    diccionario_ranking = {
        "puntuacion": datos_juego["puntuacion"],
        "nombre": nombre,
        "tiempo": datos_juego["tiempo"],
        "fecha": fecha.strftime("%x")
    }
    lista_ranking.append(diccionario_ranking)
    generar_json(ruta_archivo, lista_ranking)
    
def reiniciar_estadisticas(datos_juegos:dict) -> None:
    datos_juegos['puntuacion'] = 0
    datos_juegos['vidas'] = CANTIDAD_VIDAS_MEDIO
    datos_juegos['tiempo'] = TIEMPO_MEDIO
    
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    """
    Descripción: Esta función verifica si la respuesta proporcionada 
    por el usuario a una pregunta es correcta. Actualiza los datos del juego 
    (puntuación y vidas) en consecuencia y devuelve un valor booleano indicando 
    si la respuesta fue correcta o no.

    Parámetros:
        datos_juego:dict: Un diccionario que contiene los datos del juego, incluyendo la puntuación actual y las vidas restantes.
        pregunta_actual:dict: Un diccionario que contiene los datos de la pregunta actual, incluyendo la respuesta correcta.
        respuesta:int: La respuesta proporcionada por el usuario.

    Retorno:
        bool: Devuelve `True` si la respuesta es correcta y `False` si es incorrecta.

    Funcionamiento:
        1.Comparación de respuestas: Compara la respuesta proporcionada por el usuario con la respuesta correcta almacenada en `pregunta_actual`.
        2.Actualización de datos del juego:
            Si la respuesta es correcta:
            Incrementa la puntuación del jugador.
            Si la respuesta es incorrecta:
            Decrementa la puntuación del jugador.
            Decrementa el número de vidas restantes.
        3.Retorno del resultado: Devuelve `True` si la respuesta es correcta y `False` en caso contrario.
    """
    if pregunta_actual['respuesta_correcta'] == respuesta:
        datos_juego['puntuacion'] += PUNTUACION_ACIERTO
        retorno = True
    else:
        datos_juego['puntuacion'] -= PUNTUACION_ERROR
        datos_juego['vidas'] -= 1
        retorno = False
    
    return retorno
    

# def jugar_preguntados_consola(datos_juego:dict,lista_preguntas:list[dict]) -> None:
#     #Ciclo del juego
#     indice = 0
#     while datos_juego['vidas'] != 0:
#         print(f"PUNTUACION ACTUAL: {datos_juego['puntuacion']}")
#         print(f"VIDAS RESTANTES: {datos_juego['vidas']}\n")
        
#         if indice == len(lista_preguntas):
#             indice = 0
#             mezclar_lista(lista_preguntas)
            
#         pregunta_actual = lista_preguntas[indice]
#         mostrar_pregunta(pregunta_actual)
#         respuesta = pedir_numero("Su respuesta: ","Reingrese su respuesa: (Debe estar 1 y 3)",1,3)
    
#         if verificar_respuesta(datos_juego,pregunta_actual,respuesta):
#             print("RESPUESTA CORRECTA")
#         else:
#             print("RESPUESTA INCORRECTO")
        
#         indice+=1
#         limpiar_consola()


def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    """
    Descripción: Esta función muestra un texto multilínea en una superficie de Pygame, 
    ajustándolo automáticamente al ancho de la superficie.

    Parámetros:
        surface: La superficie de Pygame donde se mostrará el texto.
        text: El texto a mostrar, que puede contener múltiples líneas separadas por saltos de línea (`\n`).
        pos: Una tupla (x, y) que representa la posición inicial del texto en la superficie.
        font: El objeto de fuente de Pygame utilizado para renderizar el texto.
        color: El color del texto. Por defecto, es negro (pygame.Color('black')).

    Funcionamiento:
        1.Dividir el texto: El texto se divide en una lista de listas de palabras, donde cada lista interna representa una línea de texto.
        2.Calcular el ancho de un espacio: Se calcula el ancho de un espacio en píxeles utilizando la fuente especificada.
        3.Obtener el tamaño de la superficie: Se obtiene el ancho y alto de la superficie.
        4.Iterar sobre las líneas y palabras:
            - Para cada línea de texto:
            - Para cada palabra en la línea:
            - Se renderiza la palabra en una superficie utilizando la fuente y el color especificados.
            - Se calcula el ancho y alto de la superficie de la palabra.
            - Si la posición actual más el ancho de la palabra excede el ancho máximo de la superficie:
            - Se reinicia la posición horizontal `x` a la posición inicial `pos[0]`.
            - Se incrementa la posición vertical `y` para pasar a la siguiente línea.
            - Se dibuja la superficie de la palabra en la posición actual `(x, y)` utilizando `surface.blit()`.
            - Se incrementa la posición horizontal `x` para la siguiente palabra.
            - Se reinicia la posición horizontal `x` a la posición inicial `pos[0]` para la siguiente línea.
            - Se incrementa la posición vertical `y` para pasar a la siguiente línea.
    """
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    


# def mostrar_diccionario(diccionario) -> None:
#     for clave,valor in diccionario.items():
#         print((f"{clave.title().replace("_","")} : {valor}"))

# def mostrar_diccionario2(diccionario):
#     if not isinstance(diccionario, dict):
#         print("El argumento debe ser un diccionario")
#         return
    
#     for clave, valor in diccionario.items():
#         print(f"{clave.title().replace(' ', '_')} : {valor}")
        
# def mostrar_lista_diccionarios(lista:list) -> bool:
#     retorno = False
#     for elemento in lista:
#         retorno = True
#         mostrar_diccionario2(elemento)
#         print("")
        
#     return retorno

def crear_diccionario_pregunta(lista_valores:list) -> dict:
    preguntas = {}
    preguntas['pregunta'] = lista_valores[0]
    preguntas['respuesta_1'] = lista_valores[1]
    preguntas['respuesta_2'] = lista_valores[2]
    preguntas['respuesta_3'] = lista_valores[3]
    preguntas['respuesta_4'] = lista_valores[4]
    preguntas['respuesta_correcta'] = int(lista_valores[5])
    return preguntas

def leer_csv(nombre_archivo:str,lista:list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
            #Falsa lectura -> Para evitar recorrer en el for de abajo, la cabecera
            archivo.readline()
            
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                una_pregunta = crear_diccionario_pregunta(lista_valores)
                lista.append(una_pregunta)
        retorno = True
        
    else:
        
        retorno = False
        
    return retorno
      


def leer_json(nombre_archivo:str)->bool:
    if os.path.exists(nombre_archivo):
        lista = []
        with open(nombre_archivo,"r") as archivo:
            lista = json.load(archivo)
        return lista

def generar_json(nombre_arhivo:str,lista:list)->bool:
    if type(lista) == list and len(lista) > 0:
        with open(nombre_arhivo,"w") as archivo:
            json.dump(lista,archivo,indent=4)
        retorno = True
    else:
        retorno = False

    return retorno

# def obtener_top_10(lista_ranking):
#     """
#     Obtiene los 10 mejores registros de una lista de diccionarios, ordenados por puntuación y tiempo.

#     Args:
#         lista_ranking (list): Lista de diccionarios con las claves "puntuacion", "tiempo", "vidas", "usuario", "volumen_musica" y "volumen_musica_principal".

#     Returns:
#         list: Lista de diccionarios con los 10 mejores registros, ordenados de mayor a menor puntuación y tiempo.
#     """

#     # Ordenar la lista por puntuación (de mayor a menor) y tiempo (de menor a mayor)
#     lista_ranking.sort(key=lambda x: (-x["puntuacion"], x["tiempo"]))

#     # Retornar los primeros 10 elementos de la lista ordenada
#     return lista_ranking[:10]



def obtener_top_10(lista_ranking):
    """
    Obtiene los 10 mejores registros de una lista de diccionarios, ordenados por puntuación (descendente) y tiempo (ascendente),
    utilizando el algoritmo de burbujeo.

    Args:
        lista_ranking (list): Lista de diccionarios con las claves "puntuacion", "tiempo", "vidas", "usuario", "volumen_musica" y "volumen_musica_principal".

    Returns:
        list: Lista de diccionarios con los 10 mejores registros, ordenados.
    """

    n = len(lista_ranking)
    # Iteraciones para el ordenamiento por burbuja
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_ranking[j]["puntuacion"] < lista_ranking[j+1]["puntuacion"] or \
                (lista_ranking[j]["puntuacion"] == lista_ranking[j+1]["puntuacion"] and lista_ranking[j]["tiempo"] > lista_ranking[j+1]["tiempo"]):
                # Intercambiar posiciones si el elemento de la izquierda es menor
                lista_ranking[j], lista_ranking[j+1] = lista_ranking[j+1], lista_ranking[j]

    # Retornar los primeros 10 elementos de la lista ordenada
    return lista_ranking[:10]



def escalar_superficie(superficie,tamaño):
    """
    Escala una superficie a un nuevo tamaño.

    Args:
        superficie (pygame.Surface): La superficie a escalar.
        tamaño (tuple): Una tupla (ancho, alto) con el nuevo tamaño.

    Returns:
        pygame.Surface: La superficie escalada.
    """
    superficie_escalada = pygame.transform.scale(superficie,tamaño)
    return superficie_escalada


def crear_boton(tamaño):
    """
    Crea un diccionario que representa un botón de Pygame.

    Args:
        tamaño (tuple): Una tupla (ancho, alto) que define el tamaño del botón.
    Returns:
        dict: Un diccionario con las claves "superficie" y "rectangulo" que representan el botón.
    """

    boton = {}
    boton["superficie"] = pygame.Surface(tamaño)
    boton["rectangulo"] = boton["superficie"].get_rect()
    
    return boton


def reproducir_musica(ruta_musica,volumen):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.set_volume(volumen / 100)
    pygame.mixer.music.play(-1) 