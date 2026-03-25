from ListaDuplamente import ListaDuplamente

lista = ListaDuplamente()
lista.imprimir()

lista.add( "João" )
lista.add( "Maria" )
lista.add( "Júlia" )
lista.add( "Abel" )

lista.imprimirReverso()

lista.remover("João")
lista.remover("José")
lista.remover("Abel")

lista.imprimirReverso()