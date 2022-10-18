# Nome: Christopher Álvaro do Carmo
# Matrícula: 82231
# Data: 03/10/2022


def main():

    
# Escreva aqui um breve comentário sobre o programa solução da questão 1 
# Este programa busca calcular as contribuições previdenciárias realizadas em diferentes faixas salariais e diferentes regimes previdenciários.
#    
# Escreva o código para a resolução da questão 1 abaixo
# Os comandos devem estar alinhados (mesma coluna) do comando print()


# alíquotas - percentual de contribuição para as faixas salariais
    al1 = 0.075
    al2 = 0.09
    al3 = 0.12
    al4 = 0.14
    al5 = 0.145
    al6 = 0.165
    al7 = 0.19
    al8 = 0.22

# valores limites para as faixas salariais - vigentes a partir de 2022
    lim1 = 1212.00
    lim2 = 2427.35
    lim3 = 3641.03
    lim4 = 7087.22  # limite sp e não sp
    lim5 = 12136.79
    lim6 = 24273.57
    lim7 = 47333.46

# complete seu código ABAIXO desta linha

    print('Quanto é a contribuição previdenciária de um trabalhador? Simule aqui!')
    nome = input('Qual o seu Nome: ')
    salariobruto = float(input('Qual o Valor do seu Salário Bruto (R$): '))
    valorinss1 = salariobruto*al1
    valorinss2 = al1*lim1+al2*(salariobruto-lim1)
    valorinss3 = al1*lim1+al2*(lim2-lim1)+al3*(salariobruto-lim2)
    valorinss4 = al1*lim1+al2*(lim2-lim1)+al3*(lim3-lim2)+al4*(lim4-lim3)
    valorrpp5 = al1*lim1+al2*(lim2-lim1)+al3*(lim3-lim2)+al4*(lim4-lim3)+al5*(salariobruto-lim4)
    valorrpp6 = al1*lim1+al2*(lim2-lim1)+al3*(lim3-lim2)+al4*(lim4-lim3)+al5*(lim5-lim4)+al6*(salariobruto-lim5)
    valorrpp7 = al1*lim1+al2*(lim2-lim1)+al3*(lim3-lim2)+al4*(lim4-lim3)+al5*(lim5-lim4)+al6*(lim6-lim5)+al7*(salariobruto-lim6)
    valorrpp8 = al1*lim1+al2*(lim2-lim1)+al3*(lim3-lim2)+al4*(lim4-lim3)+al5*(lim5-lim4)+al6*(lim6-lim5)+al7*(lim7-lim6)+al8*(salariobruto-lim7)
    print()
    print('------------------------------------------------')
    print('Nome: ',nome)
    print('Salário Bruto (R$): ',salariobruto)
    print('------------------------------------------------')
    print('Setor: Privado (INSS) Público (RPP)')
    if salariobruto<=lim1:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al1,salariobruto*al1))
        print('Alíquota Real (%): ',100*valorinss1/salariobruto,100*valorinss1/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al1,salariobruto-salariobruto*al1)
    if salariobruto<=lim2 and salariobruto>lim1:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al2,salariobruto*al2))
        print('Alíquota Real (%):',100*valorinss2/salariobruto,100*valorinss2/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al2,salariobruto-salariobruto*al2)
    if salariobruto<=lim3 and salariobruto>lim2:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al3,salariobruto*al3))
        print('Alíquota Real (%):',100*valorinss3/salariobruto,100*valorinss3/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al3,salariobruto-salariobruto*al3)
    if salariobruto<=lim4 and salariobruto>lim3:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al4,salariobruto*al4))
        print('Alíquota Real (%):',100*valorinss4/salariobruto,100*valorinss4/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al4,salariobruto-salariobruto*al4)
    if salariobruto<=lim5 and salariobruto>lim4:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al4,salariobruto*al5))
        print('Alíquota Real (%):',100*valorinss4/salariobruto,100*valorrpp5/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al4,salariobruto-salariobruto*al5)
    if salariobruto<=lim6 and salariobruto>lim5:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al4,salariobruto*al6))
        print('Alíquota Real (%):',100*valorinss4/salariobruto,100*valorrpp6/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al4,salariobruto-salariobruto*al6)
    if salariobruto<=lim7 and salariobruto>lim6:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al4,salariobruto*al6))
        print('Alíquota Real (%):',100*valorinss4/salariobruto,100*valorrpp7/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al4,salariobruto-salariobruto*al6)
    if salariobruto>lim7:
        print('Desconto Prev. (R$): %17d %10.2f' %(salariobruto*al4,salariobruto*al6))
        print('Alíquota Real (%):',100*valorinss4/salariobruto,100*valorrpp8/salariobruto)
        print('Salário Líquido(R$):',salariobruto-salariobruto*al4,salariobruto-salariobruto*al6)


# este comando faz com que o programa seja executado uma primeira vez, a cada
# alteração e seleção da opção Run-> Run Module ou teclando F5
main()   # não apague esta linha e NÂO escreva seu código abaixo desta linha
