import os
nombre, servicio_de_internet, serv_de_telefono, serv_de_cable=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
servicio_de_internet=int(os.sys.argv[2])
serv_de_telefono=int(os.sys.argv[3])
serv_de_cable=int(os.sys.argv[4])

#procesing
total=(servicio_de_internet+serv_de_telefono+serv_de_cable)

#verificador
cliente_potencial=(total>=130)

#output
print("##############################")
print("#servicios movistar")
print("#variables:    cantidad:")
print("nombre:",    nombre)
print("#servicio de internet:", servicio_de_internet)
print("#servicio de telefono:", serv_de_telefono)
print("#servicio de cable:",    serv_de_cable)
print("total:",                 total)
print("##############################")

#condicion simple
#si el total supera los 130 soles mostrarle el servicio de internet 5G de velocidad
if ( cliente_potencial== True ):
    print("tiene posibilidad de adquirir el interne con velocidad 5G")
#fin_if
