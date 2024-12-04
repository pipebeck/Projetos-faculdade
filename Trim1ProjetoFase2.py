import matplotlib.pyplot as plt
listas = []
arq = open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r")
#pula a primeira linha do arquivo
next(arq)

# Tratamento do arquivo dado
for item in arq:
        itemLimpo = item.replace("\n", " ").replace("/", ",")
        listas.append(itemLimpo.split(","))

arq.close()

#cria variável com tamanho da lista criada
comprimento = len(listas)

#função para visualização de intervalo de dados em modo texto
def visualizacaoDeDados():
        #inputs de ano e mês final e inicial
        while True:
                try:
                        print(" ")
                        selecao = int(input("Para acessar os dados de:\nPrecipitação - 1\nTemperatura - 2\nUmidade e vento - 3\nTodos - 4\nSelecione uma opção: "))
                        if 0 < selecao < 5:
                                break
                        else:
                                print("Valor inválido")
                except ValueError:
                        print("Insira um valor numérico")

        while True:
                try:
                        print(" ")
                        anoInicial = int(input("Insira o ano inicial desejado: "))
                        if 1960 < anoInicial < 2017:
                                break
                        else:
                                print("Valor inválido")
                except ValueError:
                        print("Insira um valor numérico")

        while True:
                try:
                        mesInicial = int(input("Insira o mês inicial desejado (1-12): "))
                        if 0 < mesInicial < 13:
                                break
                        else:
                                print("Mês inválido")
                except ValueError:
                        print("Insira um valor numérico")

        while True:
                try:
                        anoFinal = int(input("Insira o ano final desejado: "))
                        if 1960 < anoFinal < 2017:
                                break
                        else:
                                print("Ano inválido")
                except ValueError:
                        print("Insira um valor numérico")

        while True:
                try:
                        mesFinal = int(input("Insira o mês final desejado (1-12): "))
                        if 0 < mesFinal < 13:
                                break
                        else:
                                print("Mês inválido")
                except ValueError:
                        print("Insira um valor numérico")

        print("________________________________________________________________________________________________________________________________________")
        #gera os dados do período solicitado
        mesesSolicitados = []
        cont = 1
        valorMes = 0
        valorAno = 0      
        while cont < comprimento:
                valorMes = int(listas[cont][1])
                valorAno = int(listas[cont][2]) 
                if valorMes >= mesInicial and valorMes <= mesFinal and valorAno >= anoInicial and valorAno <= anoFinal:
                        mesesSolicitados.append(listas[cont])
                cont += 1

        return (selecao,mesesSolicitados)

#função para o mês mais chuvoso
def mesMaisChuvoso():
        precipMax = 0
        mesMaisChuvoso = 1
        anoMaisChuvoso = 1961
        #três loops aninhados para selecionar por mês, ano e linha da lista
        for mes in range(1, 13):
                for ano in range(1961, 2017):
                        precipMes = 0
                        for cont in range(1, comprimento):
                                if int(listas[cont][1]) == mes and int(listas[cont][2]) == ano:
                                        precipMes += float(listas[cont][3])
                        #testa o mês mais chuvoso
                        if precipMes > precipMax:
                                precipMax = precipMes
                                mesMaisChuvoso = mes
                                anoMaisChuvoso = ano


        print(" ")
        print(f"Mês mais chuvoso da série: {mesMaisChuvoso} de {anoMaisChuvoso} - {precipMax:.2f} mm")
        print(" ")

#função prara calcular a média geral e a média mínima do período solicitado
def calcMediaMes(mes):
        medias = {}
        for ano in range(2006, 2017):
                tempMinMesAno = []
                tempMesAno = []
                for item in listas:
                        if int(item[1]) == mes and int(item[2]) == ano:  #testa se o mês corresponde ao solicitado e se o ano corresponde ao loop atual
                                tempMinMesAno.append(float(item[5]))
                                tempMesAno.append(float(item[7]))

                if tempMinMesAno and tempMesAno:
                        mediaMin = sum(tempMinMesAno) / len(tempMinMesAno)
                        media = sum(tempMesAno) / len(tempMesAno)
                        medias[ano] = {"mediaMin": mediaMin, "media": media} #cria o dicionário "medias" contendo a mínima e geral

        return medias


#função para gerar gráfico
def grafico(medias, nomeMes):
        anos = list(medias.keys())
        valores = list(medias.values())
        plt.figure(figsize=(10, 6))
        plt.bar(anos, valores, color='b')
        plt.title(f"Média de temperatura mínima para o mês de {nomeMes}")
        plt.xlabel("Ano")
        plt.ylabel("Temperatura Mínima (°C)")
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

