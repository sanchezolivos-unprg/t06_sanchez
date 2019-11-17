import os
# MOSTRAR VALORES
largo=0.0
ancho=0.0

# INPUT
largo=float(os.sys.argv[1])
ancho=float(os.sys.argv[2])

# OUTPUT
print(largo)
print(ancho)

# PRECESSING
area=(largo*ancho)

# VERIFICADOR
rectangulo=(area>=20)

# CONDICIONAL DOBLE
# si el area del rectangulo es mayor o igual que 20 es muy grande
if(rectangulo==True):
	print("ES MUY GRANDE")
else:
    print("ES PEQUEÑO")
# fin_if
