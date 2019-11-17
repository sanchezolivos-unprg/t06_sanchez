import os
# VALIDOR EN LA CLIMATOLOGIA
# MOSTRAR VALORES
clima_grados_cent=0.0
velocidad_viento=0.0

# INPUT
clima_grados_cent=float(os.sys.argv[1])
velocidad_viento=float(os.sys.argv[2])

# PROCESSING
climatologia=(clima_grados_cent+velocidad_viento)

# OUTPUT
print(clima_grados_cent)
print(velocidad_viento)
print("la climatologia es:", climatologia)

# CODICIONAL MULTIPLE
# si la temperatura cumplen las siguientes condiciones multiples seran
if(climatologia>0.0 and climatologia<17.0):
    print("HACE BASTANTE FRIO")

if(climatologia<17.0 and climatologia<24.4):
    print("HACE POCO FRIO")

if(climatologia>24.4 and climatologia<30.8):
    print("HACE POCO CALOR")

if(climatologia>=30.8):
    print("MUCHO CALOR")
# fin_if
