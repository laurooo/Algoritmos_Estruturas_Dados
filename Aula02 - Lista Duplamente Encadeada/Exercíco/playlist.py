
class Musica:
    def __init__(self, titulo, autor, duracao):
        self.titulo = titulo
        self.autor = autor
        self.duracao = duracao  # duração em segundos

    def __str__(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return f'"{self.titulo}" - {self.autor} ({minutos}:{segundos:02d})'


class No:
    def __init__(self, musica):
        self.musica = musica
        self.anterior = None
        self.proximo = None


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, musica):
        novo = No(musica)

        # lista vazia
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            self.tamanho += 1
            return

        # inserir antes do primeiro (menor que todos)
        if musica.titulo.lower() < self.inicio.musica.titulo.lower():
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo
            self.tamanho += 1
            return

        # percorrer para encontrar a posição correta
        atual = self.inicio
        while atual.proximo is not None:
            if musica.titulo.lower() < atual.proximo.musica.titulo.lower():
                break
            atual = atual.proximo

        # inserir após o nó atual
        novo.proximo = atual.proximo
        novo.anterior = atual

        if atual.proximo is not None:
            atual.proximo.anterior = novo
        else:
            self.fim = novo

        atual.proximo = novo
        self.tamanho += 1

    def remover(self, titulo):
        atual = self.inicio

        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower():
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                self.tamanho -= 1
                print(f'"{atual.musica.titulo}" removida da playlist.')
                return

            atual = atual.proximo

        print(f'Música "{titulo}" não encontrada.')

    def exibir(self):
        if self.inicio is None:
            print(f'Playlist "{self.nome}" está vazia.')
            return

        print(f'\n=== Playlist: {self.nome} ({self.tamanho} músicas) ===')
        atual = self.inicio
        i = 1
        while atual is not None:
            print(f'  {i}. {atual.musica}')
            atual = atual.proximo
            i += 1

    def exibir_invertida(self):
        if self.fim is None:
            print(f'Playlist "{self.nome}" está vazia.')
            return

        print(f'\n=== Playlist (invertida): {self.nome} ===')
        atual = self.fim
        i = self.tamanho
        while atual is not None:
            print(f'  {i}. {atual.musica}')
            atual = atual.anterior
            i -= 1

    def duracao_total(self):
        total = 0
        atual = self.inicio
        while atual is not None:
            total += atual.musica.duracao
            atual = atual.proximo
        minutos = total // 60
        segundos = total % 60
        print(f'Duração total: {minutos}:{segundos:02d}')

    def escolher_e_remover(self):
        if self.inicio is None:
            print('A playlist está vazia.')
            return

        self.exibir()
        print()

        while True:
            entrada = input('Digite o número da música que deseja remover (ou 0 para cancelar): ')

            if not entrada.isdigit():
                print('Apenas numeros.')
                continue

            numero = int(entrada)

            if numero == 0:
                print('Cancelada a remoção.')
                return

            if numero < 1 or numero > self.tamanho:
                print(f'Escolha entre 1 e {self.tamanho}.')
                continue

            # percorrer até o nó escolhido
            atual = self.inicio
            for _ in range(numero - 1):
                atual = atual.proximo

            self.remover(atual.musica.titulo)
            return


# ==================== Programa Principal ====================

playlist = Playlist("Minhas Favoritas")

playlist.adicionar(Musica("João e Maria", "Chico Buarque", 482))
playlist.adicionar(Musica("60 Segundos", "Gusttavo Lima", 354))
playlist.adicionar(Musica("Lancinho", "Turma do Pagode", 391))
playlist.adicionar(Musica("Rap Lord", "Haikaiss", 382))
playlist.adicionar(Musica("Fugidinha", "Michel Teló", 295))

while True:
    print('\n==============================')
    print('       MENU DA PLAYLIST       ')
    print('==============================')
    print('1. Exibir playlist')
    print('2. Remover música')
    print('3. Duração total')
    print('4. Sair')
    print('------------------------------')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        playlist.exibir()
    elif opcao == '2':
        playlist.escolher_e_remover()
    elif opcao == '3':
        playlist.duracao_total()
    elif opcao == '4':
        print('Encerrando...')
        break
    else:
        print('Opção inválida.')
