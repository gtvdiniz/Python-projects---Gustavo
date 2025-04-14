def calcular_tinta(area):
    # Cobertura da tinta: 1 litro para cada 3 metros quadrados
    litros_necessarios = area / 3
    # Cada latão contém 18 litros
    latas_necessarias = -(-litros_necessarios // 18)  # Arredonda para cima
    custo_total = latas_necessarias * 80  # Cada latão custa R$ 80,00

    return litros_necessarios, latas_necessarias, custo_total

def main():
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
    litros, latas, custo = calcular_tinta(area)

    print(f"Área a ser pintada: {area} m²")
    print(f"Litros de tinta necessários: {litros:.2f} litros")
    print(f"Latões de tinta necessários: {latas} latões")
    print(f"Custo total: R$ {custo:.2f}")

if __name__ == "__main__":
    main()
