while True:
    opcao=int(input("Escolha a opção desejada:"
          '\n[1] Soma'
          '\n[2] Subtração'
          '\n[3] Multiplicação'
          '\n[4] Divisão'
          '\n[0] Sair'
          '\nOpção: '))
    
    
    if opcao == 0:
        print('Até a próxima!')
        break

    if opcao not in [1,2,3,4]:
        print('Opção inexistente!')
        continue
    
    try:
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
    except ValueError:
        print('Valores inválidos, Digite números válidos.')
    
    if opcao == 1:
        print('O resultado da soma entre os números é:', n1 + n2)
   
    elif opcao == 2:
        print('O resultado da subtração entre os números é:', n1 - n2)
  
    elif opcao == 3:
        print('O resultado da multiplicação entre os números é:', n1 * n2)
  
    elif opcao == 4:
        if n2 != 0:
            print('O resultado da divisão entre os números é:', n1 / n2)
        else:
            print('Erro: Divisão por zero não é permitida!')

    elif opcao == 0:
        print('Até a próxima!')
        break