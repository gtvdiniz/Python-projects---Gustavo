class Bola: 
    #Cor, Circunferência, Material
    def __init__(self, cor, cir, mate):
        self.cor = input("Digite a cor: ")
        self.cir = input("\nDigite o tamanho em cm: ")
        self.mate = input("\nDigite o material: ")
        
    def trocaCor(self):
      s = str(input("\nDigite a nova cor: "))
      self.cor = s 
       
    
    
    def mostraCor(self):
        print(self.cor)
       

a = Bola('', '', '')
op = (input("Você quer trocar a cor da bola:\n[S/s] - Sim\n[N/n] - Não\n:"))
if op == 's' or op == 'S':
    a.trocaCor()
    
elif op == 'n' or op == 'N':
   a.mostraCor()


