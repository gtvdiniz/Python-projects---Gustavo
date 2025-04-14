import random

NumeroEscolhido = random.randint(1, 100)
tentativa = 0 
tentativa = 0 

while True: 
    n = int(input("Descubra qual é o número:  "))
    tentativa += 1

    if n == NumeroEscolhido: 
        print("ACERTOU !!!")
        break

    elif n > NumeroEscolhido: 
       print("está abaixo")

    else:
       print("está acima")
    
    if tentativa == 10 and n == NumeroEscolhido :
         print("ACERTOU !!!")
         break
    
    elif tentativa == 10:
        print("10 Chances utilizadas, terminando programa......")
        break

    

