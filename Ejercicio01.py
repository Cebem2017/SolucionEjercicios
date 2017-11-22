fichero = open("fichero.txt",'r')
fleido=fichero.read()
fseparado = fleido.split(";") 
print (fseparado)

num=0
while num < len(fseparado):
    if((fseparado[num]%2)==0):
        print(fseparado[num]+"Es Par")
        
    else:
        print(fseparado[num]+"No es Par")