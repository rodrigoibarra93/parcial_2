import pygame
from Constantes import *
from Funciones import *

pygame.init()


#fondo menu
fondo_menu = escalar_superficie(FONDO_MENU,VENTANA)


#fondo botones
boton_1 = escalar_superficie(MENU_BOTON_1,TAMAÑO_BOTON)
boton_2 = escalar_superficie(MENU_BOTON_2,TAMAÑO_BOTON)
boton_3 = escalar_superficie(MENU_BOTON_3,TAMAÑO_BOTON)
boton_4 = escalar_superficie(MENU_BOTON_4,TAMAÑO_BOTON)


lista_botones = []

for i in range(4):
    boton = {}
    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)
   
def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    
    retorno = "menu"
    
    #Gestion Eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
            print(retorno)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == BOTON_JUGAR:
                        retorno = "juego"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == BOTON_RANKINGS:
                        retorno = "rankings"
                    elif i == BOTON_SALIR:
                        retorno = "salir"
                
    #Actualizacion del juego
    #Dibujar en pantalla
    pantalla.blit(fondo_menu,[0,0])
    
    
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(boton_1,(125,115))
    lista_botones[BOTON_CONFIG]["rectangulo"] = pantalla.blit(boton_2,(125,195))
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(boton_3,(125,275))
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(boton_4,(125,355))

    
    mostrar_texto(boton_1,"JUGAR",(170,22),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(boton_2,"CONFIGURAR",(12,25),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(boton_3,"RANKINGS",(12,20),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(boton_4,"SALIR",(80,20),FUENTE_30,COLOR_NEGRO)
    
    return retorno