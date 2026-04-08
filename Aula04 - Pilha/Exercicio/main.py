from Pilha import Pilha
from Livro import Livro
from Autor import Autor

pilha = Pilha()
pilha.imprimir()

# Criando autores
autor1 = Autor("Machado de Assis", 1839)
autor2 = Autor("Clarice Lispector", 1920)
autor3 = Autor("Machado de Assis", 1839)

# Criando livros
livro1 = Livro("Dom Casmurro", 256, autor1)
livro2 = Livro("A Hora da Estrela", 96, autor2)
livro3 = Livro("Memórias Póstumas de Brás Cubas", 288, autor3)
livro4 = Livro("A Paixão Segundo G.H.", 180, autor2)

# Adicionando livros na pilha
pilha.add(livro1)
pilha.add(livro2)
pilha.add(livro3)

# Removendo o livro do topo
pilha.remover()

# Adicionando mais um livro
pilha.add(livro4)

# Consultando livros por autor
pilha.contar_por_autor("Machado de Assis")
pilha.contar_por_autor("Clarice Lispector")
