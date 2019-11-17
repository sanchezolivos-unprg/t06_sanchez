import os
# BOLETA DE VENTA
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

# CONDICION MULTIPLE
# si el señor consume poco regular o bastante
if(importe_total<8.5):
    print("vuelva pronto")

if(importe_total>8.5 and importe_total<15.0):
    print("usted tiene combustible gratis por un dia")

if(importe_total>15.0 and importe_total<20.0):
    print("usted tiene combustible gratis por una semana")

if(importe_total>=20.0):
    print("usted tiene combustible gratis por tres semanas")
# fin_if