import os
# MOSTRAR VALORES
atleta=""
pes_antes_entr=0
pes_despues_entr=0

# INPUT
atleta=os.sys.argv[1]
pes_antes_entr=int(os.sys.argv[2])
pes_despues_entr=int(os.sys.argv[3])

# PROCESSING
diferencia_pes=(pes_antes_entr-pes_despues_entr)

# OUTPUT
print("#############################################")
print("ATLETA:", atleta)
print("#############################################")
print("peso antes del entrenamiento=", pes_antes_entr)
print("peso despues del entrenamiento=", pes_despues_entr)
print("diferencia del peso es=", diferencia_pes)
print("#############################################")

# CONDICION MULTIPLE
# validando a traves del condicion multiple la diferencia del peso de un atleta
if(diferencia_pes>5):
    print("EXCELENTE")

if(diferencia_pes>3 and diferencia_pes<5):
    print("BIEN")

if(diferencia_pes<3):
    print("DEBE ENTRENAR MAS")
# fin_if
