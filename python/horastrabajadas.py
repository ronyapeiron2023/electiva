ht = int(input("digita horas trabajadas"))

tatifa_hora=float(input("digita tarifa"))

if ht > 40 :
   salario =(40*tatifa_hora)+((ht-40)* (2*ht))
   
elif ht == 40 :
    
  salario =(40*tatifa_hora)+((ht-40)* (2*ht))
  
else :
   
   salario =(40*tatifa_hora)+((ht-40)* (2*ht))


print("el salario es ",salario)