#!/usr/bin/python



# =============================================================================================
#	Opa! Se vc esta lendo isso, desde ja muito obrigado por estar interessado no meu codigo
# =============================================================================================

# =============================================================================================================
#	Eu queria avisar que essas fontes, luzes piscando e etc nao foram feitas por mim, mas sim geradas por IA
# =============================================================================================================

# =======================================================================================================================================================================
#	Portanto, eu que programei e construi todo script base, manipulando os pacotes de rede com o scapy interagindo com portas TCP de um certo IP passado via argumento
# ========================================================================================================================================================================


import sys
from scapy.all import *


VERMELHO       = "\033[91m"
VERMELHO_PISCA = "\033[91m\033[5m"      
VERDE_NEGRITO  = "\033[1;92m"
NEGRITO        = "\033[1m"
RESET          = "\033[0m"


FONTE = {
    "P": ["█████", "█   █", "█████", "█    ", "█    "],
    "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    "R": ["█████", "█   █", "█████", "█  █ ", "█   █"],
    "T": ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
    "S": [" ████", "█    ", " ███ ", "    █", "████ "],
    "C": [" ████", "█    ", "█    ", "█    ", " ████"],
    "A": [" ███ ", "█   █", "█████", "█   █", "█   █"],
    "N": ["█   █", "██  █", "█ █ █", "█  ██", "█   █"],
}

def render_titulo(palavra):
    """Monta o nome em ASCII art (bloco) linha por linha."""
    linhas = ["", "", "", "", ""]
    for letra in palavra:
        for i in range(5):
            linhas[i] += FONTE[letra][i] + "  "
    return linhas


def banner_uso():
    """Mostrado quando o usuário NÃO passa argumento."""
    largura = 56
    print(f"\n{VERMELHO_PISCA}{'#' * largura}{RESET}")
    print(f"{VERMELHO}#{RESET}{NEGRITO}{VERDE_NEGRITO}{'MODO DE USO'.center(largura - 2)}{RESET}{VERMELHO}#{RESET}")
    print(f"{VERMELHO_PISCA}{'#' * largura}{RESET}\n")
    print(f"  {NEGRITO}Uso:{RESET}     python {sys.argv[0]} <IP>")
    print(f"  {NEGRITO}Exemplo:{RESET} python {sys.argv[0]} 192.168.0.1\n")


def banner_portscan():
    """Mostrado quando o usuário PASSA o IP como argumento."""
    linhas = render_titulo("PORTSCAN")
    largura = max(len(l) for l in linhas) + 4

    print()
    print(f"{VERMELHO_PISCA}{'•' * largura}{RESET}")
    for linha in linhas:
        print(f"{VERMELHO_PISCA}•{RESET} {VERDE_NEGRITO}{linha}{RESET} {VERMELHO_PISCA}•{RESET}")
    print(f"{VERMELHO_PISCA}{'•' * largura}{RESET}")
    print(f"{VERMELHO}{NEGRITO}{'[ Desenvolvido por Rooster123872 ]'.center(largura)}{RESET}")
    print(f"{VERMELHO_PISCA}{'•' * largura}{RESET}\n")


# ============================================================
#               CODIGO PRINCIPAL FEITO POR ROOSTER
# ============================================================
if len(sys.argv) < 2:
    banner_uso()
    sys.exit(1)

banner_portscan()

conf.verb = 0

portas = [21,22,23,24,25,80,443,110,143,445,995,993,587,389,53]

pIP = IP(dst=sys.argv[1])
pTCP = TCP(dport=portas,flags="S")
pacote = pIP/pTCP
resposta, noresp = sr(pacote, timeout=2)

for respostagrande in resposta:
        porta = respostagrande[1][TCP].sport
        statusdaporta = respostagrande[1][TCP].flags

        if statusdaporta == "SA":
                print (f"[+] Porta {porta} ABERTA!")
