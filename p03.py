# Nome do aluno: Christopher Álvaro do Carmo
# Matrícula: 82231
# Data: 28/09/2022
# O programa busca obter informações sobre o estudante e seu ingresso na Universidade Grana Viva, assim como informar o quanto de dinheiro, em dinheiro, será necessário para pagar uma mensalidade na instituição.

def main():
    nome_inst = 'Universidade Grana Viva'
    ano_atual = 2022
    semestre = 2
    print()             # este comando imprime uma linha em branco
    # entrada de dados
    nome = input('Informe seu nome: ')
    ano = int(input('Informe o ano do seu nascimento: '))
    # inclua o teste número 1 e a mensagem de erro 1
    # e faça a indentação necessária do restante do código
    if ano>ano_atual:
        print('ERRO: ano de nascimento (',ano,') > ano atual (',ano_atual,')!!!')
    else:
        ano_ent = int(input('Informe o ano de entrada na Universidade Grana Viva: '))
    # inclua o teste número 2 e a mensagem de erro 2
    # e faça a indentação necessária do restante do código
        if ano_ent>ano_atual:
            print('ERRO: ano de entrada na UGV (',ano_ent,') > ano atual (',ano_atual,')!!!')
    # inclua, na sequência, o teste número 3 e a mensagem de erro 3
    # e faça a indentação necessária do restante do código
        if ano>ano_ent:
            print('ERRO: ano de nascimento (',ano,') > ano de entrada na UGV (',ano_ent,')!!!')
    # processamento - que só deve ser feito no caso de não haver inconsistência
    # entre o ano de nascimento, ano de entrada na UFV e o ano atual
        else:
            valor = float(input('Quanto é a mensalidade do seu curso (R$)?: '))
            valor = round(valor+0.49)
            n100 = valor // 100
            n50 = valor % 100 // 50
            n20 = valor % 100 % 50 // 20
            n10 = valor % 100 % 50 % 20 // 10
            n5 = valor % 100 % 50 % 20 % 10 // 5
            m1 = valor % 100 % 50 % 20 % 10 % 5 % 2
            n2 = valor % 100 % 50 % 20 % 10 % 5 // 2 + m1
            soma = 100*n100 + 50*n50 + 20*n20 + 10*n10 + 5*n5 + 2*n2
            # saída
            print(nome_inst)
            print('Nome:', nome)
            print('Para pagar, em dinheiro, uma mensalidade, você deverá sacar') 

            # os comandos print a seguir devem passar a ser condicionais
            if n100>=1:
                print('%3d nota(s) de R$ 100,00 = %8.2f' %(n100, 100*n100))
            if n50>=1:
                print('%3d nota(s) de R$  50,00 = %8.2f' %(n50, 50*n50))
            if n20>=1:
                print('%3d nota(s) de R$  20,00 = %8.2f' %(n20, 20*n20))
            if n10>=1:
                print('%3d nota(s) de R$  10,00 = %8.2f' %(n10, 10*n10))
            if n5>=1:
                print('%3d nota(s) de R$   5,00 = %8.2f' %(n5, 5*n5))
            if n2>=1:
                print('%3d nota(s) de R$   2,00 = %8.2f' %(n2, 2*n2))
          

            # o próximo print NÃO é condicional
            print('Valor total (R$): %17.2f' %soma)

