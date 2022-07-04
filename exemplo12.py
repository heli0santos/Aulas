num = int(input("Digite um número: "))
contador = 0

while num != 0:
    num //= 10
    contador += 1

print ("Total de dígitos = ", contador)