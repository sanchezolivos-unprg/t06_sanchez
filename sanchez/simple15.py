import os
# INGRESO A UNA CUENTA WEB
# MOSTRAR VALORES
usuario=""
contraseña=""

# INPUT
usuario=os.sys.argv[1]
contraseña=os.sys.argv[2]

# OUTPUT
print(usuario)
print(contraseña)

# VERIFICADOR
ingreso=(contraseña=="sr#&op")

# CONDICION SIMPLE
# si el ingreso es verdadero la cuenta ok
if(ingreso==True):
    print("cuenta OK")
# fin_if
