"""
Exercício 
Peça ao usuário para digitar seu nome
peca ao usuario para gigitar sua idade
se nome e idade forem digitados:
      
     Exiba:
         Seu nome é {nome}
         Seu nome invertido e {nome invertido}
         Se nome contem (ou nao) espacos
         Seu nome tem {n} letras
         Aprimeira letra do seu nome e {letra}
         A ultima  letra do seu nome é {letra}
         Se nada for digitado em nome ou idade :
           exiba "Desculpa,você deixou campos vazios".
"""
nome = input('Digite o seu nome:')
idade= input('Digite sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')


    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome Nao contem espaços')    

        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome e {nome[0]} ')
        print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')    