class Vocacao:
    """Contêiner que armazena os bônus de cada classe do jogo."""
    def __init__(self, nome, bonus_vida, bonus_ataque, bonus_defesa, bonus_esquiva):
        """Inicializa os modificadores de status da vocação."""
        self.nome = nome
        self.bonus_vida = bonus_vida
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa

        self.bonus_esquiva = bonus_esquiva
