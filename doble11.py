import os
# MOSTRAR VALORES
nombre=""
idiomas=0

# INPUT
nombre=os.sys.argv[1]
idiomas=int( os.sys.argv[2])

# OUTPUT
print(nombre)
print(idiomas)

# VERIFICADOR
cantidad_idiomas=(idiomas>3)

# CONDICION DOBLE
# si sabe mas de 3 idiiomas es inteligente
if(cantidad_idiomas==True):
    print("eres muy inteligente")
else:
    print("sabes pocos idiomas")
# fin_if
