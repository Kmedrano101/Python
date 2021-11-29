"""
 By Kevin Medrano Ayala
"""
import random

# Obtener los numeros pares e impares de una lista y un diccionario en una  linea de codigo
# Usar random para modificar lista y dicc
# El resultado seleccionar de forma aleatoria 2 elementos
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
b = {"A":2,"B":5,"C":9,"D":7,"E":3,"F":13,"G":16}

# Modificando la lista
a = [x* random.randint(1,10) for x in a]

# Modificando el diccionario
b = {k:v*random.randint(1,10) for k,v in b.items()}

# Lista de pares lista
listaPar = [x for x in a if x%2==0]
print(f'Lista pares {listaPar}')
listaParAle = random.sample(listaPar,2)
print(listaParAle)

# Lista de impares lista
listaImpar = [b for b in a if b%2==1]
print(f'Lista impares {listaImpar}')
listaImparAle = random.sample(listaImpar,2)
print(listaImparAle)

# Lista pares diccionario
diccPar = {k:v for k,v in b.items() if v%2==0}
print(f'Diccionario pares {diccPar.items()}')
diccParAle = random.sample(diccPar.items(),2)
print(diccParAle)

# Lista impares diccionario
diccImpar = {k:v for k,v in b.items() if v%2==1}
print(f'Diccionario impares {diccImpar.items()}')
diccImparAle = random.sample(diccImpar.items(),2)
print(diccImparAle)

# Realizar un sorteo de nombres de forma aleatorio mediante una lista

nombres = ["Kevin M.","Maria T.","Jeniffer G.","Juan R.","Pedro Y."]
nombres.append("Benito H.") # Agregar elemento
nombres.pop(1) # Eliminar elemento
print(nombres)
# Sorteo para x ganadores 0 1 >> 0 * 0.3 + random(0,len(nombres))
n_ganadores = 3
listaGanadores = [x for x in random.sample(nombres,n_ganadores)]
print(listaGanadores)