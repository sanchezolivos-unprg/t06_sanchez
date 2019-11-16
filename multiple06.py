import os
# AREA DEL RECTANGULO
# MOSTRAR VALORES
largo=0.0
ancho=0.0

# INPUT
largo=float(os.sys.argv[1])
ancho=float(os.sys.argv[2])

# PRECESSING
area=(largo*ancho)

# OUTPUT
print(largo)
print(ancho)
print("el area es", area)

# CONDICION SIMPLE
# si el area del rectangulo son menores o mayores que los argumentos dados
if(area>7.5 and area<20.5):
	print("ES PEQUEÑO")

if(area>=20.5 and area<30.0):
    print("EL AREA DEL RECTANGULO ES REGULAR")

if(area>30.0 and area<40.8):
    print("EL AREA DEL RECTANGULO ES GRANDE")

if(area>=40.8):
    print("EL AREA ES MUY GRANDE")
# fin_if
