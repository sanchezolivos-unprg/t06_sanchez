import os
# MOSTRAR VALORES
cliente, producto, precio, cantidad= "", "", 0.0, 0

# INPUT
cliente=os.sys.argv[1]
producto=(os.sys.argv[2])
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

# PROCESSING
monto_total=round(cantidad*precio,2)

# VERIFICADOR
comprador_compulsivo=(monto_total>100)

# OUTPUT
print("###############################")
print("#      BOLETA DE VENTA        #")
print("###############################")
print("# cliente:", cliente)
print("# producto:", producto)
print("# p.u:", precio)
print("# cantidad:", cantidad)
print("# total:", monto_total)
print("###############################")

# CONDICION SIMPLE
# si el comprador es compulsivo mostrarle la tarjeta dorada
if(comprador_compulsivo==True):
    print("GANASTE LA TARJETA DORADA")
# fin_if
