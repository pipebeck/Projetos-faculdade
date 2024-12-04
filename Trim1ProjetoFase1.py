#preparaçâo das variaveis que serão usadas
meses = [1,2,3,4,5,6,7,8,9,10,11,12]                                      #contador de meses para o loop
somatorio = 0                                                             #somatório das temperaturas
escaldantes = 0                                                           #somatório dos meses escaldantes
maior = -100                                                              #atribui um valor fora da margem prevista para garantir que o primeiro valor vai ser atribuido como maior
mesmaior = int                                                            #valor do mês com maior temperatura
menor = 100                                                               #atribui um valor fora da margem prevista para garantir que o primeiro valor vai ser atribuido como menor
mesmenor = int                                                            #valor do mês com menor temperatura
nomesmes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] #lista de nomes dos meses

for mes in meses:                                                         #loop de 12 repetições para inserir a temperatura de cada mês
    while True:                                                           #loop while para permitir o usuario re-inserir o input em caso de erro
        try:                                                              #checa se o código a seguir retorna uma resposta válida
            entrada = (input(f'Insira a temperatura (em C) do mês {mes}: ')) #usuario insere uma string
            temp = float(entrada)                                         #a string é transformada em float
            if -60<temp<50:                                               #checa se o float está dentro da margem esperada
                break                                                     #fim do loop while se o usuario insere um input válido
            else:
                print('Temperatura inválida')                             #avisa o usuário que o valor nâo é válido e recomeça o loop while
        except ValueError:                                                #alerta caso o input nâo seja um número
            print(f'{entrada} não é um número') 

    somatorio = somatorio + temp                                          #soma os valores da temperatura para depois gerar a média
    
    if temp > maior :                                                     #testa se o mês inserido foi o mês mais quente
        maior = temp                                                      #atribui o novo maior valor
        mesmaior = mes                                                    #atribui o valor do mês atual como mês mais quente
    
    if temp < menor:                                                      #testa se o mês inserido foi o mês mais frio
        menor = temp                                                      #atribui o novo menor valor
        mesmenor = mes                                                    #atribui o valor do mês atual como mês mais frio

    if temp > 33: escaldantes = escaldantes + 1                           #soma quantos mêses estiveram acima de 33C

media = somatorio/12                                                      #gera a média para que depois o valor possa ser apresentado com 3 casas decimais
mesmaior = nomesmes [+mesmaior-1]                                         #atribui o nome do mês ao valor do mês mais quente
mesmenor = nomesmes [+mesmenor-1]                                         #atribui o nome do mês ao valor do mês mais frio
print(f'Média anual: {media:.3f}')                                        #imprime a média com três casas decimais
print('O total de meses escaldantes foi: ', escaldantes)
print('O mês com a maior temperatura foi: ', mesmaior)
print('O mês com a menor temperatura foi: ', mesmenor)