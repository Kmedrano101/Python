"""
 By Kevin Medrano Ayala
"""
# Obtener el valor de velocidad segun datos proporcionados V = d / t, V = m/s, d=m, t = s
# Importar Librerias
#xfrom typing import type_check_only
import sys
# Variables
velocidad = 0
distancia = 0
tiempo = 0
aux = [0,0]
unidades = ["d","t"]
data = ""

while True:
    print("Calcular la Velocidad\nPresione la tecla 'q' para reiniciar y 'x' para salir")
    while aux[0] == 0:
        if data.lower() == "q": 
            data = ""
            break
        data = str(input("Ingrese la unidad de distancia (m / km): "))
        if data.lower() == "x": sys.exit()
        if data.lower() == "q": break
        if data.lower() == "m" or data.lower() == "km":
            try:
                distancia = float(input(f'Ingrese la distancia en {data.lower()}: '))
            except Exception as e:
                print("Formato o valor no valido!")
                data = "q"  
                break
            aux[0],unidades[0] = 1,data.lower()
        else:
          print("El formato de unidad de distancia no es valido!, vuelva a intertarlo")
    while aux[1]==0:
        if data.lower() == "q":
            data = ""
            break
        data = str(input("Ingrese la unidad de tiempo (h / s): "))
        if data.lower() == "x": sys.exit()
        if data.lower() == "q": break
        if data.lower() == "h" or data.lower() == "s":
            try:
                tiempo = float(input(f'Ingrese el tiempo en {data.lower()}: '))
            except Exception as e:
                print("Formato o valor no valido!")
                data = "q"  
                break
            aux[1],unidades[1] = 1,data.lower()
        else:
          print("El formato de unidad de tiempo no es valido!, vuelva a intertarlo")
    if aux[0]==1 and aux[1]==1:
        if unidades[0]=="km":
            distancia = distancia * 1000
        if unidades[1]=="h":
            tiempo = tiempo * 3600
        # Calcular V segun la formula
        velocidad = "{:.2f}".format(distancia / tiempo)
        print("#################################")
        print(f'La Velocidad obtenida es: {velocidad} m/s')
        print("#################################")
        aux[0],aux[1]=0,0

    
    
    