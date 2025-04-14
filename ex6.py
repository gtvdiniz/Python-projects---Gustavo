class Tv: 
    def __init__(self, canal = 0, volume = 0 ):
       self.vol = volume 
       self.can = canal 
       
    def volumeTv(self): 
        nivelvol = int(input("Informe o volume desejado(0 - 100): "))
        
        if nivelvol > 100 or nivelvol < 0: 
            print("Erro!!!!!")
            
        else: 
            self.vol = nivelvol 
    
    def canalTv(self): 
        escanal = int(input("Informe o canal desejado(1- 69): "))
        
        if escanal > 69 or escanal < 1:
            print("Erro!!!!!")
            
        else: 
            self.can = escanal
            
            
    
    def progAtual(self):
        print(f'A televisão está no canal {self.can} com volume {self.vol}')
        

a = Tv()
alt = input("Deseja ligara televisão?\n[S] - sim [N] - não\n:")
if alt == 's' or alt == 'S':
    a.canalTv()

    while True: 
        op = int(input("\nDigite uma opção:\n[1] - Escolher Canal\n[2] - Aumentar/Diminuir Volume\n[3] - Mostrar programação atual\n[4] - Desligar televisão\n:"))
    
        if op == 1: 
         a.canalTv()
        
        elif op == 2: 
         a.volumeTv()
        
        elif op == 3: 
         a.progAtual()
    
        elif op == 4: 
         break 
    
        else: 
         print("Erro !!!!")

else: 
    print("Desligando...")
        
            
  
        