from No import No
from NoFila import NoFila

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, noDaArvore):
        nodo = NoFila( noDaArvore )
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.tamanho += 1

    def remover(self):
        if self.inicio is not None:
            aux = self.inicio.noArvore
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None 
            self.tamanho -= 1
            return aux
        return None