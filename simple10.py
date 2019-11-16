import os
# CLIMATOLOGIA
# MOSTRAR VALORES
clima_grados_cent=0.0
velocidad_viento=0.0

# INPUT
clima_grados_cent=float(os.sys.argv[1])
velocidad_viento=float(os.sys.argv[2])

# PROCESSING
climatologia=(clima_grados_cent+velocidad_viento)

# VERIFICADOR
temperatura=(climatologia<17)

# CODICIONAL SIMPLE
# si la temperatura del lugar es menor que 17 hace bastante frio
if(temperatura==True):
    print("HACE BASTANTE FRIO")
# fin_if
