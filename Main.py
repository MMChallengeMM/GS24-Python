from datetime import datetime


def calcular_emissao(consumo, fator):
    return consumo * fator


def emissao_veiculos():
    print("\nEsta primeira etapa é sobre seus meios de locomoção.\n"
          "Primeiro, vou fazer algumas perguntas sobre o seu veículo pessoal.")

    while True:
        try:
            print("\nQual o tipo de combustível do seu veículo?\n"
                  "1. Diesel\n"
                  "2. Gasolina\n"
                  "3. Elétrico\n"
                  "4. Não possuo veículo\n"
                  "===========================================================")

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
                    print("Opção inválida.")
        except ValueError:
            print("Valor inválido.")

    if veiculo_escolhido != 4:
        while True:
            try:
                km_veiculo_pessoal = float(input("Quantos quilômetros por semana, em média, você dirige?\n"))
                break
            except ValueError:
                print("Valor inválido.\n")
    else:
        km_veiculo_pessoal = 0

    emissao_veiculo_pessoal = calcular_emissao(consumo_veiculo_escolhido, km_veiculo_pessoal)

    print("\nAgora vou fazer algumas perguntas sobre seu uso de transporte público.")

    while True:
        try:
            print("Qual o principal meio de transporte público que você utiliza?\n"
                  "1. Ônibus\n"
                  "2. Trem/Metrô\n"
                  "3. Não utilizo transporte público\n"
                  "===========================================================")

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
                    print("Opção inválida.")
        except ValueError:
            print("Valor inválido.\n")

    if transporte_escolhido != 3:
        while True:
            try:
                km_transporte_publico = float(
                    input("Quantos quilômetros por semana, em média, você utiliza transporte público?\n"))
                break
            except ValueError:
                print("Valor inválido.\n")
    else:
        km_transporte_publico = 0

    emissao_transporte_publico = calcular_emissao(consumo_transporte_escolhido, km_transporte_publico)

    print("\nPara finalizar esta etapa, vou fazer algumas perguntas sobre viagens aéreas.")

    while True:
        try:
            vezes_viagem_aviao = int(input("Quantas vezes por ano você viaja de avião?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")

    while True:
        try:
            km_aviao = float(input("Qual a distância média dos seus voos?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_aviao = calcular_emissao(vezes_viagem_aviao * 0.09, km_aviao)

    return emissao_veiculo_pessoal + emissao_transporte_publico + emissao_aviao


def emissao_energia():
    print("\nEsta segunda etapa é sobre sua energia residencial.\n"
          "Vou fazer algumas perguntas sobre o seu uso de energia.")
    while True:
        try:
            kwh_mes = float(input("Quantos kWh você consome por mês?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_energia_residencial = calcular_emissao(0.5, kwh_mes)

    while True:
        try:
            m3_gas_natural_mes = float(input("Quantos m³ de gás natural você utiliza por mês?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_gas_natural = calcular_emissao(2.2, m3_gas_natural_mes)

    while True:
        try:
            kgs_glp_mes = float(input("Quantos kg de GLP você utiliza por mês?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_glp_mes = calcular_emissao(3, kgs_glp_mes)

    return emissao_energia_residencial + emissao_gas_natural + emissao_glp_mes


def emissao_alimentos():
    print("\nEsta última etapa é sobre sua alimentação.\n"
          "Vou fazer algumas perguntas sobre o seu consumo de alimentos.")
    while True:
        try:
            porcoes_carne_vermelha = int(input("Quantas vezes por semana você consome carne vermelha?\n"))
            break
        except ValueError:
            print("Valor inválido.")
    emissao_carne_vermelha = calcular_emissao(4.5, porcoes_carne_vermelha)

    while True:
        try:
            porcoes_frango = int(input("Quantas vezes por semana você consome frango?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_frango = calcular_emissao(1.1, porcoes_frango)

    while True:
        try:
            porcoes_peixe = int(input("Quantas vezes por semana você consome peixe?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_peixe = calcular_emissao(1.5, porcoes_peixe)

    while True:
        try:
            porcoes_ovos_laticinios = int(input("Quantas vezes por semana você consome ovos/laticínios?\n"))
            break
        except ValueError:
            print("Valor inválido.\n")
    emissao_ovos_laticinios = calcular_emissao(0.5, porcoes_ovos_laticinios)

    return emissao_carne_vermelha + emissao_frango + emissao_peixe + emissao_ovos_laticinios


# Ajustei todas as strings para corrigir erros gramaticais e melhorar a clareza das mensagens.


def iniciar_calculo():
    valor_emissao_veiculo = emissao_veiculos()
    valor_emissao_energia = emissao_energia()
    valor_emissao_alimento = emissao_alimentos()
    total_emissao = valor_emissao_alimento + valor_emissao_energia + valor_emissao_veiculo

    ultimos_calculos.append({
        "data_criacao": datetime.now().date().strftime("%d/%m/%Y"),  # .strftime("%d/%m/%Y")
        "valor_emissao_veiculo": valor_emissao_veiculo,
        "valor_emissao_energia": valor_emissao_energia,
        "valor_emissao_alimento": valor_emissao_alimento,
        "total_emissao": total_emissao
    })
    print(f"\nAqui estão seu niveis de emissão de carbono:\n"
          f"Você gerou {valor_emissao_veiculo:.2f} kg de CO2 em veiculos\n"
          f"Você gerou {valor_emissao_energia:.2f} kg de CO2 em energia\n"
          f"Você gerou {valor_emissao_alimento:.2f} kg de CO2 em alimentos\n"
          f"Em geral você produziu {total_emissao:.2f} kg de CO2")


def ver_dados():
    sum_total_emissao_carbono = 0

    maior_emissao_carbono = {
        "data_criacao": datetime,
        "total_emissao": 0
    }
    menor_emissao_carbono = {
        "data_criacao": datetime,
        "total_emissao": 999999999999999999999999999999
    }

    for calculo in ultimos_calculos:
        sum_total_emissao_carbono += calculo["total_emissao"]

        if calculo["total_emissao"] > maior_emissao_carbono["total_emissao"]:
            maior_emissao_carbono = calculo

        if calculo["total_emissao"] < menor_emissao_carbono["total_emissao"]:
            menor_emissao_carbono = calculo

    media_emissao = sum_total_emissao_carbono / len(ultimos_calculos)

    print("Aqui estão seus dados:\n"
          f"O total de carbono gerado por você foi de {sum_total_emissao_carbono:.2f} kg de CO2\n"
          f"Seu calculo de emissão do dia {maior_emissao_carbono["data_criacao"]} foi o que mais gerou CO2, gerando {maior_emissao_carbono["total_emissao"]:.2f} kg de CO2\n"
          f"Seu calculo de emissão do dia {menor_emissao_carbono["data_criacao"]} foi o que menos gerou CO2, gerando {menor_emissao_carbono["total_emissao"]:.2f} kg de CO2\n"
          f"Em média você gera {media_emissao:.2f} kg de CO2\n")


ultimos_calculos = []

while True:
    try:
        print("\nBem-vindo ao GreenPrint\n"
              "1. Iniciar cálculo de emissão de carbono\n"
              "2. Ver últimos dados\n"
              "0. Sair\n"
              "===========================================================")

        opcao = int(input("Digite a opção desejada:\n"))

        match opcao:
            case 0:
                print("Saindo...")
                break
            case 1:
                iniciar_calculo()
            case 2:
                ver_dados()
            case _:
                print("Opção inválida")
    except ValueError:
        print("Valor inválido")
