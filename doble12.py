import os
# TRIANGULO RECTANGULO
# MOSTRAR VALORES
cat1=0.0
cat2=0.0

# INPUT
cat1=float(os.sys.argv[1])
cat2=float(os.sys.argv[2])

# PROCESSING
import math
hipotenusa= math.sqrt(cat1**2+cat2**2)

# OUTPUT
print(cat1)
print(cat2)

# VERIFICADOR
triangulo=(hipotenusa>6.0)

# CONDICIONAL DOBLE
# si el la hipotenusa es mayor que 6 es muy grande
if(triangulo==True):
    print("ES GRANDE")
else:
    print("ES PEQUEÑO")
# fin_if
