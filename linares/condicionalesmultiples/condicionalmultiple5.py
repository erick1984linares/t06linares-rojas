import os
nombre, precio1, precio2, precio3=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
precio1=int(os.sys.argv[2])
precio2=int(os.sys.argv[3])
precio3=int(os.sys.argv[4])

#procesing
total=(precio1+precio2+precio3)

#verificador
comprobando=(total>=50)

#output
print("##############################")
print("#negocios linares")
print("#variables:    cantidad:")
print("nombre:",    nombre)
print("#precio1:",  precio1)
print("#precio2:",  precio2)
print("#precio3:",  precio3)
print("total:",     total)
print("##############################")

#condicion simple
#si supera los 50 soles regalar un plato
if ( comprobando == True ):
    print("se ha ganado un plato")
if ( comprobando>=40 and comprobando<50 ):
    print("gracias por su compra, vuelva pronto")
if ( comprobando<=39 ):
    print("gracias")
#fin_if
