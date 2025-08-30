numero01 = float (input ("litros: "))
numero02 = float (input("quilometragem: ")) 

litrosporkm = numero01 / numero02 

print(f"LITROS POR KM: {litrosporkm}")

etanol = litrosporkm * 0.70

print (f"ETANOL: {etanol}")