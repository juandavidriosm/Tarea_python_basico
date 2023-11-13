import random
import openpyxl
import matplotlib.pyplot as grafico
from getpass import getpass

import jd_mod_excel
import jd_mod_utiles
import jd_mod_main

#Version como quiere el profe
def juego(modo,cantidad,rango):
    
    if modo == 1:
        print("Jugador 1, debes acertar el número que la máquina elija")
        numero_maquina = random.randint(1, rango)
    elif modo == 2:
        print("Jugador 2, debes asegurarte que jugador 1 no acierte tu número")
        print("Jugador 1, debes acertar el número que jugador 2 elija")
        
        numero_maquina = int(getpass("jugador2 elige un número: "))
    
    contador = 0
    while contador < cantidad:

       #se definen los números de ambos jugadores o de la máquina
        if modo == 1:
            numero_tuyo = int(input("jugador1 elige un número: "))
            #numero_maquina = random.randint(1, rango)
        elif modo == 2:
            numero_tuyo = int(input("jugador1 elige un número: "))
            #numero_maquina = int(input("jugador2 elige un número: "))
        
        if jd_mod_utiles.validarNumero(numero_tuyo,numero_maquina,rango,modo) == False:
            break
        
            
       #empieza el juego
        if numero_maquina == numero_tuyo:
            print("¡Ganaste jugador1! Introduce tus datos y serás devuelto al menú principal")
            print()
            nombre = input("Introduce tu nombre: ")
            jd_mod_excel.estadistica_siempre(nombre,1,0)
            if modo == 2:
                print("¡Has perdido jugador 2. Introduce tus datos y serán devueltos al menú principal")
                nombre_2 = input("Introduce tu nombre: ")
                jd_mod_excel.estadistica_siempre(nombre_2,0,1)
            print()
            jd_mod_main.adivinaElNumero()
            break
       
        else:
           
            if numero_maquina > numero_tuyo:
                contador +=1
                print("el número buscado era mayor")
                print()
                if contador == cantidad:
                    jd_mod_utiles.intentosNoQuedan(cantidad,modo)
                    break
            
            elif numero_maquina < numero_tuyo:
                contador +=1
                print("el número buscado era menor")
                print()
                if contador == cantidad:
                    jd_mod_utiles.intentosNoQuedan(cantidad,modo)
                    break
                    
        