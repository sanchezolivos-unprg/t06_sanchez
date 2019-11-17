import os
# MOSTRAR VALORES
restaurante=""
consumidor=""
ceviche=0.0
gaseosa=0.0
arroz_con_pato=0.0
cabrito=0.0

# INPUT
restaurante=os.sys.argv[1]
consumidor=os.sys.argv[2]
ceviche=float(os.sys.argv[3])
gaseosa=float(os.sys.argv[4])
arroz_con_pato=float(os.sys.argv[5])
cabrito=float(os.sys.argv[6])

# PROCESSING
total= (ceviche+gaseosa+arroz_con_pato+cabrito)

# VERIFICADOR
verificador=(total>100.0)

# OUTPUT
print("##########################################")
print("        RESTAURANTE:", restaurante         )
print("##########################################")
print("CONSUMIDOR:", consumidor)
print("##########################################")
print("CEVICHE=", ceviche,      "GASEOSA=", gaseosa)
print("ARROZ CON PATO=", arroz_con_pato)
print("CABRITO=", cabrito)
print("##########################################")
print("total a pagar=", total)

# CONDICION DOBLE
# si el total es mayor a 100 ganaste menu gratis
if(verificador==True):
    print("GANASTE UN MENU GRATIS")
else:
    print("GRACIAS POR VENIR")
# fin_if
