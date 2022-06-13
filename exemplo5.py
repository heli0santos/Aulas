## fatorial
n = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = 1
for i in range(2, (n+1)):
    fat = fat * i
print ("Fatorial de ", n," = ", fat)

## n = 5
## fat = 1
## range (2, 6)
## fat = fat * 2
## fat = 1 * 2
## fat = 2 * 3
## fat = 6 * 4
## fat = 24 * 5
## fat = 120