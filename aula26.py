"""
Formacao basica de strings
- string
- int
- float
. <numero de digitos> f
x ou X -Hexadecimal
 (Caractere) (><^) (quantidade)
  > - Esquerda
  < - Direita
  ^ - Centro
  = - forca o numero a aparecer antes dos zeros
  Sinal  + ou -
  ex.: 0>-100,1f
  conversion flags - !r !s !a 

"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print( f'{1000.4873648123746:0=+10,.1f}')
print(f'o hexadecimal de 1500 e {1500:08X}')