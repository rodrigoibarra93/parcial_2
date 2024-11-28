import pygame 
from Constantes import *
from Funciones import *

pygame.init()

#fondo ventana
fondo = escalar_superficie(FONDO_RANKING,VENTANA)

#fondo boton volver
fondo_volver = escalar_superficie(FONDO_VOLVER,TAMAÑO_BOTON_VOLVER)


#boton volver
boton_volver = crear_boton(TAMAÑO_BOTON_VOLVER)



def mostrar_puntuaciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_ranking):
    global fondo
    global fondo_volver
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
        
    
    lista_ranking_top_10 = obtener_top_10(lista_ranking)

    pantalla.blit(fondo,[0,0])

    boton_volver["rectangulo"] = pantalla.blit(fondo_volver,(10,10))
    mostrar_texto(fondo_volver,"VOLVER",(10,25),FUENTE_22,COLOR_NEGRO)


    mostrar_texto(pantalla,"NOMBRE",(50,100),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,"PUNTUACION",(220,100),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,"TIEMPO",(450,100),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,"FECHA",(620,100),FUENTE_32,COLOR_NEGRO)


    #1
    mostrar_texto(pantalla,lista_ranking_top_10[0]["nombre"],(60,150),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[0]["puntuacion"]),(280,148),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[0]["tiempo"])+"s",(480,148),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[0]["fecha"],(625,148),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,168),(800,168))

    #2
    mostrar_texto(pantalla,lista_ranking_top_10[1]["nombre"],(60,190),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[1]["puntuacion"]),(280,188),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[1]["tiempo"])+"s",(480,188),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[1]["fecha"],(625,188),FUENTE_25,COLOR_NEGRO)
    
    pygame.draw.line(pantalla,COLOR_NEGRO,(0,208),(800,208))

    #3
    mostrar_texto(pantalla,lista_ranking_top_10[2]["nombre"],(60,230),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[2]["puntuacion"]),(280,228),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[2]["tiempo"])+"s",(480,228),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[2]["fecha"],(625,228),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,248),(800,248))

    #4
    mostrar_texto(pantalla,lista_ranking_top_10[3]["nombre"],(60,270),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[3]["puntuacion"]),(280,268),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[3]["tiempo"])+"s",(480,268),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[3]["fecha"],(625,268),FUENTE_25,COLOR_NEGRO)
    
    pygame.draw.line(pantalla,COLOR_NEGRO,(0,288),(800,288))

    #5
    mostrar_texto(pantalla,lista_ranking_top_10[4]["nombre"],(60,310),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[4]["puntuacion"]),(280,308),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[4]["tiempo"])+"s",(480,308),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[4]["fecha"],(625,308),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,328),(800,328))

    #6
    mostrar_texto(pantalla,lista_ranking_top_10[5]["nombre"],(60,350),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[5]["puntuacion"]),(280,348),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[5]["tiempo"])+"s",(480,348),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[5]["fecha"],(625,348),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,368),(800,368))

    #7
    mostrar_texto(pantalla,lista_ranking_top_10[6]["nombre"],(60,390),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[6]["puntuacion"]),(280,388),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking[6]["tiempo"])+"s",(480,388),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking[6]["fecha"],(625,388),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,408),(800,408))

    #8
    mostrar_texto(pantalla,lista_ranking_top_10[7]["nombre"],(60,430),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[7]["puntuacion"]),(280,428),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[7]["tiempo"])+"s",(480,428),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[7]["fecha"],(625,428),FUENTE_25,COLOR_NEGRO)


    pygame.draw.line(pantalla,COLOR_NEGRO,(0,448),(800,448))

    #9
    mostrar_texto(pantalla,lista_ranking_top_10[8]["nombre"],(60,470),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[8]["puntuacion"]),(280,468),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[8]["tiempo"])+"s",(480,468),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[8]["fecha"],(625,468),FUENTE_25,COLOR_NEGRO)

    pygame.draw.line(pantalla,COLOR_NEGRO,(0,488),(800,488))

    #10
    mostrar_texto(pantalla,lista_ranking_top_10[9]["nombre"],(60,510),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[9]["puntuacion"]),(280,508),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(lista_ranking_top_10[9]["tiempo"])+"s",(480,508),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,lista_ranking_top_10[9]["fecha"],(625,508),FUENTE_25,COLOR_NEGRO)
    
    return retorno