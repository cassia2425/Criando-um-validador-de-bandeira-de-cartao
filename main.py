def validar_cartao(numero):
    # Remove espaços e traços
    numero = numero.replace(" ", "").replace("-", "")
    
    # Verifica se o número contém apenas dígitos
    if not numero.isdigit():
        return False
    
    # Verifica o comprimento do número do cartão
    if len(numero) < 13 or len(numero) > 19:
        return False
    
    # Implementa o algoritmo de Luhn para validação
    soma = 0
    alternar = False
    for digito in reversed(numero):
        d = int(digito)
        if alternar:
            d *= 2
            if d > 9:
                d -= 9
        soma += d
        alternar = not alternar
    
    return soma % 10 == 0

def identificar_bandeira(numero):
    if numero.startswith("4"):
        return "Visa"
    elif numero.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif numero.startswith("34") or numero.startswith("37"):
        return "American Express"
    elif numero.startswith("6011") or numero.startswith("65"):
        return "Discover"
    else:
        return "Desconhecida"

def main():
    numero_cartao = input("Digite o número do cartão de crédito: ")
    
    if not validar_cartao(numero_cartao):
        print("Número de cartão inválido.")
        return
    
    bandeira = identificar_bandeira(numero_cartao)
    print(f"A bandeira do cartão é: {bandeira}")

if __name__ == "__main__":
    main()