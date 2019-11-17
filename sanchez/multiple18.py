import os
# MOSTRAR VALORES
nombre=""
t_grado_fahrenheit=0.0

# INPUT
nombre=os.sys.argv[1]
t_grado_fahrenheit=float(os.sys.argv[2])

# OUTPUT
print("################################")
print("  TEMPERATURA DE UNA PERSONA    ")
print("################################")
print("NOMBRE:", nombre)
print("TEMPERATURA EN GRADO FAHRENHEIT:", t_grado_fahrenheit)
print("################################")

# CONDICION MULTIPLE
# la temperatura de una persona con la siguiente condicion multiple
if(t_grado_fahrenheit>40.0):
    print("peligro de muerte")

if(t_grado_fahrenheit>38.1 and t_grado_fahrenheit<39):
    print("tiene fiebre alta")

if(t_grado_fahrenheit>37.8 and t_grado_fahrenheit<38.0):
    print("tiene fiebre")

if(t_grado_fahrenheit<37.0):
    print("temperatura normal")
# fin_if
