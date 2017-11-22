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
        
    else:
        #print(str(fseparado[num])+"No es Par")
    num+=1
