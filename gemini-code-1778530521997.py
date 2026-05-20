import pygame
import random
from jogador import Jogador
from vocacao import Vocacao
from inimigo import inimigos

# Configurações Iniciais
WIDTH, HEIGHT = 1280, 720
FPS = 60

class JogoVisual:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RPG PATH DARK - Mortal Kombat Edition")
        self.clock = pygame.time.Clock()
        self.fonte_titulo = pygame.font.SysFont("impact", 80)
        self.fonte_texto = pygame.font.SysFont("arial", 24)
        
        # Estado do Jogo
        self.estado = "INTRODUCAO"
        self.jogador = None
        self.inimigo_atual = None

    def desenhar_texto(self, texto, fonte, cor, x, y, centralizar=True):
        img = fonte.render(texto, True, cor)
        rect = img.get_rect(center=(x, y)) if centralizar else img.get_rect(topleft=(x, y))
        self.tela.blit(img, rect)

    def tela_introducao(self):
        self.tela.fill((0, 0, 0))
        # Referência à história original: "Em um mundo consumido pela escuridão..."
        self.desenhar_texto("PATH DARK", self.fonte_titulo, (255, 0, 0), WIDTH//2, HEIGHT//2 - 50)
        self.desenhar_texto("Pressione ESPAÇO para começar a lenda", self.fonte_texto, (255, 255, 255), WIDTH//2, HEIGHT//2 + 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.estado = "SELECAO"

    def tela_selecao(self):
        self.tela.fill((20, 20, 20))
        self.desenhar_texto("ESCOLHA SEU LUTADOR", self.fonte_texto, (255, 215, 0), WIDTH//2, 50)
        
        # Quadrados de seleção (Estilo MK)
        opcoes = [
            ("Guerreiro", (50, 150, 250, 400)),
            ("Mago", (350, 150, 250, 400)),
            ("Paladino", (650, 150, 250, 400)),
            ("Assassino", (950, 150, 250, 400))
        ]

        for nome, rect in opcoes:
            pygame.draw.rect(self.tela, (50, 50, 50), rect, 2)
            self.desenhar_texto(nome, self.fonte_texto, (255, 255, 255), rect[0] + 125, rect[1] + 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Lógica simplificada de clique para o Guerreiro
                if 50 <= mx <= 300:
                    v = Vocacao("Guerreiro", 30, 10, 5, 2)
                    self.jogador = Jogador("Heroi", v)
                    self.gerar_inimigo()
                    self.estado = "BATALHA"

    def gerar_inimigo(self):
        # Seleção baseada na lógica original de dificuldade
        classe = random.choice(inimigos["fracos"])
        self.inimigo_atual = classe()

    def tela_batalha(self):
        # Cenário de Luta
        self.tela.fill((30, 10, 10))
        pygame.draw.rect(self.tela, (100, 0, 0), (0, 500, WIDTH, 220)) # Chão
        
        # Barras de Vida Estilo MK
        # Jogador (Esquerda)
        pygame.draw.rect(self.tela, (255, 0, 0), (50, 50, 500, 30))
        vida_width = (self.jogador.vida / self.jogador.vida_max) * 500
        pygame.draw.rect(self.tela, (0, 255, 0), (50, 50, vida_width, 30))
        self.desenhar_texto(self.jogador.nome, self.fonte_texto, (255, 255, 255), 50, 30, False)

        # Inimigo (Direita)
        pygame.draw.rect(self.tela, (255, 0, 0), (730, 50, 500, 30))
        vida_inimigo = (self.inimigo_atual.vida / self.inimigo_atual.vida_max) * 500
        pygame.draw.rect(self.tela, (0, 255, 0), (730 + (500 - vida_inimigo), 50, vida_inimigo, 30))
        self.desenhar_texto(self.inimigo_atual.nome, self.fonte_texto, (255, 255, 255), 1100, 30, False)

        # "Sprites" (Placeholder - Substitua por imagens)
        pygame.draw.rect(self.tela, (0, 0, 255), (200, 300, 150, 250)) # Herói
        pygame.draw.rect(self.tela, (255, 255, 0), (930, 300, 150, 250)) # Inimigo

        self.desenhar_texto("1: ATACAR | 2: CURAR", self.fonte_texto, (255, 255, 255), WIDTH//2, 650)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.jogador.atacar(self.inimigo_atual)
                    if self.inimigo_atual.vida > 0:
                        self.inimigo_atual.atacar(self.jogador)

    def rodar(self):
        while True:
            if self.estado == "INTRODUCAO": self.tela_introducao()
            elif self.estado == "SELECAO": self.tela_selecao()
            elif self.estado == "BATALHA": self.tela_batalha()
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    jogo = JogoVisual()
    jogo.rodar()