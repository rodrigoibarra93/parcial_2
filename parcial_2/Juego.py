import pygame
import csv
from Funciones import *
from Constantes import *


#inicializamos el juego
pygame.init()

#fondo de pantalla
fondo = escalar_superficie(FONDO_JUEGO,VENTANA)

lista_preguntas = []
leer_csv("parcial_2\Preguntas.csv",lista_preguntas)

#creo las  superficies de la pregunta y las respuestas
mi_superficie_pregunta = escalar_superficie(FONDO_PREGUNTA,TAMAÑO_PREGUNTA)
mi_superficie_respuesta_1 = escalar_superficie(FONDO_RESPUESTA_1,TAMAÑO_RESPUESTA)
mi_superficie_respuesta_2 = escalar_superficie(FONDO_RESPUESTA_2,TAMAÑO_RESPUESTA)
mi_superficie_respuesta_3 = escalar_superficie(FONDO_RESPUESTA_3,TAMAÑO_RESPUESTA)
mi_superficie_respuesta_4 = escalar_superficie(FONDO_RESPUESTA_4,TAMAÑO_RESPUESTA)
mi_superficie_acierto = escalar_superficie(FONDO_ACIERTO,TAMAÑO_RESPUESTA)
mi_superficie_error = escalar_superficie(FONDO_ERROR,TAMAÑO_RESPUESTA)



#Sonidos de click
click_acierto = CLICK_ACIERTO
click_error = CLICK_ERROR

#boton volver
boton_volver = crear_boton(TAMAÑO_BOTON_VOLVER)

#Boton Pasar pregunta
boton_pasa_pregunta = crear_boton(TAMAÑO_BOTON_VOLVER)
boton_pasa_pregunta["superficie"].fill(COLOR_VERDE)
#boton vale x2
boton_vale_x2 = crear_boton(TAMAÑO_BOTON_VOLVER)
boton_vale_x2["superficie"].fill(COLOR_VERDE)


#respuestas
cartas_respuestas = []
for i in range(4):
    carta_respuesta = {}
    carta_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    carta_respuesta["rectangulo"] = carta_respuesta["superficie"].get_rect()
    cartas_respuestas.append(carta_respuesta)
    




#evento de tiempo
evento_1s = pygame.USEREVENT
pygame.time.set_timer(evento_1s,1000)

