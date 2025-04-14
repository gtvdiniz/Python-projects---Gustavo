h = int(input("Informe o valor da hora trabalhada: "))
q = int(input("Informe a quantidade de horas trabalhadas: "))
        

salariobruto = h * q 

if salariobruto <= 900: 
    impostorenda = 0 
    inss = salariobruto/10
    sindicato = salariobruto*0.03
    print(f'Salário Bruto: RS {salariobruto}\nIR : RS{impostorenda}\nINSS: RS{inss},00\nFGTS(11%): RS{salariobruto*0.11}\nSindicato: RS{sindicato}\nTotal de descontos: RS{impostorenda + inss + sindicato }\nSalário Liquido: RS{salariobruto - (impostorenda + inss + sindicato) } ')


elif salariobruto > 900 and salariobruto <=1500: 
    impostorenda = salariobruto*0.05 
    inss = salariobruto/10
    sindicato = salariobruto*0.03
    print(f'Salário Bruto: RS {salariobruto}\nIR : RS{impostorenda}\nINSS: RS{inss},00\nFGTS(11%): RS{salariobruto*0.11}\nSindicato: RS{sindicato}\nTotal de descontos: RS{impostorenda + inss + sindicato }\nSalário Liquido: RS{salariobruto - (impostorenda + inss + sindicato) } ')

elif salariobruto > 1500 and salariobruto <=2500: 
    impostorenda = salariobruto*0.1 
    inss = salariobruto/10
    sindicato = salariobruto*0.03
    print(f'Salário Bruto: RS {salariobruto}\nIR : RS{impostorenda}\nINSS: RS{inss},00\nFGTS(11%): RS{salariobruto*0.11}\nSindicato: RS{sindicato}\nTotal de descontos: RS{impostorenda + inss + sindicato }\nSalário Liquido: RS{salariobruto - (impostorenda + inss + sindicato) } ')
    
elif salariobruto > 2500: 
    impostorenda = salariobruto*0.2 
    inss = salariobruto/10
    sindicato = salariobruto*0.03
    print(f'Salário Bruto: RS {salariobruto}\nIR : RS{impostorenda}\nINSS: RS{inss},00\nFGTS(11%): RS{salariobruto*0.11}\nSindicato: RS{sindicato}\nTotal de descontos: RS{impostorenda + inss + sindicato }\nSalário Liquido: RS{salariobruto - (impostorenda + inss + sindicato) } ')
    