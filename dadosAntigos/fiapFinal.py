# Utilizei duas culturas muito fortes aqui em Pernambuco: Café e feijão;
# Café (Plantio em formato de trapézio); Feijão (Plantio retangular);
# insumos: 

# Listas para armazenar os dados das culturas
# --- FUNÇÕES DE VALIDAÇÃO ---
from datetime import datetime

def ler_inteiro(mensagem):
    """Fica em loop até o usuário digitar um número inteiro válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            # Se o usuário apertar Enter duplo ou digitar letras, cai aqui:
            print("⚠️ Ops! Digite um número inteiro válido.")

def ler_float(mensagem):
    """Fica em loop até o usuário digitar um número decimal válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            # Captura o Enter vazio ou textos inválidos
            print("⚠️ Ops! Digite um número válido (use ponto para decimais).")

culturas = []
areas = []
insumos_totais = []

opcao = 0

while opcao != 5:
    print("\n--- MENU FARM TECH SOLUTIONS ---")
    print("1. Entrada de dados (Cadastrar Cultura)")
    print("2. Saída de dados (Exibir Culturas)")
    print("3. Atualizar dados de uma cultura")
    print("4. Deletar cultura")
    print("5. Sair do programa")
    
    
    opcao = ler_inteiro("Escolha uma opcao (1-5): ")
    
    # 1. ENTRADA DE DADOS
    if opcao == 1:
        print("\nCulturas disponiveis: 1 - Café | 2 - Feijao")
        # tipo = ler_inteiro("Digite o codigo da cultura: "))
        tipo = ler_inteiro("Digite o codigo da cultura: ")
        
        if tipo == 1:
            cultura = "Café"
            print("\nCalculo de Area: Trapezio (Talhao)")
            
            base_menor = ler_float("Digite a base menor (m): ")
            base_maior = ler_float("Digite a base maior (m): ")
            altura = ler_float("Digite a altura (m): ")
            area = ((base_menor + base_maior) * altura) / 2
            
            print("\nManejo de insumos (Fosfato)")
            dose_metro = ler_float("Digite a dose de insumo por metro linear (em kg): ")
            ruas = ler_inteiro("Quantidade de ruas na lavoura: ")
            comprimento_rua = ler_float("Comprimento medio da rua (m): ")
            insumo_necessario = dose_metro * comprimento_rua * ruas
            
        elif tipo == 2:
            cultura = "Feijao"
            print("\nCalculo de Area: Retangulo")
            largura = ler_float("Digite a largura (m): ")
            comprimento = ler_float("Digite o comprimento (m): ")
            area = largura * comprimento
            
            print("\nManejo de insumos (Pulverizacao)")
            dose_metro = ler_float("Digite a dose de defensivo por metro linear (em litros): ")
            ruas = ler_inteiro("Quantidade de ruas na lavoura: ")
            comprimento_rua = ler_float("Comprimento medio da rua (m): ")
            insumo_necessario = dose_metro * comprimento_rua * ruas
            
        else:
            print("Cultura invalida!")
            continue

        culturas.append(cultura)
        areas.append(area)
        insumos_totais.append(insumo_necessario)
        print(f"{cultura} cadastrada com sucesso!")

   # 2. SAÍDA DE DADOS
    elif opcao == 2:
        print("\n--- RELATÓRIO DE CULTURAS --- \n")
        if len(culturas) == 0:
            print("Nenhuma cultura cadastrada.")
        else:
            # 1. O laço 'for' serve APENAS para imprimir na tela
            for i in range(len(culturas)):
                print(f"ID {i}: Cultura: {culturas[i]} | Área: {areas[i]:.2f} m² | Insumo Previsto: {insumos_totais[i]:.2f} kg")
                print ("-------------------------------------------------------------------")

            # 2. FORA do laço 'for' (mesmo alinhamento dele), nós geramos o arquivo UMA ÚNICA VEZ
            print("\nGerando um relatório para a linguagem R... ")
            
            # Captura a data e hora exata de agora
            agora = datetime.now()

            # Formata para: YYYY-mm-dd_H-M-S
            data_hora_formatada = agora.strftime("%Y-%m-%d_%H-%M-%S")
        
            # Monta o nome do arquivo dinamicamente usando a f-string
            nome_arquivo_r = f"dados_culturas_{data_hora_formatada}.R"

            # 3. Bloco 'with': TUDO que for escrito no arquivo precisa ter esse espaço extra (Tab)
            with open(nome_arquivo_r, "w", encoding="utf-8") as arquivo:
                arquivo.write("# ==================================================\n")
                arquivo.write("# Script de dados gerado automaticamente pelo Python\n")
                arquivo.write("# ==================================================\n\n")
                
                # Formata os textos para o R com aspas
                culturas_formatadas = [f'"{c}"' for c in culturas]
                
                # Formatando os números para terem apenas 3 casas decimais antes de ir para o R
                areas_formatadas = [f"{a:.3f}" for a in areas]
                insumos_formatados = [f"{i:.3f}" for i in insumos_totais]
                
                # Cria os vetores no arquivo R
                arquivo.write(f"vetor_culturas <- c({', '.join(culturas_formatadas)})\n")
                arquivo.write(f"vetor_areas <- c({', '.join(areas_formatadas)})\n")
                arquivo.write(f"vetor_insumos <- c({', '.join(insumos_formatados)})\n\n")
                
                # Monta a tabela (Data Frame) no R
                arquivo.write("# Criando a tabela estatística (Data Frame)\n")
                arquivo.write("df_culturas <- data.frame(\n")
                arquivo.write("  Cultura = vetor_culturas,\n")
                arquivo.write("  Area_m2 = vetor_areas,\n")
                arquivo.write("  Insumo_kg = vetor_insumos\n")
                arquivo.write(")\n\n")
                
                arquivo.write("# Comandos prontos para análise:\n")
                arquivo.write("print(df_culturas)\n")
                arquivo.write("summary(df_culturas)\n")
                
            # Este print final fica fora do 'with', indicando que o arquivo já foi fechado e salvo
            print(f"🚀 [Sucesso] O arquivo '{nome_arquivo_r}' foi gerado com sucesso!")

    # 3. ATUALIZAÇÃO DE DADOS
    elif opcao == 3:
        idx = ler_inteiro("Digite o ID da cultura que deseja atualizar: ")
        if idx < len(culturas):
            print(f"Atualizando {culturas[idx]}")
            nova_area = ler_float("Digite o novo valor de área (m²): ")
            novo_insumo = ler_float("Digite o novo valor total de insumo: ")
            areas[idx] = nova_area
            insumos_totais[idx] = novo_insumo
            print("Dados atualizados com sucesso.")
        else:
            print("ID invalido.")

    # 4. DELEÇÃO DE DADOS
    elif opcao == 4:
        idx = ler_inteiro("Digite o ID da cultura que deseja deletar: ")
        if idx < len(culturas):
            removida = culturas.pop(idx)
            areas.pop(idx)
            insumos_totais.pop(idx)
            print(f"{removida} deletada com sucesso.")
        else:
            print("ID invalido.")

    # 5. SAIR
    elif opcao == 5:
        print("Encerrando o programa. Até logo!")
    
    else:
        print("Opcao inválida, tente novamente.")

