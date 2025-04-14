class Musica:
    def __init__(self, nome, cantor):
        self.nome = nome
        self.cantor = cantor

    def music(self):
        return f"Nome da música: {self.nome}"

    def singer(self):
        return f"Nome do cantor: {self.cantor}"

class Playlist:
    def __init__(self):
        self.lista_de_execucao = []

    def adicionar_musica(self, musica):
        self.lista_de_execucao.append(musica)

    def play(self):
        for musica in self.lista_de_execucao:
            print(musica.music())
            print(musica.singer())

# Criando algumas músicas
musica1 = Musica("Imagine", "John Lennon")
musica2 = Musica("Bohemian Rhapsody", "Queen")
musica3 = Musica("Hotel California", "Eagles")

# Criando uma playlist e adicionando músicas
playlist = Playlist()
playlist.adicionar_musica(musica1)
playlist.adicionar_musica(musica2)
playlist.adicionar_musica(musica3)

# Executando a playlist
playlist.play()
