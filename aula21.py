# Operadores logicos
# and (e) or (ou) not (nao)
# and - Todas as condicões precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressao inteira será avaliada naquele valor
#Sao considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Tabém existe o tipo None que é usado para representar um não valor


entrada = input ('[E]ntrar  [S]air:')
senha_digitada = input('Senha:')

senha_permitida = '123456'

if  entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')    