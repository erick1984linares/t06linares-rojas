import os
precio_de_polos, precio_de_pantalones, precio_de_chompas=0, 0 ,0

#imput
precio_de_polos=int(os.sys.argv[1])
precio_de_pantalones=int(os.sys.argv[2])
precio_de_chompas=int(os.sys.argv[3])

#procesing
total=(precio_de_polos+precio_de_polos+precio_de_chompas)

#verificador
comprobando=(total>=100)

#output
print("##############################")
print("#RIPLEY")
print("#variables:                cantidad:")
print("precio de polos:",         precio_de_polos)
print("#precio de pantalones:",   precio_de_pantalones)
print("#precio de chompas:",      precio_de_chompas)
print("#total:",                  total)
print("##############################")

#condicion simple
#si el total supera los 100 soles, regalar un descuento adicional
if ( comprobando == True ):
    print("usted se gano un descuento adicional")
else:
    print("gracias por su compra")
#fin_if
