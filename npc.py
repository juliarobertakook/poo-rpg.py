class NPC:
    def __init__(self, nome, fala):
        self.nome = nome
        self.fala = fala

    def falar(self):

        print(f"{self.nome} diz: {self.fala}")
