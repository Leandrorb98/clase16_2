año_de_nacimiento=int(input("año de nacimiento: "))
if año_de_nacimiento>=1920 and año_de_nacimiento<= 1940:
    print("Generacion silenciosa")
elif año_de_nacimiento>=1946 and año_de_nacimiento<=1964:
    print("Baby boomer")
elif año_de_nacimiento>=1965 and año_de_nacimiento<=1979:
    print("Generacion X")
#tambien se puede colocar la variable entre dos valores, para no tener que usar el and

elif 1980<=año_de_nacimiento<=2000:
    print("Generacion Y")
elif 2001<=año_de_nacimiento<=2010:
    print("Generacion Z")
#si no pertenece a ninguna generacion:
else: print(f"No existe generacion asociada a su año de nacimiento:{año_de_nacimiento}")
