import os
# MOSTRAR VALORES
nota1= 0.0
nota2= 0.0
nota3= 0.0
nota4= 0.0
nota5= 0.0

# INPUT
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])
nota5=float(os.sys.argv[5])

# PROCESSING
promedio=(nota1+nota2+nota3+nota4+nota5)/5

print(nota1)
print(nota2)
print(nota3)
print(nota4)
print(nota5)

# VERIFICADOR
promedio_alto=(promedio>50)

# CONDICION DOBLE
# si el promedio es mayor que 50 estara aprobado
if(promedio_alto==True):
    print("aprobado")
else:
    print("desaprobado")
# fin_if
