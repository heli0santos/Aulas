from funcoes import basico

basico.saudacao()
basico.saudacao('Maria')
basico.saudacao('João', 30)
basico.saudacao(idade=33)

a = basico.soma_e_multi(x=10, a=2, b=3)
b = basico.soma_e_multi(x=20, a=3, b=7)

resultado = a + b
print(resultado)