import random
import os
import time
from desafios import bau_raro
from jogador import Jogador
from vocacao import Vocacao
from inimigo import inimigos
from entidade import RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET, BOLD

def limpar():
    """Limpa o console de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(texto):
    """Exibe um título estilizado no terminal."""
    print(f"\n{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{BOLD}{MAGENTA} {texto:^38} {RESET}")
    print(f"{BOLD}{CYAN}{'='*40}{RESET}\n")

def introducao():
    limpar()
    cabecalho("PRÓLOGO")
    
    print("Em um mundo consumido pela escuridão...")
    time.sleep(1.5)
    print("Criaturas emergem das sombras e reinos caem em silêncio.")
    time.sleep(1.5)
    print("A esperança é apenas uma lenda esquecida.")
    time.sleep(1.5)
    print("\nMas algo desperta...")
    time.sleep(1.5)
    print(f"{BOLD}Você é a última chama contra o abismo.{RESET}")

limpar()
cabecalho("RPG PATH DARK")
introducao()

print(f"{BOLD}Escolha sua dificuldade inicial:{RESET}")
print(f"{GREEN}1 - Fácil{RESET} (Inimigos fracos)")
print(f"{YELLOW}2 - Médio{RESET} (Desafio equilibrado)")
print(f"{RED}3 - Difícil{RESET} (Somente para heróis)")

while True:
    try:
        escolha_dificuldade = int(input(f"\n{BOLD}Opção: {RESET}"))
        if escolha_dificuldade in [1, 2, 3]:
            break
    except ValueError: pass
    print(f"{RED}Dificuldade inválida. Tente novamente.{RESET}")

print(f"\n{BOLD}Escolha sua vocação:{RESET}")
print(f"{BLUE}1 - Guerreiro{RESET} (Vida: 130 | Ataque: 20 | Defesa: 15 | Esquiva: 7)")
print(f"{MAGENTA}2 - Mago{RESET}      (Vida: 90  | Ataque: 35 | Defesa: 8  | Esquiva: 10)")
print(f"{YELLOW}3 - Paladino{RESET}  (Vida: 150 | Ataque: 15 | Defesa: 22 | Esquiva: 5)")
print(f"{RED}4 - Assassino{RESET} (Vida: 100 | Ataque: 25 | Defesa: 5  | Esquiva: 20)")

while True:
    try:
        v_opc = int(input(f"\n{BOLD}Opção: {RESET}"))
        if v_opc == 1:
            vocacao = Vocacao("Guerreiro", 30, 10, 5, 2)
            break
        elif v_opc == 2:
            vocacao = Vocacao("Mago", -10, 25, -2, 5)
            break
        elif v_opc == 3:
            vocacao = Vocacao("Paladino", 50, 5, 12, 0)
            break
        elif v_opc == 4:
            vocacao = Vocacao("Assassino", 0, 15, -5, 15)
            break
    except ValueError: pass
    print(f"{RED}Vocação inválida.{RESET}")

nome = input(f"\n{BOLD}Nome do seu herói: {RESET}")
jogador = Jogador(nome, vocacao)

vitorias = 0

# LOOP PRINCIPAL DO JOGO (Até o jogador morrer)
while jogador.vida > 0:
    limpar()
    
    # Determina o inimigo baseado na dificuldade escolhida e progressão
    # Inimigos ficam mais fortes conforme as vitorias aumentam
    if vitorias < 3 and escolha_dificuldade == 1:
        classe_inimigo = random.choice(inimigos["fracos"])
    elif vitorias < 3 and escolha_dificuldade == 2:
        classe_inimigo = random.choice(inimigos["medios"])
    elif vitorias >= 6 or escolha_dificuldade == 3:
        classe_inimigo = random.choice(inimigos["fortes"])
    else:
        classe_inimigo = random.choice(inimigos["medios"])

    inimigo = classe_inimigo()
    
    cabecalho(f"BATALHA #{vitorias + 1}")
    print(f" {BOLD}{jogador.nome} ({jogador.vocacao.nome} Lvl {jogador.nivel}){RESET} vs {BOLD}{RED}{inimigo.nome}{RESET}!")
    print(f" Vitórias acumuladas: {YELLOW}{vitorias}{RESET}")
    print(f"{CYAN}{'-'*40}{RESET}")
    
    time.sleep(1)
    turno = 1

    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n{BOLD}{YELLOW}--- Turno {turno} ---{RESET}")
        
        jogador.status()
        inimigo.status()
        
        print(f"\n{BOLD}O que você deseja fazer?{RESET}")
        print(f"{RED}1 - Atacar{RESET}")
        print(f"{GREEN}2 - Usar Poção ({jogador.pocoes} rest.){RESET}")
        print(f"{BLUE}3 - Aguardar (Recupera 5 HP){RESET}")
        
        decisao = input(f"\n{BOLD}Ação: {RESET}")
        
        if decisao == "1":
            jogador.atacar(inimigo)
        elif decisao == "2":
            jogador.curar()
        else:
            print(f" {BLUE}Você recupera um pouco de folêgo (+5 HP).{RESET}")
            jogador.vida = min(jogador.vida_max, jogador.vida + 5)
        
        if inimigo.vida > 0:
            inimigo.atacar(jogador)
        
        if jogador.vida > 0:
            input(f"\n{BOLD}Pressione Enter para o próximo turno...{RESET}")
        turno += 1

    if jogador.vida > 0:
        vitorias += 1
        limpar()
        cabecalho("VITÓRIA!")
        print(f" {BOLD}{GREEN}Você derrotou o {inimigo.nome}!{RESET}")
        jogador.ganhar_exp(inimigo.exp_recompensa)
        
        if random.randint(1, 100) <= 40:
            bau_raro(jogador)
        
        print(f"\n{BOLD}Deseja continuar sua jornada ou descansar?{RESET}")
        print("1 - Continuar explorando")
        print("2 - Fugir (Sair do jogo)")
        
        cont = input(f"\n{BOLD}Opção: {RESET}")
        if cont == "2":
            print(f"\n{BOLD}{YELLOW}Você decidiu encerrar sua jornada vitorioso com {vitorias} vitórias.{RESET}")
            break
    else:
        limpar()
        cabecalho("HERÓI TOMBADO")
        print(f" {BOLD}{RED}Infelizmente você não resistiu aos ferimentos.{RESET}")
        print(f" Sua jornada termina aqui com {YELLOW}{vitorias}{RESET} vitórias.")
        print(f"\n{BOLD}{CYAN}Obrigado por jogar Path Dark!{RESET}")
import random
import os
import time
from desafios import bau_raro
from jogador import Jogador
from vocacao import Vocacao
from inimigo import inimigos
from entidade import RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET, BOLD

def limpar():
    """Limpa o console de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(texto):
    """Exibe um título estilizado no terminal."""
    print(f"\n{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{BOLD}{MAGENTA} {texto:^38} {RESET}")
    print(f"{BOLD}{CYAN}{'='*40}{RESET}\n")

