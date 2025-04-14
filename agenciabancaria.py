diciocli = {'numero_conta':[], 'saldo':[]}
contagem_negativos = 0  

for i in range(5):
    numero_conta = int(input("Digite o número da conta do cliente: "))
    if numero_conta == -999:
        break 
    diciocli['numero_conta'].append(numero_conta)

    saldo = float(input("Digite o saldo do cliente: "))
    diciocli['saldo'].append(saldo)
   
    print(diciocli)
    
    if saldo < 0: 
        contagem_negativos += 1

total_clientes = len(diciocli['numero_conta'])
saldo_total = sum(diciocli['saldo'])

print(f'O total de clientes com saldo negativo é: {contagem_negativos}')
print(f'O total de clientes da agência é: {total_clientes}')
print(f'O saldo total da agência é: R$ {saldo_total:.2f}')
