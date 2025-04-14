sal = float(input("Informe o salário de um colaborador: "))

if sal <= 280: 
    novosalario = sal + (sal*20/100)
    print(f'O salário antes do reajuste: {sal}\npercentual de 20% de aumento aplicado\n valor do aumento: {sal*20/100}\nnovo salário = {novosalario}')

elif sal > 280 and sal <= 700:
    novosalario = sal + (sal*15/100)
    print(f'O salário antes do reajuste: {sal}\npercentual de 15% de aumento aplicado\n valor do aumento: {sal*15/100}\nnovo salário = {novosalario}')

elif sal > 700 and sal <= 1500:
    novosalario = sal + (sal/10)
    print(f'O salário antes do reajuste: {sal}\npercentual de 10% de aumento aplicado\n valor do aumento: {sal/10}\nnovo salário = {novosalario}')

elif sal > 1500:
    novosalario = sal + (sal*5/100)
    print(f'O salário antes do reajuste: {sal}\npercentual de 5% de aumento aplicado\n valor do aumento: {sal*5/100}\nnovo salário = {novosalario}')
