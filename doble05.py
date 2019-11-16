import os
# TRIANGULO COMUN
# MOSTRAR VALORES
base=0.0
haltura=0.0

# INPUT
base=float(os.sys.argv[1])
haltura=float(os.sys.argv[2])

# PROCESSING
area= (base*haltura)/2

# VERIFICADOR
triangulo=(area>=15.5)

# OUTPUT
print("#########################")
print("    TRIANGULO COMUN      ")
print("#########################")
print("BASE=", base)
print("HALTURA=", haltura)
print("#########################")
print("        AREA=", area)

# CONDICION DOBLE
# si el area del triangulo es mayor o igual que 15.5 es un gran triangulo
if(triangulo==True):
    print("es un triangulo grande")
else:
    print("es un triangulo pequeño")
# fin_if