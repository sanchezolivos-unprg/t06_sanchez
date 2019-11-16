import os
# MOSTRAR VALORES
señor, dni, pu, igv, conumo_gas="", "", 0.0, 0.0, 0.0

# INPUT
señor=os.sys.argv[1]
dni=os.sys.argv[2]
pu=float(os.sys.argv[3])
igv=float(os.sys.argv[4])
conumo_gas=float(os.sys.argv[5])

# PROCESSING
importe_total=(pu+igv+conumo_gas)

# VERIFICADOR
consume_bastante=(importe_total>25)

# OUTPUT
print("#############################")
print(" VOLETA DE VENTA ELECTRONICA ")
print("#############################")
print("SEÑOR:", señor)
print("#############################")
print("CONSUMO DE GAS=", conumo_gas)
print("PRECIO UNITARIO=", pu)
print("IGV=", igv)
print("#############################")
print("IMPORTE TOTAL=", importe_total)

# CONDICIONAL DOBLE
# si el señor consume bastante gana combustible una semana gratis
if(consume_bastante==True):
    print("ganaste conbustible por una semana")
else:
    print("GRACIAS POR CONSUMIR")
# fin_if
