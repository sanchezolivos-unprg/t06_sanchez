import os
# DIFERENCIA DE UN RECTANGULO CON CUADRADO
# MOSTRAR VALORES
lado1=0.0
lado2=0.0

# INPUT
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])

# OUTPUT
print(lado1)
print(lado2)

# CONDICION MULTIPLE
# en las siguientes condiciones multiples se cumple que
if(lado1!=lado2):
    print("ES UN RECTANGULO")

if(lado1==lado2):
    print("es un cuadrado")

if(lado1>lado2):
    print("es un rectangulo vertical")

if(lado1<lado2):
    print("es un rectangulo horizontal")
# fin_if
