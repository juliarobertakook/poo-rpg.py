
import random

# Cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

class Entidade:
    """Classe base para todos os personagens do jogo."""
    def __init__(self, nome, vida, defesa, ataque, esquiva):
        """Inicializa os atributos básicos da entidade."""
        self.nome = nome
        self.vida_max = vida
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva

    def atacar(self, alvo):
        """Realiza o cálculo de dano e chance de acerto contra um alvo."""
        chance = random.randint(1, 100)

        print(f"\n{BOLD}{self.nome}{RESET} está atacando {BOLD}{alvo.nome}{RESET}!")
        
        if chance <= alvo.esquiva:
            print(f"  {CYAN}{alvo.nome} foi ágil e desviou do ataque!{RESET}")
        else:
            dano = self.ataque - alvo.defesa
            if dano < 0:
                dano = 0
            alvo.vida -= dano
            print(f"  {RED}{self.nome} causou {dano} de dano!{RESET}")

    def status(self):
        """Exibe graficamente a barra de vida e HP atual."""
        # Barra de vida visual
        proporcao = max(0, self.vida / self.vida_max)
        tamanho_barra = 20
        caracteres_cheios = int(proporcao * tamanho_barra)
        barra = f"[{GREEN}{'#' * caracteres_cheios}{RED}{'-' * (tamanho_barra - caracteres_cheios)}{RESET}]"
        
        print(f"{BOLD}{self.nome:15}{RESET} {barra} {self.vida}/{self.vida_max} HP")

import random

# Cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

class Entidade:
    """Classe base para todos os personagens do jogo."""
    def __init__(self, nome, vida, defesa, ataque, esquiva):
        """Inicializa os atributos básicos da entidade."""
        self.nome = nome
        self.vida_max = vida
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva

    def atacar(self, alvo):
        """Realiza o cálculo de dano e chance de acerto contra um alvo."""
        chance = random.randint(1, 100)

        print(f"\n{BOLD}{self.nome}{RESET} está atacando {BOLD}{alvo.nome}{RESET}!")
        
        if chance <= alvo.esquiva:
            print(f"  {CYAN}{alvo.nome} foi ágil e desviou do ataque!{RESET}")
        else:
            dano = self.ataque - alvo.defesa
            if dano < 0:
                dano = 0
            alvo.vida -= dano
            print(f"   {RED}{self.nome} causou {dano} de dano!{RESET}")

    def status(self):
        """Exibe graficamente a barra de vida e HP atual."""
        # Barra de vida visual
        proporcao = max(0, self.vida / self.vida_max)
        tamanho_barra = 20
        caracteres_cheios = int(proporcao * tamanho_barra)
        barra = f"[{GREEN}{'#' * caracteres_cheios}{RED}{'-' * (tamanho_barra - caracteres_cheios)}{RESET}]"
        
        print(f"{BOLD}{self.nome:15}{RESET} {barra} {self.vida}/{self.vida_max} HP")

