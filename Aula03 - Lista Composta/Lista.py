from No import No

class Lista:

    def __init__(self):
        self.inicio = None

    def add(self, value):
        nodo = No(value)
        if self.inicio is None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Lista Encadeada (Aula03)")
        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.inicio
        while aux :
            print(  aux.dado )
            aux = aux.prox

    def remover(self, value):
        removeu = False
        if self.inicio == None:
            print("Lista Vazia")
        else:
            if value == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux: 
                    if value == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print("\n", value , " removido!" )
            else:
                print( "\n", value , " não encontrado na lista!")
            self.imprimir()
