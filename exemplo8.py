print('\t ----Cálculo do novo salário---- ')
salario_atual = float(input('Informe o salário atual: '))

if salario_atual < 500:
    salario_novo = salario_atual+(salario_atual*0.15)
    print('Salário com reajuste = ', salario_novo)
elif salario_atual >= 500 and salario_atual <= 1000:
    salario_novo = salario_atual+(salario_atual*0.10)
    print('Salário com reajuste = ', salario_novo)
else:
    salario_novo = salario_atual+(salario_atual*0.05)
    print('Salário com reajuste = ', salario_novo)