from entidade import Entidade

class Bruxa(Entidade):
    """Exemplo de monstro: Fraco, mas recompensa XP."""
    def __init__(self):
        super().__init__("Bruxa", 40, 3, 6, 5)
        self.exp_recompensa = 20

class Ghoul(Entidade):
    def __init__(self):
        super().__init__("Ghoul", 45, 4, 7, 4)
        self.exp_recompensa = 25

class Grifo(Entidade):
    def __init__(self):
        super().__init__("Grifo", 50, 3, 8, 8)
        self.exp_recompensa = 30

class AranhaGigante(Entidade):
    def __init__(self):
        super().__init__("Aranha Gigante", 35, 2, 5, 2)
        self.exp_recompensa = 20

class Morcego(Entidade):
    def __init__(self):
        super().__init__("Morcego", 30, 2, 6, 10)
        self.exp_recompensa = 20

class SereiaAbisal(Entidade):
    def __init__(self):
        super().__init__("Sereia Abisal", 80, 10, 15, 6)
        self.exp_recompensa = 45

class Lobisomem(Entidade):
    def __init__(self):
        super().__init__("Lobisomem", 75, 9, 14, 12)
        self.exp_recompensa = 50

class Vampiro(Entidade):
    def __init__(self):
        super().__init__("Vampiro", 85, 8, 16, 14)
        self.exp_recompensa = 55

class Troll(Entidade):
    def __init__(self):
        super().__init__("Troll", 70, 7, 13, 10)
        self.exp_recompensa = 50

class Fantasma(Entidade):
    def __init__(self):
        super().__init__("Fantasma", 65, 6, 12, 15)
        self.exp_recompensa = 45

class Doppelganger(Entidade):
    def __init__(self):
        super().__init__("Doppelganger", 120, 15, 22, 18)
        self.exp_recompensa = 80

class Demonio(Entidade):
    def __init__(self):
        super().__init__("Demônio", 140, 18, 25, 12)
        self.exp_recompensa = 90

class Dragao(Entidade):
    def __init__(self):
        super().__init__("Dragão", 160, 20, 28, 10)
        self.exp_recompensa = 100

class Necromante(Entidade):
    def __init__(self):
        super().__init__("Necromante", 110, 14, 21, 16)
        self.exp_recompensa = 85

class Hidra(Entidade):
    def __init__(self):
        super().__init__("Hidra", 170, 22, 30, 8)
        self.exp_recompensa = 120

inimigos = {
    "fracos": [Bruxa, Ghoul, Grifo, AranhaGigante, Morcego],
    "medios": [SereiaAbisal, Lobisomem, Vampiro, Troll, Fantasma],
    "fortes": [Doppelganger, Demonio, Dragao, Necromante, Hidra]
}
