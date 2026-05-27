from Arvore import Arvore

a = Arvore()

a.inserir( a.raiz, 48 )
a.inserir( a.raiz, 22 )
a.inserir( a.raiz, 17 )
a.inserir( a.raiz, 13 )
a.inserir( a.raiz, 64 )
a.inserir( a.raiz, 75 )
a.inserir( a.raiz, 52 )
a.inserir( a.raiz, 31 )
a.inserir( a.raiz, 19 )
a.inserir( a.raiz, 100 )

print( "\n--- Em Ordem (ERD) --------")
a.imprimirEmOrdem( a.raiz )
print( "\n--- Pré Ordem (RED)--------")
a.imprimirPreOrdem( a.raiz )
print( "\n--- Pós Ordem (EDR)--------")
a.imprimirPosOrdem( a.raiz )
print( "\n--- Ordem reversa (DRE) ---")
a.imprimirReverso( a.raiz )

print( "\n--- Em Nível --------------")
a.imprimirEmNivel( a.raiz )




# Implemente uma árvore binária de carros, que serão ordenados pela placa
# Cada carro será composto por modelo, placa e ano
# Implemente um Menu com as seguintes opções:
# -> 1) Adicionar carro
# -> 2) Imprimir em ordem (ERD)
# -> 3) Imprimir pré ordem (RED)
# -> 4) Imprimir pós ordem (EDR)
# -> 5) Imprimir ordem reversa (DRE)
# -> 6) Imprimir em nível reversa (DRE)
# -> 7) Procurar carro
# -> 0) Sair
# A opção 7 deverá perguntar ao usuário a placa do carro e informar se o carro está
# na árvore. Informe ao usuário, quantas iterações foram necessárias para encontrar
# ou não o carro