limpar()
cabecalho("RPG PATH DARK")

print(f"{BOLD}Escolha sua dificuldade inicial:{RESET}")
print(f"{GREEN}1 - Fácil{RESET} (Inimigos fracos)")
print(f"{YELLOW}2 - Médio{RESET} (Desafio equilibrado)")
print(f"{RED}3 - Difícil{RESET} (Somente para heróis)")

while True:
    try:
        escolha_dificuldade = int(input(f"\n{BOLD}Opção: {RESET}"))
        if escolha_dificuldade in [1, 2, 3]:
            break
    except ValueError: pass
    print(f"{RED}Dificuldade inválida. Tente novamente.{RESET}")

print(f"\n{BOLD}Escolha sua vocação:{RESET}")
print(f"{BLUE}1 - Guerreiro{RESET} (Vida: 130 | Ataque: 20 | Defesa: 15 | Esquiva: 7)")
print(f"{MAGENTA}2 - Mago{RESET}      (Vida: 90  | Ataque: 35 | Defesa: 8  | Esquiva: 10)")
print(f"{YELLOW}3 - Paladino{RESET}  (Vida: 150 | Ataque: 15 | Defesa: 22 | Esquiva: 5)")
print(f"{RED}4 - Assassino{RESET} (Vida: 100 | Ataque: 25 | Defesa: 5  | Esquiva: 20)")

