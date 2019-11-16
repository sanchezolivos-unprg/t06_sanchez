import os
# VALIDOR DE ASISTENCIAS A CLASES
# MOSTRAR VALORES
estudiante=""
asistencia1=0
asistencia2=0
asistencia3=0
asistencia4=0
asistencia5=0
asistencia6=0
asistencia7=0
asistencia8=0

# INPUT
estudiante=os.sys.argv[1]
asistencia1=int(os.sys.argv[2])
asistencia2=int(os.sys.argv[2])
asistencia3=int(os.sys.argv[2])
asistencia4=int(os.sys.argv[2])
asistencia5=int(os.sys.argv[6])
asistencia6=int(os.sys.argv[6])
asistencia7=int(os.sys.argv[7])
asistencia8=int(os.sys.argv[8])

# OUTPUT
print(estudiante)
print(asistencia1)
print(asistencia2)
print(asistencia3)
print(asistencia4)
print(asistencia5)
print(asistencia6)
print(asistencia7)
print(asistencia8)

# PROCESSING
total=(asistencia1+asistencia2+asistencia3+asistencia4+asistencia5+asistencia6+asistencia7+asistencia8)
print("total de asistencias:", total)

# CONDICIONAL MULTIPLE
# si el condicion multiple son validadas de cumple que
if(total==0):
    print("NUNCA ASISTE")

if(total>15 and total<25):
    print("ASISTE POCAS VECES")

if(total>=25 and total<50):
    print("asistencia regular")

if(total==80):
    print("asistio todos los dias")
# fin_if