import os
# VALIDORES EN LOS VIDEOJUEGOS
# MOSTRAR VALORES
gamer=""
t_play1=0
t_play2=0
t_play3=0
t_play4=0

# INPUT
gamer=os.sys.argv[1]
t_play1=int(os.sys.argv[2])
t_play2=int(os.sys.argv[3])
t_play3=int(os.sys.argv[4])
t_play4=int(os.sys.argv[5])

# PROCESSING
tiempo_total=(t_play1+t_play2+t_play3+t_play4)/2

# OUTPUT
print(gamer)
print(t_play1)
print(t_play2)
print(t_play3)
print(t_play4)
print("horas jugadas:", tiempo_total)

# CONDICION MULTIPLE
# si el tiempo total es mayor o igual cumplen las sgts condiciones
if(tiempo_total>1 and tiempo_total<3):
    print("no le gusta jugar mucho al play")

if(tiempo_total>3 and tiempo_total<5):
    print("es un jugador que ama los videojuegos")

if(tiempo_total>5 and tiempo_total<8):
    print("es un vicioso en los videojuegos")

if(tiempo_total>8):
    print("es muy vicioso")
# fin_if
