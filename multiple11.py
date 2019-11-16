import os
# VALIDORES EN EJERCICIOS RESUELTOS
# MOSTRAR VALORES
ejrs1, ejrs2, ejrs3, ejrs4, ejrs5, ejrs6, ejrs7, ejrs8=0, 0, 0, 0, 0, 0, 0, 0

# INPUT
ejrs1=int(os.sys.argv[1])
ejrs2=int(os.sys.argv[2])
ejrs3=int(os.sys.argv[3])
ejrs4=int(os.sys.argv[4])
ejrs5=int(os.sys.argv[5])
ejrs6=int(os.sys.argv[6])
ejrs7=int(os.sys.argv[7])
ejrs8=int(os.sys.argv[8])

# PROCESSING
total=(ejrs1+ejrs2+ejrs3+ejrs4+ejrs5+ejrs6+ejrs7+ejrs8)

# OUTPUT
print(ejrs1)
print(ejrs2)
print(ejrs3)
print(ejrs4)
print(ejrs5)
print(ejrs6)
print(ejrs7)
print(ejrs8)
print("total=", total)

# CONDICION MULTIPLE
# si el total de ejercisios resueltos es menor o igual que 105 jalaste el curso
if(total>5 and total<100):
    print("JALASTE EL CURSO")

if(total>100 and total<150):
    print("tienes otra portunidad de aprobar")

if(total>150):
    print("FELICITACIONES APROBASTE EL CURSO")
# fin_if
