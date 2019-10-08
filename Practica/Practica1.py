"""
Desarrollar la función anónima que retorne True or False si el número dado es par.
"""

#Ingreso por teclado del numero a evaluar
numero = input("Ingrese el numero: \n")
#Especificar el tipo de dato
numero = int(numero)
#Funcion para realizar una comparacion
impar = lambda numero : numero%2 !=0
#Al final luego de realizar la comparacion se arroja un dato True or False
print(impar(numero)) 




