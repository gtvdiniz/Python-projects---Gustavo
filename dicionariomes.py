mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembroo', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

meslido = int(input('Entre com o valor do mes(1 a 12): '))

if 1 <= meslido <= 12:
    print(f'você digitou o mês de {mes[meslido]}')

else:
    print("Inválido !!!")