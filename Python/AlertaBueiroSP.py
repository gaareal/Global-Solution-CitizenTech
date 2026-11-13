# Menu inicial do sistema
print ("Seja bem-vindo ao Sistema do Alerta Bueiro SP\n ")

# Calculo do índice de risco através da Formula "h(t) = h0 + v . t"
print ("Calculo do índice de risco através da Formula h(t) = h0 + v . t\n")
# Input do h0
nivelInicialAgua = float(input("Digite o nível inicial da água (em centimetros): "))
# Input do v
taxaDeElevacao = float(input("Digite a taxa de elevação da água (em centimetros por minuto): "))
# Input do tempo para o cálculo
tempoMinCalculo = float(input("Digite o tempo a ser calculado (em minutos): "))
# Cálculo do nível projetado da água após determinado tempo
calculoNivelProjetadoDaAgua = nivelInicialAgua + (taxaDeElevacao * tempoMinCalculo)
# Exibição do resultado do cálculo do nível projetado da água
print(f"O nível projetado da água após {tempoMinCalculo} minutos será de {calculoNivelProjetadoDaAgua} centimetros.")
