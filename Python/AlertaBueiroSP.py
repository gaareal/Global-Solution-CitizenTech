# Menu inicial do sistema / Tela de boas-vindas
print("Seja bem-vindo ao Sistema do Alerta Bueiro SP!")

# Guarda o nível final de cada projeção durante o uso do programa
historicoProjecoes = []

# Indica se os dados da última estimativa de transbordamento podem ser usados novamente
estimativaTransbordamentoRealizada = False

# Menu persistente até que o usuário escolha sair
while True:
    print("\n1 - Calcular o nível projetado da água")
    print("2 - Ver a fórmula")
    print("3 - Mostrar tabela por minuto")
    print("4 - Mostrar histórico de projeções")
    print("5 - Estimar tempo até o transbordamento")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")
    # Match case para tratar as opções do menu
    match opcao:
        case "1":
            # Input do h0
            while True:
                nivelInicialAgua = input("Digite o nível inicial da água (em milímetros): ")

                valido = True
                tem_Digito = False
                quantidade_de_pontos = 0
                # Validação do input para garantir que seja um número válido
                for caractere in nivelInicialAgua:
                    if caractere in "0123456789":
                        tem_Digito = True
                    elif caractere == ".":
                        quantidade_de_pontos += 1
                    else:
                        valido = False
                if valido and tem_Digito and quantidade_de_pontos <= 1:
                    nivelInicialAgua = float(nivelInicialAgua)
                    break
                else:
                    print("Entrada inválida. Por favor, digite um número válido para o nível inicial da água.")

            # Input do i
            while True:
                taxaDeIntensidade = input("Digite a taxa de intensidade (em milímetros por minuto): ")

                valido = True
                tem_Digito = False
                quantidade_de_pontos = 0
                # Validação do input para garantir que seja um número válido
                for caractere in taxaDeIntensidade:
                    if caractere in "0123456789":
                        tem_Digito = True
                    elif caractere == ".":
                        quantidade_de_pontos += 1
                    else:
                        valido = False
                if valido and tem_Digito and quantidade_de_pontos <= 1:
                    taxaDeIntensidade = float(taxaDeIntensidade)
                    break
                else:
                    print("Entrada inválida. Por favor, digite um número válido para a taxa de intensidade.")

            # Input do tempo para o cálculo
            while True:
                tempoMinCalculo = input("Digite o tempo a ser calculado (em minutos): ")
                valido = True
                tem_Digito = False
                quantidade_de_pontos = 0
                # Validação do input para garantir que seja um número válido
                for caractere in tempoMinCalculo:
                    if caractere in "0123456789":
                        tem_Digito = True
                    elif caractere == ".":
                        quantidade_de_pontos += 1
                    else:
                        valido = False
                if valido and tem_Digito and quantidade_de_pontos <= 1:
                    tempoMinCalculo = float(tempoMinCalculo)
                    break
                else:
                    print("Entrada inválida. Por favor, digite um número válido para o tempo.")

            # Cálculo do nível projetado da água após determinado tempo
            calculoNivelProjetadoDaAgua = nivelInicialAgua + (taxaDeIntensidade * tempoMinCalculo)
            # Exibição do resultado do cálculo do nível projetado da água
            print(f"O nível projetado da água após {tempoMinCalculo} minutos será de {calculoNivelProjetadoDaAgua:.2f} milímetros.")

            # Adiciona o nível calculado ao histórico
            historicoProjecoes.append(calculoNivelProjetadoDaAgua)

        # Case para exibir a fórmula do cálculo do nível projetado da água
        case "2":
            print("h(t) = h0 + i x t")
            print("h0 é o nível inicial em mm, i é a taxa de intensidade em mm/min e t é o tempo em minutos.")

        # Case para mostrar a tabela até o minuto escolhido pelo usuário
        case "3":
            if len(historicoProjecoes) > 0:
                # O último minuto deve ser um número inteiro a partir de zero
                while True:
                    entradaMinutoTabela = input("Até qual minuto você quer ver a tabela? ")
                    valido = entradaMinutoTabela != ""

                    for caractere in entradaMinutoTabela:
                        if caractere not in "0123456789":
                            valido = False
                            break

                    if valido:
                        minutosTabela = int(entradaMinutoTabela)
                        break

                    print("Entrada inválida. Digite um número inteiro a partir de zero.")

                # Guarda o nível projetado em uma lista, com uma posição por minuto
                niveisPorMinuto = []
                # O + 1 inclui o último minuto, pois o range para antes do limite
                for minuto in range(minutosTabela + 1):
                    nivelNoMinuto = nivelInicialAgua + taxaDeIntensidade * minuto
                    niveisPorMinuto.append(nivelNoMinuto)

                # A posição na lista corresponde ao minuto da projeção
                print("Minuto | Nível projetado (último cálculo)")
                for minuto in range(len(niveisPorMinuto)):
                    print(f"{minuto:6d} | {niveisPorMinuto[minuto]:.2f} mm")
            else:
                print("Escolha a opção 1 para fazer um cálculo primeiro.")

        # Case para mostrar a quantidade e os resultados das projeções
        case "4":
            print(f"Cálculos realizados: {len(historicoProjecoes)}")

            # Os índices começam em zero, mas a numeração exibida começa em um
            for indice in range(len(historicoProjecoes)):
                nivelProjetado = historicoProjecoes[indice]
                print(f"Projeção {indice + 1}: {nivelProjetado:.2f} mm")

        case "5":
            # Escolha entre reutilizar os dados da última estimativa e digitar novos
            reutilizarDadosTransbordamento = False
            if estimativaTransbordamentoRealizada:
                print(f"Última estimativa com nível inicial de {nivelInicialTransbordamento} mm, "
                      f"taxa de {taxaDeIntensidadeTransbordamento} mm/min "
                      f"e altura limite de {alturaLimiteTransbordamento} mm.")
                while True:
                    resposta = input("Deseja usar os mesmos valores? (S/N): ").upper()
                    if resposta in ["S", "N"]:
                        reutilizarDadosTransbordamento = resposta == "S"
                        break
                    print("Opção inválida. Digite S para usar os mesmos valores ou N para digitar novos.")

            if reutilizarDadosTransbordamento == False:
                # Leitura e validação do campo de nível inicial
                while True:
                    nivelInicialTransbordamento = input("Digite o nível inicial da água em milímetros (ex.: 100): ")
                    valido = True
                    tem_Digito = False
                    quantidade_de_pontos = 0

                    for caractere in nivelInicialTransbordamento:
                        if caractere in "0123456789":
                            tem_Digito = True
                        elif caractere == ".":
                            quantidade_de_pontos += 1
                        else:
                            valido = False

                    if valido and tem_Digito and quantidade_de_pontos <= 1:
                        nivelInicialTransbordamento = float(nivelInicialTransbordamento)
                        break

                    print("Entrada inválida. Digite zero ou um número positivo usando ponto decimal.")

                # Leitura e validação do campo de taxa de intensidade
                while True:
                    taxaDeIntensidadeTransbordamento = input("Digite a taxa de intensidade em milímetros por minuto (ex.: 25): ")
                    valido = True
                    tem_Digito = False
                    quantidade_de_pontos = 0

                    for caractere in taxaDeIntensidadeTransbordamento:
                        if caractere in "0123456789":
                            tem_Digito = True
                        elif caractere == ".":
                            quantidade_de_pontos += 1
                        else:
                            valido = False

                    if valido and tem_Digito and quantidade_de_pontos <= 1:
                        taxaDeIntensidadeTransbordamento = float(taxaDeIntensidadeTransbordamento)
                        break

                    print("Entrada inválida. Digite zero ou um número positivo usando ponto decimal.")

                # Leitura e validação do campo de altura limite
                while True:
                    alturaLimiteTransbordamento = input("Digite a altura limite em milímetros (ex.: 225): ")
                    valido = True
                    tem_Digito = False
                    quantidade_de_pontos = 0

                    for caractere in alturaLimiteTransbordamento:
                        if caractere in "0123456789":
                            tem_Digito = True
                        elif caractere == ".":
                            quantidade_de_pontos += 1
                        else:
                            valido = False

                    if valido and tem_Digito and quantidade_de_pontos <= 1:
                        alturaLimiteTransbordamento = float(alturaLimiteTransbordamento)
                        break

                    print("Entrada inválida. Digite zero ou um número positivo usando ponto decimal.")

            # Verificação do nível inicial e da taxa antes de calcular o tempo
            if nivelInicialTransbordamento == alturaLimiteTransbordamento:
                print("No nível inicial, a água já está na altura limite.")
            elif nivelInicialTransbordamento > alturaLimiteTransbordamento:
                print("No nível inicial, a água já ultrapassou a altura limite.")
            elif taxaDeIntensidadeTransbordamento == 0:
                print("Com taxa de intensidade igual a zero, a água fica abaixo da altura limite.")
            else:
                # Na fórmula h(t) = h0 + i * t, a água chega ao limite quando h(t) = alturaLimite.
                # Subtraímos h0 dos dois lados e dividimos por i para obter t = (alturaLimite - h0) / i.
                tempoAteTransbordamento = (
                    alturaLimiteTransbordamento - nivelInicialTransbordamento
                ) / taxaDeIntensidadeTransbordamento
                print(f"Tempo estimado desde o nível inicial até a altura limite: {tempoAteTransbordamento:.2f} minutos.")

            estimativaTransbordamentoRealizada = True

        # Case para encerrar o programa
        case "0":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida. Digite 1, 2, 3, 4, 5 ou 0.")
