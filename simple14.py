import os
# HALTURA DE UNA PERSONA
nombre, masa, mc="", 0.0, 0.0

# INPUT
nombre=os.sys.argv[1]
masa=float(os.sys.argv[2])
mc=float(os.sys.argv[3])

# PROCESSING
haltura=(masa*mc)/2

# VERIFICADOR
validez=(haltura<=160.0)

# CONDICION SIMPLE
# si su haltura es menor o igual a 160 es chato
if(validez==True):
    print("ES CHATO")
# fin_if