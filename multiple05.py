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

# CONDICION MULTIPLE
# si la condicion cumple los siguientes pasos serian nadies usa luz, consumen poco consumen regular, consumen mucho
if(total<5.5):
    print("nadies usa luz en la casa")

if(total>5.5 and total<15.5):
    print("consumen poco")

if(total>=15.5 and total<25.0):
    print("consumen luz regular")

if(total>25.0):
    print("consumen mucha luz")
# fin_if