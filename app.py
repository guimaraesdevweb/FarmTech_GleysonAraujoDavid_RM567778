import streamlit as st
import pandas as pd

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="FarmTech Solutions - Torre de Controle",
    page_icon="🌱",
    layout="wide"
)

# 2. Menu Lateral de Navegação (Os 2 Links/Aba que pediste)
st.sidebar.title("🌱 FarmTech Solutions")
st.sidebar.markdown("---")
st.sidebar.subheader("Painel de Navegação")

# Cria a seleção de telas através de botões de rádio no menu lateral
opcao = st.sidebar.radio(
    "Ir para:",
    ["📊 Fase 1: Gestão de Insumos & Clima", "🧠 Fase 6: Visão Computacional (YOLOv5)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Sistema Integrado - FIAP Fase 7")

# ==========================================
# TELA 1: FASE 1 (Executada dentro do Projeto)
# ==========================================
if opcao == "📊 Fase 1: Gestão de Insumos & Clima":
    st.title("📊 Fase 1: Gestão Agrícola & Análise Climática")
    st.write("Esta secção integra os cálculos de manejo e a simulação de dados meteorológicos desenvolvidos na Fase 1.")
    
    # Divisão em duas colunas para o Layout ficar bonito
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧮 Calculadora de Manejo de Insumos")
        
        # Inputs interativos para o utilizador
        area = st.number_input("Área de Plantio (em Hectares):", min_value=1.0, value=10.0, step=1.0)
        cultura = st.selectbox("Tipo de Cultura:", ["Soja", "Milho", "Alface/Hortaliças"])
        
        # Lógica simples de cálculo baseada na cultura escolhida
        if cultura == "Soja":
            agua_por_hectare = 5000  # litros
            fertilizante_por_hectare = 200  # kg
        elif cultura == "Milho":
            agua_por_hectare = 6000
            fertilizante_por_hectare = 250
        else:
            agua_por_hectare = 3000
            fertilizante_por_hectare = 150
            
        total_agua = area * agua_por_hectare
        total_fert = area * fertilizante_por_hectare
        
        # Exibição dos resultados formatados
        st.success(f"**Resultados do Cálculo para {cultura}:**")
        st.metric(label="Necessidade de Água Total (Litros)", value=f"{total_agua:,} L")
        st.metric(label="Necessidade de Fertilizante Total (Kg)", value=f"{total_fert:,} Kg")

    with col2:
        st.subheader("🌤️ Monitorização Meteorológica (API Simulada)")
        st.write("Dados estatísticos consolidados sobre o clima da região da fazenda:")
        
        # Criação de um gráfico simples para simular a análise climática
        dados_clima = pd.DataFrame({
            'Dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
            'Temperatura (°C)': [26, 28, 25, 24, 27, 29, 30],
            'Umidade (%)': [70, 65, 80, 85, 72, 60, 55]
        })
        
        st.line_chart(dados_clima.set_index('Dia'))
        st.caption("Gráfico de evolução da Temperatura e Umidade com base nas análises estatísticas.")

# ==========================================
# TELA 2: FASE 6 (Link e Demonstração do Colab)
# ==========================================
elif opcao == "🧠 Fase 6: Visão Computacional (YOLOv5)":
    st.title("🧠 Fase 6: Detecção de Objetos com Inteligência Artificial")
    st.write("A nossa rede neural foi desenvolvida e treinada utilizando a infraestrutura de GPU do Google Colab.")
    
    st.markdown("---")
    
    # O LINK EXIGIDO: Botão de destaque para abrir o Colab
    st.subheader("🚀 Execução e Treinamento do Modelo")
    st.info("Para visualizar o código fonte, o histórico de treino (30 vs 60 épocas) e rodar novas inferências, aceda ao ambiente cloud oficial:")
    
    # ATENÇÃO: Substitui o link abaixo pelo link real do teu Google Colab da Fase 6
    link_do_seu_colab = "https://colab.research.google.com/drive/seu_link_aqui"
    
    st.link_button("👉 Abrir Notebook da Fase 6 no Google Colab", link_do_seu_colab, type="primary")
    
    st.markdown("---")
    
    # Vitrine de Resultados para impressionar o avaliador
    st.subheader("🖼️ Galeria de Resultados (Resultados do Treinamento)")
    st.write("Abaixo estão os exemplos das imagens de teste que descarregámos após a execução do YOLOv5 Customizado:")
    
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.markdown("**Exemplo 1: Detecção de Saúde Animal (Galo)**")
        # Dica: Coloca a foto do seu galo com o quadrado na mesma pasta do projeto
        # st.image("caminho_da_foto_do_galo_com_caixa.jpg", caption="Galo detectado com 43% de confiança (--conf 0.4)")
        st.warning("⚠️ [Dica do Dev]: Descomente a linha de código acima no VS Code e aponte para a imagem do seu Galo para exibi-la aqui!")
        
    with col_img2:
        st.markdown("**Exemplo 2: Análise de Campo (Flores)**")
        # st.image("caminho_da_foto_da_flor_com_caixa.jpg", caption="Flores detectadas após ajuste de sensibilidade (--conf 0.15)")
        st.warning("⚠️ [Dica do Dev]: Aponte aqui para o print das suas Flores com as caixas delimitadoras!")