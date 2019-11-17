import os
# MOSTRAR VALORES
nombre=""
cargo_fijo=0.0
consumo_energia=0.0
alumbrado_publico=0.0
igv=0.0
seguridad_energetica=0.0

# INPUT
nombre=os.sys.argv[1]
cargo_fijo=float(os.sys.argv[2])
consumo_energia=float(os.sys.argv[3])
alumbrado_publico=float(os.sys.argv[4])
igv=float(os.sys.argv[5])
seguridad_energetica=float(os.sys.argv[6])

# PROCESSING
total=(cargo_fijo+consumo_energia+alumbrado_publico+igv+seguridad_energetica)

# VERIFICADOR
pago=(total>25.0)

# OUTPUT
print("####################################")
print("           RECIBO DE LUZ            ")
print("####################################")
print("NOMBRE:", nombre)
print("CARGO FIJO=", cargo_fijo   ,"CONSUMO DE ENERGIA=", consumo_energia)
print("ALUMBRADO PUBLICO=", alumbrado_publico    , "IGV=", igv)
print("SEGURIDAD ENERGETICA=", seguridad_energetica)
print("####################################")
print("CANCELAR=", total)
print("####################################")

# CONDICIONAL DOBLE
# si el total es mayor que 25 consume mucho
if(pago==True):
    print("CONSUME MUCHO")
else:
    print("GRACIAS POR AHORRAR ENERGIA")
# fin_if
