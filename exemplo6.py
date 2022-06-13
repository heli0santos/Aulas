from tkinter import N


n = int(input("Digite um número inteiro >= 0 "))
maior = n
menor = n
while (n >= 0):
    if (n > maior):
        maior = n
    elif (n < menor):
        menor = n
    n = int(input("Digite um número inteiro >= 0 "))
if maior >= 0:
    print ("Maior número digitado = ", maior)
    print ("Menor número digitado = ", menor)
else:
    print ("Não foi digitado nenhum número válido.")