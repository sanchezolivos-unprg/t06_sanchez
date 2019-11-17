import os
# EXCESO DE LOS VIDEOJUEGOS
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

# VERIFICADOR
tiempo_exceso=(tiempo_total>=8)

# CONDICION SIMPLE
# si el tiempo total e mayor o igual que 8 es un vicioso
if(tiempo_exceso==True):
    print("ERES MUY VICIOSO")
# fin_if
