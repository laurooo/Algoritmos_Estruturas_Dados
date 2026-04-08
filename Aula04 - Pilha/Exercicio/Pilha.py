from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, livro):
        nodo = No(livro)
        nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Pilha de Livros - LIFO")
        if self.topo is None:
            print("\nPilha Vazia")
            return
        aux = self.topo
        while aux:
            livro = aux.dado
            print(f"\n  Título   : {livro.titulo}")
            print(f"  Páginas  : {livro.qtd_paginas}")
            print(f"  Autor    : {livro.autor.nome}")
            print(f"  Nasc.    : {livro.autor.ano_nascimento}")
            aux = aux.prox

    def remover(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = self.topo.prox
            del(aux)
        self.imprimir()

    def contar_por_autor(self, nome_autor):
        contador = 0
        aux = self.topo
        while aux:
            if aux.dado.autor.nome.lower() == nome_autor.lower():
                contador += 1
            aux = aux.prox
        print(f"\n----------------------")
        print(f"Livros de '{nome_autor}' na pilha: {contador}")
