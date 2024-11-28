import pygame
from Constantes import *
from Menu import *
from Juego import *
from Configuraciones import *
from Terminado import *
from Rankings import *

pygame.init()
pygame.display.set_caption("PREGUNTADOS EDICION: DRAGON BALL Z")
icono = ICONO
pygame.display.set_icon(icono)
pygame.display.set_mode(VENTANA_EXPANDIDA,pygame.FULLSCREEN)
pygame.display.set_mode(VENTANA,pygame.RESIZABLE)
pantalla = pygame.display.set_mode(VENTANA)

corriendo = True

reloj = pygame.time.Clock()



datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS_MEDIO,"usuario":"","tiempo":TIEMPO_MEDIO,"volumen_musica":10,"volumen_musica_principal":10}
ventana_actual = "menu"
pygame.mixer.init()

bandera_musica_juego = False
bandera_musica_principal = False
bandera_terminado = False

while corriendo:
    
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)
    
    if ventana_actual == "menu":
        if bandera_musica_juego == True:
            pygame.mixer.music.stop()
            bandera_musica_juego = False
        if bandera_musica_principal == False:
            reproducir_musica("parcial_2\materiales\musica menu prinicpal.mp3",datos_juego["volumen_musica_principal"])
            bandera_musica_principal = True
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_musica_juego == False:
            reproducir_musica("parcial_2\materiales\chala-head-chala-dragon-ball-z.mp3",datos_juego["volumen_musica"])  
            bandera_musica_juego = True
        bandera_musica_principal = False
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
        bandera_musica_principal = False
    elif ventana_actual == "rankings":
        lista_ranking = leer_json("parcial_2\\rankings.json")
        ventana_actual = mostrar_puntuaciones(pantalla,cola_eventos,lista_ranking)
    elif ventana_actual == "terminado":
        ventana_actual = mostrar_juego_terminado(pantalla,cola_eventos,datos_juego)
        
    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()

pygame.quit()
