nome = input("Digite o nome do aluno: ")
n1 = int(input("Digite a primeira nota de " + nome + ": "))
n2 = int(input("Digite a segunda nota de " + nome + ": "))
media = (n1 + n2)/2
print ("A média de " + nome + " é: %f" %(media))
if media >= 7:
    print (nome + " está aprovado. Bom trabalho.")
elif media > 4:
    print (nome + " fará a prova final. Boa srote.")
else:
    print (nome + " está reprovado.  Estude mais.")