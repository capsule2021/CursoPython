# Operadores in e not in
# Strings sao interaveis
# 0 1 2 3 4 5 6
# J o n a t a s 
# -6-5-4-3-2-1

nome = 'Jônatas'
# print(nome[0])
# print(nome[-6])

print('Jônat' in nome)
print('z' in nome)


nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'encontrar nao estar em {nome}')    