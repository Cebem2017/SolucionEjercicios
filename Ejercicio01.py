fichero = open("fichero.txt",'r')
fleido=fichero.read()
fseparado = fleido.split(";") 
print (fseparado)

cont=0
num=0
while num < len(fseparado):
    if((fseparado[num]%2)==0):
        print(fseparado[num]+"Es Par")
        cont+=1
        
    else:
        print(fseparado[num]+"No es Par")
    num+=1

print("HAY "+cont+" PARES")