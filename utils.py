def validar_cartao(numero_cartao):
    numero_cartao = numero_cartao.replace(" ", "")
    if not numero_cartao.isdigit() or len(numero_cartao) < 13 or len(numero_cartao) > 19:
        return False
    return True

def identificar_bandeira(numero_cartao):
    if not validar_cartao(numero_cartao):
        return "Número de cartão inválido"
    
    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif numero_cartao.startswith("34") or numero_cartao.startswith("37"):
        return "American Express"
    elif numero_cartao.startswith("6011") or numero_cartao.startswith("65"):
        return "Discover"
    else:
        return "Bandeira desconhecida"