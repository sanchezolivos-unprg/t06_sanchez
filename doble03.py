import os
# MOSTRAR VALORES
radio=0.0

# INPUT
radio=float(os.sys.argv[1])

# PROCESSING
pi= 3.14
volumen= round(4*pi*(radio**3)/3,2)

# VERIFICADOR
verificador=round(volumen>36.0)

# OUTPUT
print("############################")
print("    VOLUMEN DE LA ESFERA    ")
print("############################")
print("RADIO=", radio)
print("############################")
print("          VOLUMEN=", volumen)

# CONDICION DOBLE
# si el volumen es mayor que 36 es muy grande
if(verificador==True):
    print("esfera muy grande")
else:
    print("esfera muy pequeña")
# fin_if