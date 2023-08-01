while True:
    nome = str(input('Digite o seu nome completo: '))
    
    try:
        a_nasc = int(input('Digite o ano do seu nascimento: '))
        if (a_nasc<1922) or (a_nasc>2021):
            print('Ano inválido, por favor digite novamente.')
        else:
            print(f'Seu nome é {nome}, e você completará {2023-a_nasc} anos em 2023!')
            break
        
    except ValueError:
            print('Caracteres inválidos, por favor digite novamente.')
        
   
    
            
    
    
            
