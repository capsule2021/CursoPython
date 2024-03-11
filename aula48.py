"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Métodos úteis:
  append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        +01234
#        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
# lista = [123, True, 'Luiz Otávio',  1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [10,20,30,40,50,60]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(70)  
# lista.append(80)
# lista.append(90)
# ultimo_valor =lista.pop() # remove
# print(lista, 'Removido,',ultimo_valor)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)