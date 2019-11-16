import os
# INSTRUMENTOS MUSICALES
# MOSTRAR VALORES
nombre=""
cantidad_guitarras=0
cantidad_tambores=0
cantidad_baterias=0
cantidad_microfonos=0

# INPUT
nombre=os.sys.argv[1]
cantidad_guitarras=int(os.sys.argv[2])
cantidad_tambores=int(os.sys.argv[3])
cantidad_baterias=int(os.sys.argv[4])
cantidad_microfonos=int(os.sys.argv[5])

# OUTPUT
print(nombre)
print(cantidad_guitarras)
print(cantidad_tambores)
print(cantidad_baterias)
print(cantidad_microfonos)

# PROCESSING
cantidad_total=(cantidad_guitarras+cantidad_tambores+cantidad_baterias+cantidad_microfonos)

# VERIFICADOR
verificador=(cantidad_total>21)

# CONDICION SIMPLE
# si la cantidad total de instrumentos es mayor que 21 pertenece a una banda musical
if(verificador==True):
    print("perteneces a una banda musical")
else:
    print("no tienes una banda musical")
# fin_if
