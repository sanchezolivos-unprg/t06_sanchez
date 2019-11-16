import os
# VALIDOR EN EL PROMEDIO DE 5 NOTAS DE INGLES
# MOSTRAR VALORES
estudiante=""
not1=0.0
not2=0.0
not3=0.0
not4=0.0
not5=0.0

# INPUT
estudiante=os.sys.argv[1]
not1=float(os.sys.argv[2])
not2=float(os.sys.argv[3])
not3=float(os.sys.argv[4])
not4=float(os.sys.argv[5])
not5=float(os.sys.argv[6])

# PROCESSING
promedio=(not1+not2+not4+not5+not3)/5

# OUTPUT
print("##################################")
print("PROMEDIO DE LAS 5 NOTAS DE INGLES ")
print("##################################")
print("ESTUDIANTE:", estudiante)
print("nota 1=", not1)
print("nota 2=", not2)
print("nota 3=", not3)
print("nota 4=", not4)
print("nota 5=", not5)
print("##################################")
print("PROMEDIO=", promedio)

# CONDICION MULTIPLE
# condicion multiple de las notas del curso de ingles
if(promedio>95 and promedio<100):
    print("very good")

if(promedio>90 and promedio<94):
    print("good")

if(promedio>85 and promedio<90):
    print("not bad")

if(promedio>80 and promedio<84):
    print("bad")

if(promedio<80):
    print("very bad")
# fin_if

