import random
import sys
import os


#PERMITE SELECCIONAR LA LETRA CON LA CUAL JUGARA EL USUARIO
def Seleccion_Letra():
    marcas_jugadores = {1:"X",2:"O"}
    seleccion =""
    while not (seleccion == 1 or  seleccion == 2):
        seleccion = input("Ingrese 1 si Desea seleccionar X u 2 si desea seleccionar O: ")
        while not (seleccion.isdigit()):
            seleccion = input(" Usted no ha ingresado un digito, Ingrese 1 si Desea seleccionar X u 2 si desea seleccionar O: ")
        seleccion = int(seleccion)    


    if (seleccion ==1):
        marcajugador = marcas_jugadores.get(1)
        marcamaquina = marcas_jugadores.get(2)
        print("usted eligio ", marcajugador, "por lo cual la maquina lanzara con ",marcamaquina)
    else:
        marcajugador = marcas_jugadores.get(2)
        marcamaquina = marcas_jugadores.get(1)
        print("usted eligio ", marcajugador, "por lo cual la maquina lanzara con ",marcamaquina)
    return marcajugador , marcamaquina


#DEFINE UNA DICCIONARIO DE POSICIONES
def defposiciones():
    posiciones={1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
    return posiciones


#PINTA EL TABLERO DE JUEGO
def Tablero():
    for pos in range(1,10):
        sys.stdout.write("|" + posicion[pos])
        if (pos%3==0): print("|\n")


#EVALUA SI EXISTE UN GANADOR
def ganador(posiciones2,marca):
    
    if (posiciones2[1] == posiciones2[2] == posiciones2[3] == marca or \
        posiciones2[1] == posiciones2[4] == posiciones2[7] == marca or \
        posiciones2[7] == posiciones2[8] == posiciones2[9] == marca or \
        posiciones2[3] == posiciones2[6] == posiciones2[9] == marca or \
        posiciones2[1] == posiciones2[5] == posiciones2[9] == marca or \
        posiciones2[3] == posiciones2[5] == posiciones2[7] == marca or \
        posiciones2[2] == posiciones2[5] == posiciones2[8] == marca or \
        posiciones2[4] == posiciones2[5] == posiciones2[6] == marca):
        return True
    else:
        return False


#CONTROLA LO RELACIONADO A EL LANZAMIETO DE LA PERSONA
def lanzamiento_Persona():
    valor = input("ingrese la posicion en la cual desea marcar: ")
    while not (valor.isdigit()):
        valor = input(" No ha ingresado un numero entre 1 y 9, ingrese nuevamente la posicion en la cual desea marcar: ")

    valor = int(valor)

    if (posicion.get(valor) == "_"):
        posicion.update({valor:mjugador})
        Tablero()
    else:
        while not (posicion.get(valor) =="_" and valor <= 9 ):
            print("error la posicion ", valor, "se encuentra ocupada , o ", valor, " puede ser un valor superior a 9")
            valor = input("ingrese una posicion valida en la cual desea marcar: ")
            while not (valor.isdigit()):
                valor = input(" No ha ingresado un numero entre 1 y 9, ingrese nuevamente la posicion en la cual desea marcar: ")
            valor = int(valor)
        posicion.update({valor:mjugador})    
        Tablero()


#MANEJA TODA LA IA DEL JUEGO
def lanzamiento_Maquina():
    lista = list(posicion.values())
    lista_vacios= []
    lista_esquinas = []
    seleccion = []
    seleccion2 = []
    seleccion3 = []
    esquinas =[1,3,7,9]
    asignacion = 0

    for pos in esquinas:
        if (lista[pos-1] =="_"):
            lista_esquinas.append(pos)

    for k, v in posicion.items():
        if (posicion.get(k) == "_"):
            lista_vacios.append(k)

    for vacio in lista_vacios:
        posiciones2 = posicion.copy()
        posiciones2.update({vacio:mmaquina})
        if (ganador(posiciones2,mmaquina)):
            seleccion2.append(vacio) 
            posicion.update({seleccion2[0]:mmaquina})
            asignacion +=1

    for vacio in lista_vacios:
        posiciones2 = posicion.copy()
        posiciones2.update({vacio:mjugador})
        if (ganador(posiciones2,mjugador) and asignacion ==0):
            seleccion.append(vacio) 
            posicion.update({seleccion[0]:mmaquina})
            asignacion +=1
 
    if ( len(lista_vacios)<= 9 and asignacion == 0 and len(lista_esquinas)> 0):
        seleccion3.append(random.choice(lista_esquinas))
        posicion.update({seleccion3[0]:mmaquina})

    if( len(lista_vacios) <= 9 and asignacion == 0):
        seleccion3.append(random.choice(lista_vacios))
        posicion.update({seleccion3[0]:mmaquina})

    Tablero()


#CONTROLA LO RELACIONADO A LAS JUGADAS, QUIEN LANZA PRIMERO
def jugada():

    global posicion, mjugador, mmaquina
    conteo = 0
    posicion = defposiciones()
    mjugador, mmaquina = Seleccion_Letra()
    if (mjugador == "X"):
        gag =""
        while not (gag ==True):
            conteo += 1
            print("Lanza el Usuario")
            lanzamiento_Persona()
            if (ganador(posicion, mjugador) == True):
                print("Felicidades usted ha ganado")
                gag = True
                posicion.clear() 
                break

            if ( conteo ==9):
                print("Empte,Juego terminado")
                break

            print("Lanza el Ordenador")
            conteo += 1
            lanzamiento_Maquina()
            if (ganador(posicion, mmaquina)== True):
                print("Oppss el ordenador ha ganado")
                gag = True
                posicion.clear()
                break

            if ( conteo ==9):
                print("Empte, Juego terminado")
                break
                
    else:
        gag =""
        while not (gag ==True):
            conteo += 1
            print("Lanza el Ordenador")
            lanzamiento_Maquina()
            if (ganador(posicion, mmaquina) == True):
                print("Oppss el ordenador ha ganado")
                gag = True
                posicion.clear() 
                break

            if ( conteo ==9):
                print("Empte, Juego terminado")
                break

            print("Lanza el Usuario")
            conteo += 1
            lanzamiento_Persona()
            if (ganador(posicion, mjugador)== True):
                print("Felicidades usted ha ganado")
                gag = True
                posicion.clear()
                break

            if ( conteo ==9):
                print("Empte, Juego terminado")
                break

#CONTROLA EL JUEGO COMO TAL, SI JUEGA DE NUEVO O TERMINA
def juego ():
    print("Bienvenido al juego del  TRIKI o TA-TE-TI")
    print("")
    continuar = 1
    while (continuar == 1):
        jugada()
        continuar = input("Presione 1 si desea Jugar de nuevo, de lo contrario presion cualquier tecla: ")
        if (continuar.isdigit() and int(continuar) ==1 ):
            continuar = int(continuar)
        else:
            break
    print("juego Termiando")

#LLAMA AL JUEGO DEL TATETI

juego()
