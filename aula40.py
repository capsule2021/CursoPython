""" Calculadora com while """
while True:
    print('nummmmm')
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


# while True:
#     # Input do usuário
#     numero1 = input('Digite um número: ')
#     numero2 = input('Digite outro número: ')
#     operador = input('Digite um operador apenas -> (+-*/) : ')

#     # Checando se os números são válidos
#     try:
#         n1_float = float(numero1)
#         n2_float = float(numero2)
#     except ValueError:
#         print('Por favor, digite números válidos')
#         continue

#     # Checando se o operador é válido
#     operadores_validos = '+-/*'
#     if len(operador) != 1 or operador not in operadores_validos:
#         print('Por favor, digite um operador válido')
#         continue

#     # Realizando as operações
#     if operador == '-':
#         resultado = n1_float - n2_float
#     elif operador == '+':
#         resultado = n1_float + n2_float
#     elif operador == '/':
#         if n2_float == 0:
#             print('Não é possível dividir por zero')
#             continue
#         resultado = n1_float / n2_float
#     elif operador == '*':
#         resultado = n1_float * n2_float

#     print(f'O resultado é: {resultado}')

#     # Sair da calculadora
#     sair = input('Deseja sair da calculadora? [s]im: ').lower().startswith('s')
#     if sair:
#         break