#extras
indice = 0
mezclar_lista(lista_preguntas)
bandera_respuesta = False
contador_respuestas_correctas = 1
bandera_pasar_pregunta = False
bandera_vale_x2 = 0

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    global mi_superficie_pregunta
    global mi_superficie_respuesta_1
    global mi_superficie_respuesta_2
    global mi_superficie_respuesta_3
    global mi_superficie_respuesta_4
    global mi_superficie_acierto
    global mi_superficie_error
    global contador_respuestas_correctas
    global boton_vale_x2
    global boton_pasa_pregunta
    global bandera_pasar_pregunta
    global bandera_vale_x2
    retorno = "juego"

    pregunta_actual = lista_preguntas[indice]

    if bandera_respuesta:
        mi_superficie_pregunta = escalar_superficie(FONDO_PREGUNTA,TAMAÑO_PREGUNTA)
        mi_superficie_respuesta_1 = escalar_superficie(FONDO_RESPUESTA_1,TAMAÑO_RESPUESTA)
        mi_superficie_respuesta_2 = escalar_superficie(FONDO_RESPUESTA_2,TAMAÑO_RESPUESTA)
        mi_superficie_respuesta_3 = escalar_superficie(FONDO_RESPUESTA_3,TAMAÑO_RESPUESTA)
        mi_superficie_respuesta_4 = escalar_superficie(FONDO_RESPUESTA_4,TAMAÑO_RESPUESTA)
        mi_superficie_acierto = escalar_superficie(FONDO_ACIERTO,TAMAÑO_RESPUESTA)
        mi_superficie_error = escalar_superficie(FONDO_ERROR,TAMAÑO_RESPUESTA)
        pygame.time.delay(500)
        bandera_respuesta = False



    pregunta_actual = lista_preguntas[indice]
    for evento in cola_eventos:


        if evento.type == pygame.QUIT:
            print("SALIENDO")
            retorno = "salir"


        if datos_juego["vidas"] <= 0:
            retorno = "terminado"


        if evento.type == evento_1s:
            print("paso un segundo")
            datos_juego['tiempo']-=1
            if datos_juego["tiempo"] == 0:
                retorno = "terminado"


        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):

                if boton_vale_x2["rectangulo"].collidepoint(evento.pos):
                    if bandera_vale_x2 == 0:
                        CLICK_SONIDO.play()
                        boton_vale_x2["superficie"].fill(COLOR_GRIS)
                        bandera_vale_x2 = 1
                    elif bandera_vale_x2 == 2:
                        CLICK_DE_ERROR.play()
                elif cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                
                    respuesta_seleccionada = (i + 1)
                    print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                    
                        
                    if contador_respuestas_correctas == 5:
                        datos_juego["vidas"]+=1
                        datos_juego['tiempo']+=10
                        contador_respuestas_correctas = 1

                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                        print("RESPUESTA CORRECTA")
                        if bandera_vale_x2 == 1:
                            datos_juego["puntuacion"]+=PUNTUACION_ACIERTO
                            bandera_vale_x2 = 2

                        pantalla.blit(mi_superficie_acierto, cartas_respuestas[i]["rectangulo"])
                        click_acierto.play()
                        contador_respuestas_correctas+=1
                    else:
                        print("RESPUESTA INCORRECTA")
                        pantalla.blit(mi_superficie_error, cartas_respuestas[i]["rectangulo"])
                        contador_respuestas_correctas = 1
                        click_error.play()
                    
                    indice +=1

                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)

                    bandera_respuesta = True
                
                elif boton_pasa_pregunta["rectangulo"].collidepoint(evento.pos):
                    if bandera_pasar_pregunta == False:
                        CLICK_SONIDO.play()
                        mezclar_lista(lista_preguntas)
                        boton_pasa_pregunta["superficie"].fill(COLOR_GRIS)
                        bandera_respuesta = True
                        bandera_pasar_pregunta = True
                    elif bandera_pasar_pregunta == True:
                        CLICK_DE_ERROR.play()
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
                
                        

    pantalla.blit(fondo,[0,0])
    
    #Pregunta
    pantalla.blit(mi_superficie_pregunta,(195,10))
    mostrar_texto(mi_superficie_pregunta,pregunta_actual["pregunta"],(20,20),FUENTE_30,COLOR_NEGRO)
    
    #r1
    pantalla.blit(mi_superficie_respuesta_1,(240,195))
    mostrar_texto(mi_superficie_respuesta_1,pregunta_actual["respuesta_1"],(20,20),FUENTE_25,COLOR_NEGRO)
    cartas_respuestas[0]["rectangulo"] = pantalla.blit(mi_superficie_respuesta_1,(240,195))#r1
    
    #r2
    pantalla.blit(mi_superficie_respuesta_2,(240,265))
    mostrar_texto(mi_superficie_respuesta_2,pregunta_actual["respuesta_2"],(20,20),FUENTE_25,COLOR_NEGRO)
    cartas_respuestas[1]["rectangulo"] = pantalla.blit(mi_superficie_respuesta_2,(240,265))#r2
    
    #r3
    pantalla.blit(mi_superficie_respuesta_3,(240,335))
    mostrar_texto(mi_superficie_respuesta_3,pregunta_actual["respuesta_3"],(20,20),FUENTE_25,COLOR_NEGRO)
    cartas_respuestas[2]["rectangulo"] = pantalla.blit(mi_superficie_respuesta_3,(240,335))#r3

    #4
    pantalla.blit(mi_superficie_respuesta_4,(240,405))
    mostrar_texto(mi_superficie_respuesta_4,pregunta_actual["respuesta_4"],(20,20),FUENTE_25,COLOR_NEGRO)
    cartas_respuestas[3]["rectangulo"] = pantalla.blit(mi_superficie_respuesta_4,(240,405))#r4




    #boton volver
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(700,460))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),FUENTE_22,COLOR_BLANCO)
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,30),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,str(f"Tiempo: {datos_juego['tiempo']}"),(10,50),FUENTE_25,COLOR_NEGRO)

    mostrar_texto(pantalla,"BONUS",(40,200),FUENTE_40,COLOR_NEGRO)
    
    boton_vale_x2["rectangulo"] = pantalla.blit(boton_vale_x2["superficie"],(40,250))
    mostrar_texto(boton_vale_x2["superficie"],"vale x2",(15,15),FUENTE_22,COLOR_NEGRO)

    
    boton_pasa_pregunta["rectangulo"] = pantalla.blit(boton_pasa_pregunta["superficie"],(40,350))
    mostrar_texto(boton_pasa_pregunta["superficie"],"pasar pregunta",(10,10),FUENTE_22,COLOR_NEGRO)


    return retorno