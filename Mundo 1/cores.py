# Arquivo: cores.py

# Estilos de Texto
RESET = '\033[m'
NEGR  = '\033[1m'
SUBLI = '\033[4m'

# Cores de Frente (Texto)
R     = '\033[31m'
G   = '\033[32m'
Y  = '\033[33m'
B    = '\033[34m'
P  = '\033[35m'
C   = '\033[36m'
W   = '\033[97m'

# Cores de Fundo (Background)
BG_RED    = '\033[41m'
BG_GREEN  = '\033[42m'
BG_BLUE   = '\033[44m'

# Função Utilitária
def status_sim(valor):
    return f"{G}Sim{RESET}" if valor else f"{R}Não{RESET}"

def status_v_f(valor):
    return f"{G}Verdadeiro{RESET}" if valor else f"{R}Falso{RESET}"

def status_ok(valor):
    return f"{G}✔{RESET}" if valor else f"{R}✘{RESET}"

