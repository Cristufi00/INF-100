# Nome do aluno: Christopher Álvaro do Carmo
# Matrícula: 82231
# Data: 21/09/2022
# Este programa busca calcular o quanto um aluno economiza estudando em uma universidade pública e como essa mensalidade seria paga, em cédulas, caso fosse em uma universidade privada 

nome_inst = 'Universidade Federal de Viçosa'
ano_atual = 2022
semestre = 2
print()             # este comando imprime uma linha em branco
# entrada de dados

nome = input('Informe seu nome: ')
anonascimento = int(input('Informe seu ano de nascimento (somente números): '))
cursoUFV = input('Informe o seu curso na UFV: ')
matrículaUFV = int(input('Informe sua matrícula na UFV (somente números): '))
entradaUFV = int(input('Informe o ano de sua entrada na UFV: '))
mens = float(input('Quanto é a mensalidade do seu curso em uma instituição particular (R$)?: '))

# processamento

mensanual = mens*12
notas100 = int(mens//100)
notas50 = int((mens-(notas100*100))/50) 
notas20 = int((mens-notas100*100-notas50*50)/20)
notas10 = int((mens-notas100*100-notas50*50-notas20*20)/10)
notas5 = int((mens-notas100*100-notas50*50-notas20*20-notas10*10)/5)
notas2 = int((mens-notas100*100-notas50*50-notas20*20-notas10*10-notas5*5)/2)

# saída


print()
print(nome_inst)
print('Nome: ',nome,'Matrícula: ',matrículaUFV)
print('Curso: ',cursoUFV,'Período: ',(ano_atual-entradaUFV)*2+semestre,'º')
print('Você tem ou completará',2022 - anonascimento, 'anos em 2022')

print()
print('Sua economia em 2022 com 12 mensalidades é de: R$',mensanual)
print('Para pagar, em dinheiro, uma mensalidade, você deverá sacar:')
print(notas100,'nota(s) de R$100,00 = ',notas100*100)
print(notas50,'nota(s) de R$50,00 = ',notas50*50)
print(notas20,'nota(s) de R$20,00 = ',notas20*20)
print(notas10,'nota(s) de R$10,00 = ',notas10*10)
print(notas5,'nota(s) de R$5,00 = ',notas5*5)
print(notas2,'nota(s) de R$2,00 = ',notas2*2)
