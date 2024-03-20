import random

def gerar_cpf():
    # Gerando os nove primeiros dígitos do CPF de forma aleatória
    nove_digitos = [random.randint(0, 9) for _ in range(9)]

    # Calculando o primeiro dígito verificador
    contador_regressivo_1 = 10
    resultado_digito_1 = sum(digito * contador_regressivo_1 for digito, contador_regressivo_1 in zip(nove_digitos, range(10, 1, -1)))
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calculando o segundo dígito verificador
    dez_digitos = nove_digitos + [digito_1]
    contador_regressivo_2 = 11
    resultado_digito_2 = sum(digito * contador_regressivo_2 for digito, contador_regressivo_2 in zip(dez_digitos, range(11, 1, -1)))
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Formatando o CPF gerado
    cpf_gerado = ''.join(map(str, nove_digitos)) + str(digito_1) + str(digito_2)
    cpf_formatado = f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}'

    return cpf_formatado

# Gerar 100 CPFs
for _ in range(100):
    print(gerar_cpf(), "Valido!")
