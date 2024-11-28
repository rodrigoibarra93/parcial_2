import pygame
from Constantes import *
from Funciones import *


pygame.init()


#fondo de pantalla
fondo = escalar_superficie(FONDO_CONFIGURACIONES,VENTANA)

#fodno botones
fondo_facil = escalar_superficie(FONDO_DIFICULTAD_FACIL,TAMAÑO_BOTON_DIFICULTAD)

fondo_medio = escalar_superficie(FONDO_DIFICULTAD_MEDIA,TAMAÑO_BOTON_DIFICULTAD)

fondo_dificil = escalar_superficie(FONDO_DIFICULTAD_DIFICIL,(61,61))



#fondo boton volumen
fondo_suma = escalar_superficie(FONDO_SUMA,TAMAÑO_BOTON_VOLUMEN)

fondo_resta = escalar_superficie(FONDO_RESTA,TAMAÑO_BOTON_VOLUMEN)

#fondo boton volver
fondo_volver = escalar_superficie(FONDO_VOLVER,TAMAÑO_BOTON_VOLVER)



#botones de dificultad
boton_facil = crear_boton(TAMAÑO_BOTON_DIFICULTAD)

boton_medio = crear_boton(TAMAÑO_BOTON_DIFICULTAD)

boton_dificil = crear_boton(TAMAÑO_BOTON_DIFICULTAD)


#boton volumen principal
boton_suma_principal = crear_boton(TAMAÑO_BOTON_VOLUMEN)

boton_resta_principal = crear_boton(TAMAÑO_BOTON_VOLUMEN)

#boton volumen juego
boton_suma = crear_boton(TAMAÑO_BOTON_VOLUMEN)

boton_resta = crear_boton(TAMAÑO_BOTON_VOLUMEN)


#boton volver
boton_volver = crear_boton(TAMAÑO_BOTON_VOLVER)


bandera_facil = False
bandera_medio = False
bandera_dificil = False
def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global fondo
    global fondo_facil
    global fondo_medio
    global fondo_dificil
    global fondo_suma
    global fondo_resta
    global fondo_volver
    global bandera_facil
    global bandera_medio
    global bandera_dificil
    retorno = "configuraciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #volumen musica juego
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] < 100:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] += 5
                else:
                    CLICK_DE_ERROR.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] -= 5
                else:
                    CLICK_DE_ERROR.play()

            #volumen principal
            if boton_suma_principal["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica_principal"] < 100:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica_principal"] += 5
                else:
                    CLICK_DE_ERROR.play()
            elif boton_resta_principal["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica_principal"] > 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica_principal"] -= 5
                else:
                    CLICK_DE_ERROR.play()

            #Dificultad
            if boton_facil["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                datos_juego["vidas"] = CANTIDAD_VIDAS_FACIL
                datos_juego["tiempo"] = TIEMPO_FACIL
                bandera_facil = True
                bandera_medio = False
                bandera_dificil = False
            elif boton_medio["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                datos_juego["vidas"] = CANTIDAD_VIDAS_MEDIO
                datos_juego["tiempo"] = TIEMPO_MEDIO
                bandera_medio = True
                bandera_facil = False
                bandera_dificil = False
            elif boton_dificil["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                datos_juego["vidas"] = CANTIDAD_VIDAS_DIFICIL
                datos_juego["tiempo"] = TIEMPO_DIFICIL
                bandera_dificil = True
                bandera_medio = False
                bandera_facil = False
            #volver al menu
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                
    #Aca pueden usar el get_pressed()
    
    pantalla.blit(fondo,[0,0])
    
    #volumen juego
    boton_resta["rectangulo"] = pantalla.blit(fondo_resta,(250,50))
    boton_suma["rectangulo"] = pantalla.blit(fondo_suma,(470,50))
    mostrar_texto(pantalla,"volumen juego",(320,30),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(fondo_suma,"",UBICACION_VOLUMEN,FUENTE_50,COLOR_BLANCO)
    mostrar_texto(fondo_resta,"",UBICACION_VOLUMEN,FUENTE_50,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica']} %",(350,70),FUENTE_50,COLOR_NEGRO)
    
    #boton volver
    boton_volver["rectangulo"] = pantalla.blit(fondo_volver,(10,10))
    mostrar_texto(fondo_volver,"VOLVER",(10,25),FUENTE_22,COLOR_NEGRO)
    

    #volumen pantalla principal
    mostrar_texto(pantalla,"volumen pantalla principal",(260,170),FUENTE_30,COLOR_NEGRO)
    # mostrar_texto(boton_suma_principal["superficie"],"VOL +",(5,10),FUENTE_22,COLOR_NEGRO)
    # mostrar_texto(boton_resta_principal["superficie"],"VOL -",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica_principal']} %",(350,210),FUENTE_50,COLOR_NEGRO)
    boton_resta_principal["rectangulo"] = pantalla.blit(fondo_resta,(250,200))
    boton_suma_principal["rectangulo"] = pantalla.blit(fondo_suma,(470,200))

   
    #dificultad
    mostrar_texto(pantalla,"Dificultad: ",XY_TEXTO_DIFICULTAD,FUENTE_50,COLOR_NEGRO)
    
    if bandera_facil == True:
        mostrar_texto(pantalla,"Facil",(400,390),FUENTE_50,COLOR_NEGRO)
        
    if bandera_medio == True:
        mostrar_texto(pantalla,"Medio",(400,390),FUENTE_50,COLOR_NEGRO)
        
    if bandera_dificil == True:
        mostrar_texto(pantalla,"Dificil",(400,390),FUENTE_50,COLOR_NEGRO)

    boton_facil["rectangulo"] = pantalla.blit(fondo_facil,XY_BOTON_FACIL)
    boton_medio["rectangulo"] = pantalla.blit(fondo_medio,XY_BOTON_MEDIO)
    boton_dificil["rectangulo"] = pantalla.blit(fondo_dificil,XY_BOTON_DIFICIL)
    mostrar_texto(pantalla,"facil",(150,470),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,"medio",(350,470),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,"dificil",(550,470 ),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,"10 vidas y 120s",(100,440),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,"5 vidas y 90s",(310,440),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,"3 vidas y 60s",(510,440),FUENTE_32,COLOR_NEGRO)


    
    return retorno
