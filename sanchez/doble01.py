import os
# MOSTRAR VALORES
alumno=""
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0

# INPUT
alumno=os.sys.argv[1]
nota1=float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
nota3=float(os.sys.argv[4])
nota4=float(os.sys.argv[5])

# OUTPUT
print(alumno)
print(nota1)
print(nota2)
print(nota3)
print(nota4)

# PROCESSING
promedio=(nota1+nota2+nota4+nota3)/4

# VERIFICADOR
verificador=(promedio>=11.0)

# CONDICION DOBLE
# si el promedio es menor que 11 esta desaprobado y mayor que 15 esta aprobado
if(verificador==True):
    print("esta aprobado")
else:
    print("esta desaprobado")
# fin_if
