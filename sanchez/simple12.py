import os
# CONSUMO DE GOLOSINAS
# MOSTRAR VALORES
catidad_caramelos=0
precio_caramelo=0.0
cantidad_chupetines=0
precio_chupetin=0.0
cantidad_galletas=0
precio_galleta=0.0

# INPUT
catidad_caramelos=int(os.sys.argv[1])
precio_caramelo=float(os.sys.argv[2])
cantidad_chupetines=int(os.sys.argv[3])
precio_chupetin=float(os.sys.argv[4])
cantidad_galletas=int(os.sys.argv[5])
precio_galleta=float(os.sys.argv[6])

# PROCESSING
consumo=(catidad_caramelos*precio_caramelo)+(cantidad_chupetines*precio_chupetin)+(cantidad_galletas*precio_galleta)

# VERIFICADOR
niño=(consumo>=50.0)

# CONDICIONAL SIMPLE
# si el niño consume mas o igual de 50 se gana una pelota
if(niño==True):
    print("GANASTE UNA PELOTA")
# fin_if
