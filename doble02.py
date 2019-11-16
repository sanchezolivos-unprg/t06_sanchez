import os
# MOSTRAR VALORES
nombre=""
num_dni=""
edad=0
potencia=0.0
consumo=0.0
interes_monatorio=0.0
cargo_fijo=0.0

# INPUT
nombre=os.sys.argv[1]
num_dni=os.sys.argv[2]
edad=int(os.sys.argv[3])
potencia=float(os.sys.argv[4])
consumo=float(os.sys.argv[5])
interes_monatorio=float(os.sys.argv[6])
cargo_fijo=float(os.sys.argv[7])

# PROCESSING
total=(potencia+consumo+interes_monatorio+cargo_fijo)

# VERIFICADOR
verificador=(total<55.0)

# OUTPUT
print("######################################")
print("               RECIBO                 ")
print("######################################")
print("nombre:", nombre,        "DNI:", num_dni)
print("edad:", edad)
print("######################################")
print("potencia en kw=", potencia)
print("consumo=", consumo)
print("interes monatorio=", interes_monatorio)
print("cargo fijo=", cargo_fijo)
print("######################################")
print("total a pagar=", total)

# CONDICIONAL DOBLE
# si el total es menor que 55 gracias por ahorrar
if(verificador==True):
    print("GRACIAS POR AHORRAR ENERGIA")
else:
    print("CORTE")
# fin_if
