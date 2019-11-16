import os
# AREA DEL TRAPECIO
# MOSTRAR VALORES
base1= 0.0
base2=0.0
haltura=0.0

# INPUT
base1=float(os.sys.argv[1])
base2=float(os.sys.argv[2])
haltura=float(os.sys.argv[3])

# PROCESSING
area=haltura*(base1+base2)/2

# VERIFICADOR
trapecio=(area>12)

# OUTPUT
print("#################################")
print("        AREA DEL TRAPECIO        ")
print("#################################")
print("BASE NENOR=", base1)
print("BASE MAYOR=", base2)
print("HALTURA=", haltura)
print("#################################")
print("AREA=", area)

# CONDICION SIMPLE
# si el trapecio es mayor o igual que 12 es demasiado grande
if(trapecio==True):
    print("demasiado grande")
else:
    print("muy pequeño")
# fin_if
