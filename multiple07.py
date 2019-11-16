import os
# VALIDORES DE GOLEADORES Y NO GOLEADORES
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

# CONDICION MULTIPLE
# si el jugador anota mas o menos goles tiene su siguiente condicion
if(total_goles>10 and total_goles<15):
    print("NO ESTAS PARA DELANTERO")

if(total_goles>=15 and total_goles<25):
    print("ERES UN NOVATO PRA LOS GOLES")

if(total_goles>25 and total_goles<40):
    print("SIGUE ESFORZANDOTE Y LLEGARAS A SER UN CRACK")

if(total_goles>40 and total_goles<50):
    print("ESTAS ENTRE LOS MEJORES DELATEROS DEL MUNDO")

if(total_goles>=50):
    print("GANEASTE EL PREMIO DEL MAS GOLEADOR DEL MUNDO")
# fin_if
