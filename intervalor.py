print("Digite um valor deum ponto flutuante:")
pf = float(input("Ponto flutuante --> "))

if pf >= 0 and pf <= 25:
    print("Intervalo [0, 25]")

elif pf > 25 and pf <= 50: 
    print("Intervalo (25, 50]")

elif pf > 50 and pf <= 75: 
    print("Intervalo (50, 75]")

elif pf > 75 and pf <= 100: 
    print("Intervalo (75, 100]")

else :
    print("Fora de intevalo")




















#Faça um programa em Python que leia 1 valor de ponto flutuante e diga qual dos seguintes intervalos ele pertence: ([0,25], (25,50], (50,75], (75,100])
#[a,b] significa intervalo >= a e <=b 
#(a,b] significa intervalo > a e <=b, 
