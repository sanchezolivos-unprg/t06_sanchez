import os
# VALIDOR EN TRIANGULO RECTANGULO
# MOSTRAR VALORES
cat1=0.0
cat2=0.0

# INPUT
cat1=float(os.sys.argv[1])
cat2=float(os.sys.argv[2])

# OUTPUT
print(cat1)
print(cat2)

# PROCESSING
import math
hipotenusa= math.sqrt(cat1**2+cat2**2)
print("hipotenusa=", hipotenusa)

# CONDICIONAL MULTIPLE
# si el la hipotenusa es mayor que 10 es muy grande
if(hipotenusa>10.0 and hipotenusa<20.0):
    print("el triangulo rectangulo es pequeño")

if(hipotenusa>20.0 and hipotenusa<30.5):
    print("el triangulo rectangulo es regular")

if(hipotenusa>=30.5):
    print("el triangulo rectangulo es muy grande")
# fin_if
