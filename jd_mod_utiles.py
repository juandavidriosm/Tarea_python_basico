import random
import openpyxl
import matplotlib.pyplot as grafico
from getpass import getpass

import jd_mod_excel
import jd_mod_juego
import jd_mod_main

def validarNumero(numero_persona, numero_maquina,rango,modo):
    if numero_persona not in range(1,rango+1):
        if modo == 1:
            print("número inválido, has perdido el juego jugador 1, introduce tu nombre  y serás devuelto al menú principal")
            print()
            nombre = input("Introduce tu nombre: ")
            jd_mod_excel.estadistica_siempre(nombre,0,1)
            print()
            jd_mod_main.adivinaElNumero()
            return False 
            
        elif modo == 2:
            nombre1 = input("Jugador 1, has perdido, introduce tu nombre: ")
            nombre2 = input("Jugador 2, has ganado, introduce tu nombre: ")
            jd_mod_excel.estadistica_siempre(nombre1,0,1)
            jd_mod_excel.estadistica_siempre(nombre2,1,0)
            print()
            jd_mod_main.adivinaElNumero()
            return False 
            
    elif numero_maquina not in range(1,rango+1):
        print("número inválido, ha ganado el jugador 1")
                
        nombre1 = input("Introduce tu nombre jugador 1: ")
        nombre2 = input("Introduce tu nombre jugador 2: ")
        print()
        print("serán devueltos al menú principal")
        print()
        jd_mod_excel.estadistica_siempre(nombre1,1,0)
        jd_mod_excel.estadistica_siempre(nombre2,0,1)
        jd_mod_main.adivinaElNumero()
        return False 
        
def intentosNoQuedan(cantidad,modo):
    print("haz hecho ya " + str(cantidad)+ " intentos, perdiste, introduce tu nombre y serás devuelto al menú principal")
    print()
    nombre = input("Introduce tu nombre: ")
    jd_mod_excel.estadistica_siempre(nombre,0,1) 
    print()
    if modo == 2:
        print("¡Has ganado jugador 2! Introduce tus datos y serán devueltos al menú principal")
        nombre_2 = input("Introduce tu nombre: ")
        jd_mod_excel.estadistica_siempre(nombre_2,1,0)
    jd_mod_main.adivinaElNumero()

        
        
def MostrarMenu1():
    print("elija entre las siguientes opciones, introduzca sólo el número")
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")
def MostrarMenu2():
        print("elija entre las siguientes opciones, introduzca sólo el número")
        print("1. Fácil (20 intentos, rango de números posibles [1,100])")
        print("2. Medio (12 intentos, rango de números posibles [1,500])")
        print("3. Difícil (5 intentos, rango de números posibles [1,1000])")
        
def EligeDifi(dificultad,modoz):
    if dificultad == 1:
        jd_mod_juego.juego(modoz,20,100)
    elif dificultad == 2:
        jd_mod_juego.juego(modoz,12,500)
    elif dificultad == 3:
        jd_mod_juego.juego(modoz,5,1000)
    else:
        print("número inválido, serás devuelto al menú principal")
        print()
        jd_mod_main.adivinaElNumero()