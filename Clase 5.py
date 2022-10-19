a=[]

num=int(input("Cuantos numeros quiere ingresar? " ))
while len(a)<num:
    i=int(input("ingrese los valores: "))
    a.append(i)
x=sum(a)
y=len(a)
media_aritmetica=x/y
print(f"la media aritmetica es:{media_aritmetica}")


    
        
