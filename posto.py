def calcular_valor(litros, tipo_combustivel):
    if tipo_combustivel == 'A':
        preco_litro = 4.90
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo_combustivel == 'G':
        preco_litro = 5.50
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    else:
        return "Tipo de combustível inválido"

    valor_bruto = litros * preco_litro
    valor_desconto = valor_bruto * desconto
    valor_final = valor_bruto - valor_desconto

    return valor_bruto, valor_desconto, valor_final

def main():
    litros = float(input("Digite o número de litros vendidos: "))
    tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

    valor_bruto, valor_desconto, valor_final = calcular_valor(litros, tipo_combustivel)

    print(f"Valor bruto: R$ {valor_bruto:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

if __name__ == "__main__":
    main()
