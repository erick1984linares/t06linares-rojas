import os
nombre, zapatos, zapatillas, tacones=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
zapatos=int(os.sys.argv[2])
zapatillas=int(os.sys.argv[3])
tacones=int(os.sys.argv[4])

#procesing
total=(zapatos+zapatillas+tacones)

#verificador
comprador_compulsivo=(total>=150)

#output
print("##############################")
print("#bata")
print("#variables:    cantidad:")
print("nombre:",       nombre)
print("#zapatos:",     zapatos)
print("#zapatillas:",  zapatillas)
print("#tacones:",     tacones)
print("total:",        total)
print("##############################")

#condicion simple
#si s comprador compulsivo mostrar la tarjeta dorada
if ( comprador_compulsivo == True ):
    print("se gano la tarjeta dorada")
else:
    print("tiene opcion a la tarjeta platino")
#fin_if
