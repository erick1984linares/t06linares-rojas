import os
nombre, samsung, iphone, LG=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
samsung=int(os.sys.argv[2])
iphone=int(os.sys.argv[3])
LG=int(os.sys.argv[4])

#procesing
total=(samsung+iphone+LG)

#verificador
comprador_potencial=(total>=5000)

#output
print("##############################")
print("#distribuidor de celulares")
print("#variables:    cantidad:")
print("nombre:",    nombre)
print("#samsung:",  samsung)
print("#iphone:",   iphone)
print("#LG:",       LG)
print("total:",     total)
print("##############################")

#condicion simple
#si el el total supera 5000 regalar una tarjeta para google play
if ( comprador_potencial== True ):
    print("se ha ganado una tarjeta para google play")
#fin_if
