"""
Ejemplo 4: Uso de funcion lambda
andresvallejoz1991
"""

#Cada elemento de datos, tiene (edad y estaturas)
#Dupla

datos = ((30, 1.79),(25, 1.60),(35, 1.68))
#Dupla en la poscion 2
dato = lambda x: x[2]
#Segunda Dupla en la posicion 1
edad = lambda x: x[1]*100
#Impresion
print(edad(dato(datos)))