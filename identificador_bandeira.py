def identificar_bandeira(numero_cartao):
    numero = str(numero_cartao)
    if numero.startswith('4') and len(numero) in [13, 16, 19]:
        return 'Visa'
    elif numero[:2] in ['51', '52', '53', '54', '55'] and len(numero) == 16:
        return 'MasterCard'
    elif numero[:2] in ['34', '37'] and len(numero) == 15:
        return 'American Express'
    elif numero[:4] == '6011' or numero[:2] in ['65'] or (numero[:3] >= '644' and numero[:3] <= '649'):
        return 'Discover'
    elif numero[:4] in ['3528', '3589'] and len(numero) == 16:
        return 'JCB'
    elif numero[:2] in ['36', '38'] and len(numero) == 14:
        return 'Diners Club'
    else:
        return 'Bandeira desconhecida'

if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    print("Bandeira identificada:", identificar_bandeira(numero))