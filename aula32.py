"""
Faça um programa que peca ao usuario para digitar um numero inteiro,
informe se este múmero é par ou impar.Caso nao digite um numero inteiro,
informe que não é número inteiro.

"""
# entrada = input('Digite um número:')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'  # Corrigido o valor inicial

#     if par_impar:
#         par_impar_texto = 'par'

#         print(f'O número {entrada_int} é {par_impar_texto}')
#     else:
#         print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


# entrada = input('Digite um número: ')
# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

##################################################################################################


"""
Faça um programa que pergunte a hora ao usuario e, baseando no horario
descrito, exiba a saudaçao apropriada. ex:
Bom dia 0-10, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora em números inteiros: ')
# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

"""

##################################################################################################
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos descreva "Seu nome e curto"
se tiver entre 5 e 6 letras, descreva: "Seu nome é normal"; maior que 6 escreva "Seu nome e muito grande".
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')