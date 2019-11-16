import os
#DECLARAR VARIABLES
largo, ancho, altura=0, 0 ,0

#imput
largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#procesing
volumen=(largo*ancho*altura)

#verificador
comprobando=(volumen>=20)

#output
print("##############################")
print("#volumen de un rectoedro")
print("#variables:                cantidad:")
print("#largo:",                    largo)
print("#ancho:",                    ancho)
print("#altura:",                   altura)
print("#volumen:",                  volumen)
print("##############################")

#condicion simple
#si el volumen supera 20, mostrar volumen es aceptable
if ( comprobando == True):
    print("volumen del rectoedro es aceptable")
if ( comprobando>=18 and comprobando<21 ):
    print("volumen masomenos aceptable")
if ( comprobando<17 ):
    print("volumen no aceptable")
#fin_if
