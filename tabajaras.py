def calcular_reajuste(salario_atual):
    if salario_atual <= 280:
        percentual = 20
    elif salario_atual <= 700:
        percentual = 15
    elif salario_atual <= 1500:
        percentual = 10
    else:
        percentual = 5

    aumento = salario_atual * (percentual / 100)
    novo_salario = salario_atual + aumento

    return salario_atual, percentual, aumento, novo_salario

def main():
    salario_atual = float(input("Digite o salário atual do colaborador: "))
    salario_antigo, percentual, aumento, novo_salario = calcular_reajuste(salario_atual)

    print(f"Salário antes do reajuste: R$ {salario_antigo:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

if __name__ == "__main__":
    main()
