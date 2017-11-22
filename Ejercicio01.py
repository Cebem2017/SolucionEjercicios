try:
    fichero = open("fichero.txt",'r')
except IOError:
    print('No se pudo abrir el fichero')
texto_leido = fichero.read()
lista_numeros = texto_leido.split(";") 

cont_pares = 0
for num in lista_numeros:
    try:
        if int(num) % 2 == 0:
            cont_pares += 1
    except Exception:
        print('Error en la conversión de números')

print("Hay " + str(cont_pares) + " numeros pares gente de clase")
print("Este ejercicio ha sido ofrecido por Kant003 con la colaboracion de DAM del norte")

try:
    fichero.close()
except IOError:
    print('No se pudo cerrar el fichero')