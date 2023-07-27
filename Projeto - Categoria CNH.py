rodas = int(input("Informe quantas rodas há no veículo: "))
peso = int(input("Informe o peso bruto do veículo: "))
q_pessoas = int(input("Informe quantas pessoas o veículo acomoda: "))

if rodas<=3:
    print("A melhor categoria de habilitação para dirigir o veículo informado é a categoria A")

elif rodas==4 and q_pessoas<=8 and peso<=3500:
    print("A melhor categoria de habilitação para dirigir o veículo informado é a categoria B")

elif rodas>=4 and peso>3500 and peso<=6000:
    print("A melhor categoria de habilitação para dirigir o veículo informado é a categoria C")

elif rodas>=4 and q_pessoas>8:
    print("A melhor categoria de habilitação para dirigir o veículo informado é a categoria D")

elif rodas>=4 and peso>6000:
    print("A melhor categoria de habilitação para dirigir o veículo informado é a categoria E")
