fichero = open("fichero.txt",'r')
texto_leido=fichero.read()
lista_numeros = texto_leido.split(";") 

cont_pares=0
for num in lista_numeros:
    if int(num)%2==0:
        cont_pares+=1

print("Hay "+str(cont_pares)+" numeros pares gente de clase")
print("Este ejercicio ha sido ofrecido por Kant003 con la colaboracion de DAM del norte")
fichero.close()