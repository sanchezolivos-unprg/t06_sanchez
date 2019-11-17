import os
# MOSTRAR VALORES
comprador=""
num_tickes=0

# INPUT
comprador=os.sys.argv[1]
num_tickes=int(os.sys.argv[2])

# OUTPUT
print("################################")
print(" VENTA DE TICKES EN HAPPYLAND   ")
print("################################")
print("COMPRADOR:", comprador)
print("NUMERO DE TICKETS:", num_tickes)
print("################################")

# CONDICION MULTIPLE
# el numero de tickets obtenidos con condicion multiple
if(num_tickes==150):
    print("GANASTE UN JUGUETE")

if(num_tickes==120):
    print("GANASTE UN CARAMELO")

if(num_tickes>90 and num_tickes<99):
    print("GANASTE UN TICKET")

if(num_tickes<90):
    print("sigue intentando")
# fin_if