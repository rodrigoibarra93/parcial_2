import pygame
from Constantes import *
from Funciones import *
import datetime

pygame.init()


lista_ranking = leer_json("parcial_2\\rankings.json")

#fondo de pantalla
fondo = escalar_superficie(FONDO_TERMINADO,VENTANA)



#fondo donde se escribe el nombre
fondo_caja_texto = escalar_superficie(FONDO_TEXTO_DIFICULTAD,CUADRO_TEXTO_2)

#fondo que donde se muestra la puntuacion
fondo_texto_puntuacion = escalar_superficie(FONDO_TEXTO_PUNTUACION,CUADRO_TEXTO_3)


#caja de texto para escribir
caja_texto = crear_boton(CUADRO_TEXTO_2)

#boton guardar
boton_guardar = crear_boton(TAMAÑO_BOTON_VOLVER)

#fondo del boton guardar
fondo_boton_guardar = escalar_superficie(FONDO_VOLVER,CUADRO_TEXTO_1)



fecha = datetime.datetime.now()
nombre = ""


def mostrar_juego_terminado(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global lista_ranking
    global nombre
    global boton_guardar
    global fecha
    global fondo_caja_texto
    global fondo_texto_puntuacion
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            if boton_guardar["rectangulo"].collidepoint(evento.pos):
                terminar_juego(datos_juego,nombre,lista_ranking,"parcial_2\\rankings.json")
                retorno = "salir"
        if evento.type == pygame.KEYDOWN:
            #letra_presionada = chr(evento.key)
            letra_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            
            if letra_presionada == "space":
                nombre += " "
                
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1] #Me elimina automaticamente el último
                fondo_caja_texto = escalar_superficie(FONDO_TEXTO_DIFICULTAD,CUADRO_TEXTO_2)
                
            if len(letra_presionada) == 1:
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada   
        elif evento.type == pygame.QUIT:
            retorno = "salir"
    
    #imprimo el fondo de pantalla
    pantalla.blit(fondo,(0,0))



    pantalla.blit(fondo_texto_puntuacion,(130,90))
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego['puntuacion']} puntos",(130,100),FUENTE_60,COLOR_NEGRO)

    #escribir el nombre
    caja_texto["rectangulo"] = pantalla.blit(fondo_caja_texto,(270,200))
    mostrar_texto(fondo_caja_texto,nombre,(9,20),FUENTE_40,COLOR_NEGRO)
    mostrar_texto(pantalla,"Nombre:",(270,200),FUENTE_30,COLOR_NEGRO)

    #boton guardar
    boton_guardar["rectangulo"] = pantalla.blit(fondo_boton_guardar,(290,300))
    mostrar_texto(fondo_boton_guardar,"GUARDAR",(40,30),FUENTE_32,COLOR_NEGRO)
    
    
    return retorno
