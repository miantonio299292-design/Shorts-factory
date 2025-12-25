import random

HOOKS = [
    "VOCÊ NÃO CHEGOU ATÉ AQUI POR ACASO.",
    "POUCAS PESSOAS ENTENDEM ISSO.",
    "DEUS AINDA FALA NO SILÊNCIO."
]

MESSAGES = [
    "NO DESERTO, A FÉ É FORJADA.",
    "O SILÊNCIO NÃO É ABANDONO.",
    "A ESPERA TAMBÉM FAZ PARTE DO PROPÓSITO."
]

CTAS = [
    "FIQUE ATÉ O FINAL.",
    "NÃO IGNORE ESSA MENSAGEM.",
    "COMPARTILHE COM ALGUÉM."
]

def generate_script():
    return f"{random.choice(HOOKS)} {random.choice(MESSAGES)} {random.choice(CTAS)}"
