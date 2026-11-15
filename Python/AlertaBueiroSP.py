# Menu inicial do sistema
print ("Seja bem-vindo ao Sistema do Alerta Bueiro SP\n ")

# Calculo do índice de risco através da Formula "h(t) = h0 + v . t"
print ("Calculo do índice de risco através da Formula h(t) = h0 + v . t\n")
# Input do h0
while True:
    nivelInicialAgua = input("Digite o nível inicial da água (em centimetros): ")

    valido = True
    tem_Digito = False
    quantidade_de_pontos = 0

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

# Input do v
while True:
    taxaDeElevacao = input("Digite a taxa de elevação da água (em centimetros por minuto): ")

    valido = True
    tem_Digito = False
    quantidade_de_pontos = 0

    for caractere in taxaDeElevacao:
        if caractere in "0123456789":
            tem_Digito = True
        elif caractere == ".":
            quantidade_de_pontos += 1
        else:
            valido = False
    if valido and tem_Digito and quantidade_de_pontos <= 1:
        taxaDeElevacao = float(taxaDeElevacao)
        break
    else:
            print("Entrada inválida. Por favor, digite um número válido para a taxa de elevação da água.")

# Input do tempo para o cálculo
while True:
    tempoMinCalculo = input("Digite o tempo a ser calculado (em minutos): ")
    valido = True
    tem_Digito = False
    quantidade_de_pontos = 0

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
calculoNivelProjetadoDaAgua = nivelInicialAgua + (taxaDeElevacao * tempoMinCalculo)
# Exibição do resultado do cálculo do nível projetado da água
print(f"O nível projetado da água após {tempoMinCalculo} minutos será de {calculoNivelProjetadoDaAgua} centimetros.")
