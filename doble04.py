import os
# CALCULO DEL VOLUMEN DEL CILINDRO RECTO
# MOSTRAR VALORES
area_base=0.0
haltura=0.0

# INPUT
area_base=float(os.sys.argv[1])
haltura=float(os.sys.argv[2])

# PROCESSING
volumen=(area_base*haltura)

# VERIFICADOR
verificador=(volumen>55.0)

# OUTPUT
print("##########################################")
print("       VOLUMEN DEL CILINDRO RECTO         ")
print("##########################################")
print("AREA DE LA BASE=", area_base)
print("HALTURA=", haltura)
print("##########################################")
print("VOLUMEN=", volumen)

# CONDICION DOBLE
# si el volumen es mayor que 55 es muy profundo
if(verificador==True):
    print("es muy profundo")
else:
    print("no esta profundo")
# fin_if
