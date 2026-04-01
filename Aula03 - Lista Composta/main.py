from Lista import Lista
from ListaDuplamente import ListaDuplamente

def demo():
    print("Demo Lista Encadeada")
    l = Lista()
    l.add(1)
    l.add(2)
    l.add(3)
    l.remover(2)

    print("\nDemo Lista Duplamente Encadeada")
    ld = ListaDuplamente()
    ld.add('a')
    ld.add('b')
    ld.add('c')
    ld.imprimirReverso()
    ld.remover('b')

if __name__ == "__main__":
    demo()
