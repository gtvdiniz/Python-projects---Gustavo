class Estudante:
    def __init__(self, nome, disciplina, notas):
        self.nome = nome 
        self.disciplina = disciplina
        self.notas = notas

    def somaNota(self):
       return sum(self.notas)
        

    def mediaNotas(self):
        return sum(self.notas)/len(self.notas)

    def show(self):
        print(f'\n Aluno:{self.nome}\n Disciplina:{self.disciplina}\n Notas:{self.notas}')
       




est1 = Estudante('Jorge', 'Matemática', [5.5, 6, 8, 10, 6])
est2 = Estudante('Maria', 'História', [8, 7, 8, 10, 6])
est3 = Estudante('Cristiano Ronaldo', 'Educação física', [10, 10, 10, 10, 10])



est1.show()
print(f' Soma das notas é: {est1.somaNota()}')
print(f' A Média é: {est1.mediaNotas()}')

est2.show()
print(f' Soma das notas é: {est2.somaNota()}')
print(f' A Média é: {est2.mediaNotas()}')

est3.show()
print(f' Soma das notas é: {est3.somaNota()}')
print(f' A Média é: {est3.mediaNotas()}')  