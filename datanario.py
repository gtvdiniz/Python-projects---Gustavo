meses = {"1": 'Janeiro', "2": 'Fevereiro', "3": 'Março', "4": 'Abril', "5": 'Maio', "6": 'Junho', "7": 'Julho', "8": 'Agosto', "9": 'Setembroo', "10": 'Outubro', "11": 'Novembro', "12": 'Dezembro'}

data = input("Entre com o formato dd/mm/aaaa: ")

dia, mes, ano = data.split('/')


print(f'Você digitou {dia} de {meses[mes]} de {ano}')