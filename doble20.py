import os
# HALTURA DE UNA PERSONA
nombre, masa, mc="", 0.0, 0.0

# INPUT
nombre=os.sys.argv[1]
masa=float(os.sys.argv[2])
mc=float(os.sys.argv[3])

# PROCESSING
haltura=(masa*mc)/2

# OUTPUT
print(nombre)
print(masa)
print(mc)

# VERIFICADOR
validez=(haltura<=158.5)

# CONDICION DOBLE
# si su haltura es menor o igual a 158.5 es chato
if(validez==True):
    print("ES CHATO")
else:
    print("HALTURA NORMAL")
# fin_if