while True:
    try:
        v_opc = int(input(f"\n{BOLD}Opção: {RESET}"))
        if v_opc == 1:
            vocacao = Vocacao("Guerreiro", 30, 10, 5, 2)
            break
        elif v_opc == 2:
            vocacao = Vocacao("Mago", -10, 25, -2, 5)
            break
        elif v_opc == 3:
            vocacao = Vocacao("Paladino", 50, 5, 12, 0)
            break
        elif v_opc == 4:
            vocacao = Vocacao("Assassino", 0, 15, -5, 15)
            break
    except ValueError: pass
    print(f"{RED}Vocação inválida.{RESET}")

nome = input(f"\n{BOLD}Nome do seu herói: {RESET}")
jogador = Jogador(nome, vocacao)

vitorias = 0

# LOOP PRINCIPAL DO JOGO (Até o jogador morrer)
while jogador.vida > 0:
    limpar()
    
    # Determina o inimigo baseado na dificuldade escolhida e progressão
    # Inimigos ficam mais fortes conforme as vitorias aumentam
    if vitorias < 3 and escolha_dificuldade == 1:
        classe_inimigo = random.choice(inimigos["fracos"])
    elif vitorias < 3 and escolha_dificuldade == 2:
        classe_inimigo = random.choice(inimigos["medios"])
    elif vitorias >= 6 or escolha_dificuldade == 3:
        classe_inimigo = random.choice(inimigos["fortes"])
    else:
        classe_inimigo = random.choice(inimigos["medios"])

    inimigo = classe_inimigo()
    
    cabecalho(f"BATALHA #{vitorias + 1}")
    print(f" {BOLD}{jogador.nome} ({jogador.vocacao.nome} Lvl {jogador.nivel}){RESET} vs {BOLD}{RED}{inimigo.nome}{RESET}!")
    print(f" Vitórias acumuladas: {YELLOW}{vitorias}{RESET}")
    print(f"{CYAN}{'-'*40}{RESET}")
    
    time.sleep(1)
    turno = 1

    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n{BOLD}{YELLOW}--- Turno {turno} ---{RESET}")
        
        jogador.status()
        inimigo.status()
        
        print(f"\n{BOLD}O que você deseja fazer?{RESET}")
        print(f"{RED}1 - Atacar{RESET}")
        print(f"{GREEN}2 - Usar Poção ({jogador.pocoes} rest.){RESET}")
        print(f"{BLUE}3 - Aguardar (Recupera 5 HP){RESET}")
        
        decisao = input(f"\n{BOLD}Ação: {RESET}")
        
        if decisao == "1":
            jogador.atacar(inimigo)
        elif decisao == "2":
            jogador.curar()
        else:
            print(f" {BLUE}Você recupera um pouco de folêgo (+5 HP).{RESET}")
            jogador.vida = min(jogador.vida_max, jogador.vida + 5)
        
        if inimigo.vida > 0:
            inimigo.atacar(jogador)
        
        if jogador.vida > 0:
            input(f"\n{BOLD}Pressione Enter para o próximo turno...{RESET}")
        turno += 1

    if jogador.vida > 0:
        vitorias += 1
        limpar()
        cabecalho("VITÓRIA!")
        print(f" {BOLD}{GREEN}Você derrotou o {inimigo.nome}!{RESET}")
        jogador.ganhar_exp(inimigo.exp_recompensa)
        
        if random.randint(1, 100) <= 40:
            bau_raro(jogador)
        
        print(f"\n{BOLD}Deseja continuar sua jornada ou descansar?{RESET}")
        print("1 - Continuar explorando")
        print("2 - Fugir (Sair do jogo)")
        
        cont = input(f"\n{BOLD}Opção: {RESET}")
        if cont == "2":
            print(f"\n{BOLD}{YELLOW}Você decidiu encerrar sua jornada vitorioso com {vitorias} vitórias.{RESET}")
            break
    else:
        limpar()
        cabecalho("HERÓI TOMBADO")
        print(f" {BOLD}{RED}Infelizmente você não resistiu aos ferimentos.{RESET}")
        print(f" Sua jornada termina aqui com {YELLOW}{vitorias}{RESET} vitórias.")

print(f"\n{BOLD}{CYAN}Obrigado por jogar Path Dark!{RESET}")
 
