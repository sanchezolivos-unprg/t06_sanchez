import os
# GOLEADORES DEL FUTBOL
# MOSTRAR VALORES
jugador=""
goles_liga=0
goles_copa=0
goles_supercopa=0
goles_champions=0

# INPUT
jugador=os.sys.argv[1]
goles_liga=int(os.sys.argv[2])
goles_copa=int(os.sys.argv[3])
goles_supercopa=int(os.sys.argv[4])
goles_champions=int(os.sys.argv[5])

# PROCESSING
total_goles=(goles_liga+goles_copa+goles_supercopa+goles_champions)/1.5

# VERRIFICADOR
goleador=(total_goles>=50)

# OUTPUT
print("#############################")
print("   CAMPEONATO DE FUTBOL      ")
print("JUGADOR:", jugador)
print("GOLES LIGA=", goles_liga)
print("GOLES COPA=", goles_copa)
print("GOLES SUPERCOPA=", goles_supercopa)
print("GOLES CHAMPIONS LEAGUE=", goles_champions)
print("#############################")
print("GOLES EN TOTAL=", total_goles)
print("############################")

# CONDICIONAL DOBLE
# si el jugador anota mas o igual de 48 es un goleador
if(goleador==True):
    print("FELICITACIONNES ERES UN GOLEADOR")
else:
    print("ENTRENA MAS")
# fin_if
