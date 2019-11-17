import os
# VALIDOR EN CONSUMO DE GOLOSINAS
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

# OUTPUT
print(catidad_caramelos)
print(precio_caramelo)
print(cantidad_chupetines)
print(precio_chupetin)
print(cantidad_galletas)
print(precio_galleta)
print("total=", consumo)

# CONDICIONAL MULTIPLE
# si el niño consume de acuerdo a las condiciones multiples se cumple que
if(consumo>5 and consumo<15.5):
    print("GRACIAS POR COMPRAR")

if(consumo>15.5 and consumo<30.5):
    print("CASI GANAS")

if(consumo>30.5 and consumo<50.5):
    print("GANATES EL CONSUMO DE GOLOSINAS GRATIS POR UN DIA")

if(consumo>=50.5):
    print("FELICITACIONES GANASTES EL CONSUMO DE GOLOSINAS GRATIS POR DOS DIAS")
# fin_if
