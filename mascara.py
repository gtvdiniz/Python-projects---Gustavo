print("Defina a, b e c")

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))


r1 = (-(b) + (b**2 -(4*a*c)))/2
r2 = (-(b) - (b**2 -4*a*c))/2

if a == 0:
    print("A equação não está certa!")

elif (b**2 - 4*a*c) < 0:
    print("A equação não possui raízes reais")

else:
    formatted_r1 = "{:.5f}".format(r1)
    formatted_r2 = "{:.5f}".format(r2)
    print("As raízes são:", formatted_r1,"e",   formatted_r2)