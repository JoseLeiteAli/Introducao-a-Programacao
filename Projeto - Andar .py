#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Laço de repetição FOR:
andar=21
for i in range(21):
    andar=andar-1
    if andar ==13:
        continue
    if andar ==0:
        break
    print(andar,"° Andar")


#Laço de repetição WHILE:
andar=21
while(andar>1):
    andar=andar-1
    if(andar == 13):
        continue
    print(andar,"° Andar") 
     

#Laço de repetição FOR:
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar,"° Andar")

