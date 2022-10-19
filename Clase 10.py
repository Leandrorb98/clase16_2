def sumar(*args): #args es la conveción, se puede poner lo que quieras, ej: *perro
    acumulador = 0
    if len(args) < 2:
      return 0
    
    for numero in args:
        acumulador += numero
    return acumulador

print(sumar(10,10,10,50))
