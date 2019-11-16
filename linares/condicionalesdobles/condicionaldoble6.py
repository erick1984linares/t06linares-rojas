import os
nombre, nota1, nota2, nota3=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#procesing
total=(nota1+nota2+nota3)/3

#verificador
promedio=(total>=17.5)

#output
print("##############################")
print("#unprg")
print("#variables:    cantidad:")
print("nombre:",    nombre)
print("#nota1:",  nota1)
print("#nota2:",  nota2)
print("#nota3:",  nota3)
print("total:",     total)
print("##############################")

#condicion simple
#si el promedio supera 17.5 dar media bece
if ( promedio == True ):
    print("se ha ganado media beca")
else:
    print("necesitas esforzarte mas")
#fin_if
