import os
# validor AL INGRESO A UNA CUENTA WEB
# MOSTRAR VALORES
usuario=""
contraseña=""

# INPUT
usuario=os.sys.argv[1]
contraseña=os.sys.argv[2]

# OUTPUT
print(usuario)
print(contraseña)

# CONDICIONES MULTIPLES
# si las siguientes condicion multiple son validadas se cumple que
if(usuario=="damian" and contraseña=="$%srt"):
    print("cuenta OK")

if(usuario=="damian" and contraseña=="tortuga"):
    print("contraseña denegada")

if(usuario=="guzman" and contraseña=="$%srt"):
    print("usuario denegado")
# fin_if
