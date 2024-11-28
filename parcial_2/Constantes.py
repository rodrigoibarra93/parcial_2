import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_GRIS = (169,169,169)
ANCHO = 800
ALTO = 600
VENTANA = (ANCHO,ALTO)
VENTANA_EXPANDIDA = (1980,1080)
FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO_1 = (250,90)
CUADRO_TEXTO_2 = (250,50)
CUADRO_TEXTO_3 = (600,60)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,60)
TAMAÑO_BOTON_DIFICULTAD = (50,50)

FUENTE_60 = pygame.font.SysFont("Arial Narrow",60)
FUENTE_50 = pygame.font.SysFont("Arial Narrow",50)
FUENTE_40 = pygame.font.SysFont("Arial Narrow",40)
FUENTE_32 = pygame.font.SysFont("Arial Narrow",32)
FUENTE_30 = pygame.font.SysFont("Arial Narrow",30)
FUENTE_25 = pygame.font.SysFont("Arial Narrow",25)
FUENTE_22 = pygame.font.SysFont("Arial Narrow",22)

CLICK_SONIDO = pygame.mixer.Sound("parcial_2\materiales\click.mp3")
CLICK_DE_ERROR = pygame.mixer.Sound("parcial_2\materiales\click_error.mp3")
CLICK_ERROR = pygame.mixer.Sound("parcial_2\materiales\click de error.mp3")
CLICK_ACIERTO = pygame.mixer.Sound("parcial_2\materiales\click acierto.mp3")

CANTIDAD_VIDAS = 5
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
CANTIDAD_VIDAS_FACIL = 10
CANTIDAD_VIDAS_MEDIO = 5
CANTIDAD_VIDAS_DIFICIL = 3

TIEMPO_FACIL = 120
TIEMPO_MEDIO = 90
TIEMPO_DIFICIL = 60

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

ICONO = pygame.image.load("parcial_2\materiales\icono.jpg")

FONDO_MENU = pygame.image.load("parcial_2\materiales\pantalla_menu_1.jpg")
FONDO_JUEGO = pygame.image.load("parcial_2\materiales\pantalla_juego.jpg")
FONDO_CONFIGURACIONES = pygame.image.load("parcial_2\materiales\pantalla_configuraciones_2.jpg")
FONDO_RANKING = pygame.image.load("parcial_2\materiales\pantalla_ranking.jpg")
FONDO_TERMINADO = pygame.image.load("parcial_2\materiales\pantalla_terminado.jpg")


FONDO_PREGUNTA = pygame.image.load("parcial_2\materiales\pantalla de preguntas.png")
FONDO_RESPUESTA_1 = pygame.image.load("parcial_2\materiales\pantalla_respuesta_1.jpg")
FONDO_RESPUESTA_2 = pygame.image.load("parcial_2\materiales\pantalla_respuesta_2.jpg")
FONDO_RESPUESTA_3 = pygame.image.load("parcial_2\materiales\pantalla_respuesta_3.jpg")
FONDO_RESPUESTA_4 = pygame.image.load("parcial_2\materiales\pantalla_respuesta_4.jpg")

FONDO_ACIERTO = pygame.image.load("parcial_2\materiales\imagen acierto.jpg")
FONDO_ERROR = pygame.image.load("parcial_2\materiales\imagen error.jpg")


FONDO_DIFICULTAD_FACIL = pygame.image.load("parcial_2\materiales\dificultad_facil.png")
FONDO_DIFICULTAD_MEDIA = pygame.image.load("parcial_2\materiales\dificultad_medio.png")
FONDO_DIFICULTAD_DIFICIL = pygame.image.load("parcial_2\materiales\dificultad_dificil.png")

FONDO_TEXTO_DIFICULTAD = pygame.image.load("parcial_2\materiales\pantalla_texto_dificultad.jpg")

FONDO_TEXTO_PUNTUACION = pygame.image.load("parcial_2\materiales\pantalla_texto_puntuacion.jpg")

FONDO_SUMA = pygame.image.load("parcial_2\materiales\pantalla_suma.png")
FONDO_RESTA = pygame.image.load("parcial_2\materiales\pantalla_resta.png")

FONDO_VOLVER = pygame.image.load("parcial_2\materiales\pantalla_volver.png")

MENU_BOTON_1 = pygame.image.load("parcial_2\materiales\menu_boton_1.jpg")
MENU_BOTON_2 = pygame.image.load("parcial_2\materiales\menu_boton_2.jpg")
MENU_BOTON_3 = pygame.image.load("parcial_2\materiales\menu_boton_3.jpg")
MENU_BOTON_4 = pygame.image.load("parcial_2\materiales\menu_boton_4.jpg")


UBICACION_VOLUMEN = (23,10)

XY_BOTON_FACIL = (160,500)
Z,Q = XY_BOTON_FACIL
XY_BOTON_MEDIO = (Z+200,Q)
XY_BOTON_DIFICIL = (Z+400,Q)


XY_DIFICULTAD = (290,380)
X,Y = XY_DIFICULTAD
XY_TEXTO_DIFICULTAD = (X - 100, Y+10)

    