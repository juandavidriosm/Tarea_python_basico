import random
import openpyxl
import matplotlib.pyplot as grafico
from getpass import getpass

import jd_mod_excel
import jd_mod_utiles
import jd_mod_juego
import jd_mod_main

# celda principal cambiada
def adivinaElNumero():
    
    jd_mod_excel.estadistica_1()
    jd_mod_utiles.MostrarMenu1()
    eleccion = int(input())
    
    if eleccion == 1:
        jd_mod_utiles.MostrarMenu2()

        difi = int(input())
        jd_mod_utiles.EligeDifi(difi,1)
   

    elif eleccion == 2:
        jd_mod_utiles.MostrarMenu2()
        
        difi = int(input())
        jd_mod_utiles.EligeDifi(difi,2)

                        
    elif eleccion == 3:
        
        jd_mod_excel.mostrar_estadistica()
        print()
        adivinaElNumero()
        
        
        
    
    elif eleccion == 4:
        print("Has salido del juego")
        return 
        
        
        
    else:
        print("número inválido, serás devuelto al menú principal")
        print()
        adivinaElNumero()
      
    
#adivinaElNumero()