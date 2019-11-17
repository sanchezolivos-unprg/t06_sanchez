import os
# numero de veces en el cine
# MOSTRAR VALORE
nombre=""
veces_en_cine=0
precio_consume=0.0

# INPUT
nombre=os.sys.argv[1]
veces_en_cine=int(os.sys.argv[2])
precio_consume=float(os.sys.argv[3])

# OUTPUT
print("################################")
print("          cineplanet            ")
print("################################")
print("NOMBRE=", nombre)
print("################################")
print("VECES EN EL CINE=", veces_en_cine)
print("PRECIO QUE CONSUME", precio_consume)
print("################################")

# VERIFICADOR
verificador=(veces_en_cine==precio_consume)

# CONDICION DOBLE
# si la veces en el cine es igual al precio en que consume le gusta las peliculas y come mucho
if(verificador==True):
    print("le gusta las peliculas y come mucho")
else:
    print("asiste muy poco al cine")
# fin_if