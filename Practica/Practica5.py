"""
"""
#Importacion de math para realizar las operaciones aritemticas requeridas
import math 
#Se crea un listado de duplas
listado=[(10,2), (8,7), (5,4), (3,11), (10,11)]
#Se recorre unicamente las duplas de la posicion 0
posicion1 = lambda x: x[0]
#Se recorre unicamente las duplas de la posicion 1
posicion2 = lambda x: x[1]
#Creacion de la funcion con la raiz cuadrad y elevado al cubo
#Math.sqrt para la raiz y ** para la potencia
funciones = lambda x: (math.sqrt(posicion1(x)), posicion2(x)**2) 
#Presentacion mediante una lista nueva de los datos con su respectiva operacion 
print(list(map(funciones,listado)))