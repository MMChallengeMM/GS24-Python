def calcular_emissao(consumo, fator):
    return consumo * fator


def emissao_veiculos():
    while True:
        try:
            print("\nCarro\n"
                  "Qual o tipo de combustivel?\n"
                  "1. Diesel\n"
                  "2. Gasolina\n"
                  "3. Elétrico\n"
                  "4. Não possuo veiculo")

            veiculo_escolhido = int(input("Digite a opção desejada:\n"))

            match veiculo_escolhido:
                case 1:
                    consumo_veiculo_escolhido = 0.13
                    break
                case 2:
                    consumo_veiculo_escolhido = 0.2
                    break
                case 3:
                    consumo_veiculo_escolhido = 0.05
                    break
                case 4:
                    consumo_veiculo_escolhido = 0
                    break
                case _:
                    print("Opção inválida")
        except ValueError:
            print("Valor inválido")

    if veiculo_escolhido != 4:
        while True:
            try:
                km_veiculo_pessoal = int(input("\nQuantos quilomêtros, em média, você dirige?\n"))
                break
            except ValueError:
                print("Valor Inválido")
    else:
        km_veiculo_pessoal = 0

    emissao_veiculo_pessoal = calcular_emissao(consumo_veiculo_escolhido, km_veiculo_pessoal)

    while True:
        try:
            print("\nTransporte Publico\n"
                  "Qual o principal meio de transporte publico que você usa?\n"
                  "1. Ônibus\n"
                  "2. Trem/Metro\n"
                  "3. Não utilizo transporte publico")

            transporte_escolhido = int(input("Digite a opção desejada:\n"))

            match transporte_escolhido:
                case 1:
                    consumo_transporte_escolhido = 0.05
                    break
                case 2:
                    consumo_transporte_escolhido = 0.03
                    break
                case 3:
                    consumo_transporte_escolhido = 0
                    break
                case _:
                    print("Opção inválida")
        except ValueError:
            print("Valor inválido")

    if transporte_escolhido != 3:
        while True:
            try:
                km_transporte_publico = int(input("\nQuantos quilomêtros, em média, você anda de transporte público?\n"))
                break
            except ValueError:
                print("Valor Inválido")
    else:
        km_transporte_publico = 0

    emissao_transporte_publico = calcular_emissao(consumo_transporte_escolhido, km_transporte_publico)

    while True:
        try:
            vezes_viagem_aviao = int(input("\nQuantas vezes você viaja de avião?\n"))
            break
        except ValueError:
            print("Valor inválido")

    while True:
        try:
            km_aviao = int(input("\nQual a distância média dos seus voos?"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_aviao = calcular_emissao(vezes_viagem_aviao * 0.09, km_aviao)

    return emissao_veiculo_pessoal + emissao_transporte_publico + emissao_aviao


def emissao_energia():
    while True:
        try:
            kwh_mes = int(input("\nQuantos kWh você consome por mês?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_energia_residencial = calcular_emissao(0.5, kwh_mes)

    while True:
        try:
            m3_gas_natural_mes = int(input("\nQuantos m³ de gás natural você usa por mês?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_gas_natural = calcular_emissao(2.2, m3_gas_natural_mes)

    while True:
        try:
            kgs_glp_mes = int(input("\nQuantos kg de GLP você usa por mês?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_glp_mes = calcular_emissao(3, kgs_glp_mes)

    return emissao_energia_residencial + emissao_gas_natural + emissao_glp_mes


def emissao_alimentos():
    while True:
        try:
            porcoes_carne_vermelha = int(input("\nQuantas vezes, por semana, você consome carne vermelha?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_carne_vermelha = calcular_emissao(4.5, porcoes_carne_vermelha)

    while True:
        try:
            porcoes_frango = int(input("\nQuantas vezes, por semana, você consome frango?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_frango = calcular_emissao(1.1, porcoes_frango)

    while True:
        try:
            porcoes_peixe = int(input("\nQuantas vezes, por semana, você consome peixe?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_peixe = calcular_emissao(1.5, porcoes_peixe)

    while True:
        try:
            porcoes_ovos_laticinios = int(input("\nQuantas vezes, por semana, você consome ovos/laticinios?\n"))
            break
        except ValueError:
            print("Valor inválido")
    emissao_ovos_laticinios = calcular_emissao(0.5, porcoes_ovos_laticinios)

    return emissao_carne_vermelha + emissao_frango + emissao_peixe + emissao_ovos_laticinios


def iniciar_calculo():
    valor_emissao_veiculo = emissao_veiculos()
    valor_emissao_energia = emissao_energia()
    valor_emissao_alimento = emissao_alimentos()
    print(f"\nAqui estão seu niveis de emissão de carbono:\n"
          f"Você gerou {valor_emissao_veiculo} kg de CO2 em veiculos\n"
          f"Você gerou {valor_emissao_energia} kg de CO2 em energia\n"
          f"Você gerou {valor_emissao_alimento} kg de CO2 em alimentos\n"
          f"Em geral você produziu {valor_emissao_alimento + valor_emissao_energia + valor_emissao_veiculo} kg de CO2")


while True:
    try:
        print("\nBem vindo à calculadora de carbono\n"
              "1. Iniciar Calculo\n"
              "0. Sair\n")

        opcao = int(input("Digite a opção desejada:\n"))

        match opcao:
            case 0:
                print("Saindo...")
                break
            case 1:
                iniciar_calculo()
    except ValueError:
        print("Valor inválido")
