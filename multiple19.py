import os
# MOSTRAR VALORES
nombre=""
clave=""

# INPUT
nombre=os.sys.argv[1]
clave=os.sys.argv[2]

# OUTPUT
print("##############################")
print(" ACCESO A LA CUENTA DE GMAIL  ")
print("##############################")
print("NOMBRE:", nombre)
print("CLAVE:", clave)

# CONDICION MULTIPLE
# las credenciales de un servidor en la condicion multiple
if(nombre=="admin" and clave=="12345"):
    print("acceso ok")

if(nombre=="admin" and clave!="12345"):
    print("clave erronea")

if(nombre!="admin" and clave=="12345"):
    print("nombre erroneo")

if(nombre!="admin" and clave!="12345"):
    print("acceso denegado")
# fin_if