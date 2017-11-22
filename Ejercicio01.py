fichero = open("fichero.txt",'r')
fleido=fichero.read()
fseparado = fleido.split(";") 
print (fseparado)

cont=0
num=0
while num < len(fseparado):
    if int(fseparado[num])%2==0:
        #print(str(fseparado[num])+"Es Par")
        cont+=1
    num+=1

contador=str(cont)
print("Hay "+contador+" numeros pares gente de clase")
print("Este ejercicio ha sido ofrecido por Kant003 con la colaboracion de DAM del norte")
fichero.close()