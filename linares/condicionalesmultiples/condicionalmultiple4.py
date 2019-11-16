import os
nombre, fierro, cemento, tubos=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
fierro=int(os.sys.argv[2])
cemento=int(os.sys.argv[3])
tubos=int(os.sys.argv[4])

#procesing
total=(fierro+cemento+tubos)

#verificador
comprador_rentable=(total>=500)

#output
print("##############################")
print("#ferreteri linares")
print("#variables:    cantidad:")
print("nombre:",    nombre)
print("#fierro:",   fierro)
print("#cemento:",  cemento)
print("#tubos:",    tubos)
print("total:",     total)
print("##############################")

#condicion simple
#si es comprador rentable hacerle un descuento
if ( comprador_rentable == True ):
    print("se ha ganado un descuento")
if ( comprador_rentable>=490 and comprador_rentable<500 ):
    print("gane descuentos comprando mas")
if ( comprador_rentable <489 ):
    print("gracias por su compra")
#fin_if
