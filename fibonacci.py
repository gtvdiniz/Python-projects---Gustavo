nesimo = int(input("Digite o n-ésimo termo:"))
fibo = [0]*nesimo
fibo[0] = 0
fibo[1] = 1
for i in range(2, nesimo):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
print(fibo)


    