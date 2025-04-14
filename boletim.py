
notas = [
    [9.9, 8.0, 6.4, 9.9],  #MAT

    [7.3, 8.8, 9.3, 9.8],  #FIS

    [6.3, 8.2, 7.7, 7.1],  #QUI

    [7.6, 9.9, 8.6, 9.7],  #BIO

    [6.8, 7.2, 6.2, 7.2]  #HIS
]


materias = ["Matemática", "Física", "Química", "Biologia", "História"]


saidafinal = "APROVADO"

for i in range(5):
    media = sum(notas[i])/4
    
    if media >= 6.0:
        saida = "APROVADO"
        print(f"{materias[i]}: {media:.1f} - {saida}")
    else:
        saida = "REPROVADO"
        print(f"{materias[i]}: {media:.1f} - {saida}")

    if saida == "REPROVADO":
        saidafinal = "REPROVADO"
        

print(f'Status Final - {saidafinal}')

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


