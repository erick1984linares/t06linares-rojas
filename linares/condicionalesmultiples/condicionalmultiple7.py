import os
nombre, refrijeradora, televisor, lavadora=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
refrijeradora=int(os.sys.argv[2])
televisor=int(os.sys.argv[3])
lavadora=int(os.sys.argv[4])

#procesing
total=(refrijeradora+televisor+lavadora)

#verificador
comprador_potencial=(total>=2000)

#output
print("##############################")
print("#tiendas EFE")
print("#variables:    cantidad:")
print("nombre:",          nombre)
print("#refrijeradora:",  refrijeradora)
print("#televisor:",      televisor)
print("#lavadora:",       lavadora)
print("total:",           total)
print("##############################")

#condicion simple
#si el el total supera 2000 regalar una olla arrocera
if ( comprador_potencial== True ):
    print("se ha ganadouna olla arrocera")
if ( comprador_potencial>=1900 and comprador_potencial<2000 ):
    print("gana premios comprando masproductos aqui")
if ( comprador_potencial<1890):
    print("gracias por su compra")
#fin_if
