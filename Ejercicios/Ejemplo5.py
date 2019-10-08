"""
Ejemplo 5: Uso de datos de lamba
"""
#Dupla
datos = (
	    (100,170),
	    (200,180),
	    )

anios = lambda x: x[0]#Posicon 0 de la dupla
estatura = lambda x: x[1]#Posicion 1 de la dupla
#Funcion para realizar operaciones 
funciones = lambda x: (anios(x)/12.0, estatura(x)/100)
#Impresion de map y lista
print (list(map(funciones, datos)))
