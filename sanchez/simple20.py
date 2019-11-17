import os
# VENTA DE LOTES
# MOSTRAR VALORES
lugar=""
precio_lote1=0.0
precio_lote2=0.0
precio_lote3=0.0
precio_lote4=0.0
precio_lote5=0.0

# INPUT
lugar=os.sys.argv[1]
precio_lote1=float(os.sys.argv[2])
precio_lote2=float(os.sys.argv[3])
precio_lote3=float(os.sys.argv[4])
precio_lote4=float(os.sys.argv[5])
precio_lote5=float(os.sys.argv[6])

# PROCESSING
total= (precio_lote1+precio_lote2+precio_lote3+precio_lote4+precio_lote5)

# OUTPUT
print("############################################")
print("              VENTA DE LOTES                ")
print("############################################")
print("ubicacion:", lugar)
print("############################################")
print("lote 1=", precio_lote1)
print("lote 2=", precio_lote2)
print("lote 3=", precio_lote3)
print("lote 4=", precio_lote4)
print("lote 5=", precio_lote5)
print("#############################################")
print("total de lotes=", total)

# VERIFICADOR
verificador= (total>100.5)

# CONDICION SIMPLE
# si el total es mayor que 100.500 son demasiado caros
if(verificador==True):
    print("SON DEMASISDOS CAROS")
# fin_if
