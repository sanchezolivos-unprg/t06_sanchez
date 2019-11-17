import os
# LA FUERZA ELECTRICA
# MOSTRAR VALORES
Q1=0.0
Q2=0.0
distancia_metros=0

# INPUT
Q1=float(os.sys.argv[1])
Q2=float(os.sys.argv[2])
distancia_metros=int(os.sys.argv[3])

# PROCESSING
fuerza_electrica=(Q1*Q2*9)/distancia_metros**2

# VERIFICADOR
verificador=(fuerza_electrica>300)

# CONDICION DOBLE
# si la fuerza electrica es mayor que 300 las cargas estan muy cargadas
if(verificador==True):
    print("las cargas estan muy cargadas")
else:
    print("sus cargas son muy bajos")
# fin_if