#função principal
def main():
        #pede o input de qual ação o usuário quer fazer
        while True:
                try: #pede o input até que o usuário decida fechar o programa
                        opt = int(input("0 - para fechar o programa\n1 - se quiser ver todos dados em um intervalo de tempo\n2 - se quiser ver o mês com maior preciptação na série\n3 - se quiser ver a média de temperatura mínima de um mês no período (2006-2016)\n4 - se quiser ver a média geral de temperatura de um mês no período (2006-2016)\nSelecione uma opção: "))
                        if opt == 0:
                                return  #termina o programa
                        #seleção da função 1
                        elif opt == 1:
                                selecao, mesesSolicitados = visualizacaoDeDados()
                                #testa quais dados o usuário quer ver
                                if selecao == 1:
                                        print("Precipitação no período solicitado: ")
                                        cont = 0
                                        tamanho = len(mesesSolicitados)
                                        while cont < tamanho: #loop para gerar os dados linha por linha 
                                                print(mesesSolicitados[cont][0], "/", mesesSolicitados[cont][1], "/", mesesSolicitados[cont][2], " Precipitação:", mesesSolicitados[cont][3])
                                        cont += 1
                                        print("________________________________________________________________________________________________________________________________________")

                                if selecao == 2:
                                        print("Temperaturas no período solicitado: ")
                                        cont = 0
                                        tamanho = len(mesesSolicitados)
                                        while cont < tamanho:
                                                print(mesesSolicitados[cont][0], "/", mesesSolicitados[cont][1], "/", mesesSolicitados[cont][2], "Temperatura máxima:", mesesSolicitados[cont][4], " Temperatura Mínima:", mesesSolicitados[cont][5], " Temperatura média:", mesesSolicitados[cont][7])
                                                cont += 1
                                        print("________________________________________________________________________________________________________________________________________")

                                if selecao == 3:
                                        print("Umidade e vento no período solicitado:")
                                        cont = 0
                                        tamanho = len(mesesSolicitados)
                                        while cont < tamanho:
                                                print(mesesSolicitados[cont][0], "/", mesesSolicitados[cont][1], "/", mesesSolicitados[cont][2], " Umidade Relativa:", mesesSolicitados[cont][8], " Velocidade do Vento:", mesesSolicitados[cont][9])
                                                cont += 1
                                        print("________________________________________________________________________________________________________________________________________")

                                if selecao == 4:
                                        print("Todos os dados no período solicitado:")
                                        cont = 0
                                        tamanho = len(mesesSolicitados)
                                        while cont < tamanho:
                                                print(mesesSolicitados[cont][0], "/", mesesSolicitados[cont][1], "/", mesesSolicitados[cont][2], " Precipitação:", mesesSolicitados[cont][3], " Temperatura máxima:", mesesSolicitados[cont][4], " Temperatura Mínima:", mesesSolicitados[cont][5], " Temperatura média:", mesesSolicitados[cont][7], " Umidade Relativa:", mesesSolicitados[cont][8], " Velocidade do Vento:", mesesSolicitados[cont][9])
                                                cont += 1
                                        print("________________________________________________________________________________________________________________________________________")
                        #seleção da função 2
                        elif opt == 2:
                             mesMaisChuvoso()
                        #testa se a opção foi 3 ou 4 já que elas compartilham uma função
                        elif opt == 3 or opt == 4:
                                while True:
                                        try:    #input do mês desejado
                                                mes = int(input("Insira o mês desejado (1-12): "))
                                                if 0 < mes < 13:
                                                        break
                                                else:
                                                        print("Mês inválido")
                                        except ValueError:
                                                print("Insira um valor numérico")
                                #puxa os dados da função
                                medias = calcMediaMes(mes)
                                
                                if opt == 3:
                                                print("\nMédias de temperatura mínima para o mês selecionado nos últimos 11 anos:")
                                                for ano, data in medias.items(): #loop para escrever os dados de todos os meses do período
                                                        print(f"{ano}: {data["mediaMin"]:.2f}°C")

                                                mediaDasSomasMin = sum(data["mediaMin"] for data in medias.values()) / len(medias)  #gera a média da key "mediaMin" do período
                                                print(f"\nMédia das temperaturas mínimas do mês selecionado nos últimos 11 anos: {mediaDasSomasMin:.2f}°C")
                                                print(" ")
                                                meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
                                                nomeMes = meses.get(mes, "Mês inválido") #atribui nome ao valor dos meses
                                                grafico({ano: data["mediaMin"] for ano, data in medias.items()}, nomeMes) #gera o gráfico dos dados

                                elif opt == 4:
                                                print("\nMédias de temperatura para o mês selecionado nos últimos 11 anos:")
                                                for ano, data in medias.items(): #loop para escrever os dados de todos os meses do período
                                                        print(f"{ano}: {data['media']:.2f}°C")

                                                mediaDasSomas = sum(data['media'] for data in medias.values()) / len(medias) #gera a média da key "media" do período
                                                print(f"\nMédia das temperaturas do mês selecionado nos últimos 11 anos: {mediaDasSomas:.2f}°C")
                                                print(" ")
                        else:
                                print("Insira um valor válido")
                except ValueError:
                        print("Insira um valor numérico")

main()