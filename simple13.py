import os
# DIFERENCIA DE UN RECTANGULO CON CUADRADO
# MOSTRAR VALORES
lado1=0.0
lado2=0.0

# INPUT
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])

# VERIFICADOR
diferencia=(lado1!=lado2)

# CONDICION SIMPLE
# si ambos lados son diferentes es un rectangulo
if(diferencia==True):
    print(("ES UN RECTANGULO"))
# fin_if
