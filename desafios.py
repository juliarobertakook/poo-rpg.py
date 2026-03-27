import random
from entidade import RED, GREEN, YELLOW, BLUE, MAGENTA, RESET, BOLD

def bau_raro(jogador):
    """Sorteia um evento aleatório (buff ou armadilha) ao encontrar um baú."""
    print(f"\n {BOLD}{YELLOW} Você encontrou um BAÚ RARO! {RESET}")

    evento = random.choice([
        "super_cura",
        "buff_ataque",
        "buff_defesa",
        "exp_bonus",
        "armadilha_forte",
        "jackpot"
    ])

    if evento == "super_cura":
        cura = random.randint(30, 60)
        jogador.vida = min(jogador.vida_max, jogador.vida + cura)
        print(f" {GREEN} Poção lendária! +{cura} de vida!{RESET}")

    elif evento == "buff_ataque":
        jogador.ataque += 10
        print(f" {RED} Seu ataque aumentou MUITO! (+10){RESET}")

    elif evento == "buff_defesa":
        jogador.defesa += 8
        print(f" {BLUE} Sua defesa aumentou! (+8){RESET}")

    elif evento == "exp_bonus":
        exp = random.randint(40, 80)
        print(f" {MAGENTA} Você encontrou tomos de conhecimento!{RESET}")
        jogador.ganhar_exp(exp)

    elif evento == "armadilha_forte":
        dano = random.randint(20, 40)
        jogador.vida -= dano
        print(f" {RED} Armadilha poderosa! Você perdeu {dano} de vida!{RESET}")

    elif evento == "jackpot":
        jogador.vida_max += 50
        jogador.vida = jogador.vida_max
        jogador.ataque += 5
        jogador.defesa += 5
        print(f" {BOLD}{YELLOW} JACKPOT! Vida Max +50 | Ataque +5 | Defesa +5{RESET}")
