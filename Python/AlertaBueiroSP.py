# Menu inicial do sistema / Tela de boas-vindas
print("Seja bem-vindo ao Sistema do Alerta Bueiro SP!")
# Menu persistente até que o usuário escolha sair
while True:
    print("\n1 - Calcular o nível projetado da água")
    print("2 - Ver a fórmula")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")
    # Match case para tratar as opções do menu
    match opcao:
        case "1":
            # Input do h0
            while True:
                nivelInicialAgua = input("Digite o nível inicial da água (em centimetros): ")

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
                taxaDeIntensidade = input("Digite a taxa de intensidade (em centimetros por minuto): ")

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
            print(f"O nível projetado da água após {tempoMinCalculo} minutos será de {calculoNivelProjetadoDaAgua:.2f} centimetros.")
        # Case para exibir a fórmula do cálculo do nível projetado da água
        case "2":
            print("h(t) = h0 + i x t")
            print("h0 é o nível inicial, i é a taxa de intensidade e t é o tempo.")
        # Case para encerrar o programa
        case "0":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida. Digite 1, 2 ou 0.")
