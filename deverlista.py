class Tarefa:

    def __init__(self):
        self.tarefas = []

    #Função para adicionar tarefas
    def adicionar_tarefa(self, tarefa):
       if tarefa not in self.tarefas:
          self.tarefas.append(tarefa)

    #Função para excluir tarefas
    def excluir_tarefa(self, tarefa):
       if tarefa in self.tarefas:
          self.tarefas.remove(tarefa)

        

    def Show_tarefas(self):
        print(f'Tarefas: {self.tarefas}')
    
lista = Tarefa()

while True: 
 
 op = int(input("Escolha o que fazer: \n [1] - ADICIONAR TAREFA \n [2] - EXCLUIR TAREFA \n [3] - VIZUALIZAR TAREFA \n [4] - SAIR \n : "))
 if op in (1, 2, 3, 4):
    break
 
 #Adiciona Tarefas
 if op == 1:
    tarefa = input("Digite a tarefa a ser adicionada")
    lista.adicionar_tarefa()
 
 #Remove Tarefas
 elif op == 2: 
   tarefa = input("Digite a tarefa a ser excluida")
   lista.excluir_tarefa()
 
 #Vizualiza Tarefas
 elif op == 3: 
   lista.Show_tarefas()
   
 else: 
    break





