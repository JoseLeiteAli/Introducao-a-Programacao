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

