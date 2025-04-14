print("Esolha x e y:")
x = float(input("x = "))

y = float(input("y = "))

if x == 0 and y == 0:
    print("A função está na origem")

elif x > 0 and y == 0:
    print("A função está no eixo X")

elif x == 0 and y > 0:
    print("A função está no eixo Y")

elif x > 0 and y > 0:
    print("A função está no Quadrante 1")

elif x < 0 and y < 0:
    print("A função está no Quadrante 3")

elif x > 0 and y < 0:
    print("A função está no Quadrante 4")

else : 
    print("A função está no Quadrante 2")



