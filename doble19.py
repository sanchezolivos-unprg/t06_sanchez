import os
# EJERCICIOS RESUELTOS
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

# VERIFICADOR
ejrcs_resueltos=(total<=75)

# CONDICION SIMPLE
# si el total de ejercisios resueltos es menor o igual que 75 jalaste el curso
if(ejrcs_resueltos==True):
    print("JALASTE EL CURSO")
else:
    print("APROBASTE CON LAS JUSTAS")
# fin_if
