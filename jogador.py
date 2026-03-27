from entidade import Entidade, GREEN, YELLOW, RESET, BOLD

class Jogador(Entidade):
    """Representa o personagem controlado pelo jogador."""
    def __init__(self, nome, vocacao):
        """Inicializa o jogador com base na vocação escolhida."""
        super().__init__(
            nome,
            100 + vocacao.bonus_vida,
            10 + vocacao.bonus_defesa,
            10 + vocacao.bonus_ataque,
            5 + vocacao.bonus_esquiva
        )
        self.vocacao = vocacao
        self.exp = 0
        self.nivel = 1
        self.pocoes = 3

    def ganhar_exp(self, quantidade):
        """Adiciona experiência e gerencia o aumento de nível."""
        print(f"\n {YELLOW}🌟 Você ganhou {quantidade} de experiência!{RESET}")
        self.exp += quantidade

        if self.exp >= 100:
            self.nivel += 1
            self.exp -= 100
            self.vida_max += 20
            self.vida = self.vida_max # Cura ao subir de nível
            self.ataque += 5
            self.defesa += 3
            print(f" {BOLD}{GREEN}LEVEL UP!{RESET} {BOLD}Você agora é nível {self.nivel}!{RESET}")
            print(f" Atributos aumentados e vida restaurada!")

    def curar(self):
        """Restaura vida usando poções do inventário."""
        if self.pocoes > 0:
            cura = 40
            self.vida = min(self.vida_max, self.vida + cura)
            self.pocoes -= 1
            print(f" {GREEN}🧪 Você usou uma poção e recuperou {cura} HP! ({self.pocoes} restantes){RESET}")
        else:
            print(f" {YELLOW}❌ Você não tem mais poções!{RESET}")
